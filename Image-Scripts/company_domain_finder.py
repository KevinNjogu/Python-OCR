import json
import requests
from urllib.parse import quote_plus
import time
from collections import defaultdict

class CompanyDomainFinder:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def find_domain_using_clearbit(self, company_name):
        """Try to find domain using Clearbit's Autocomplete API"""
        try:
            url = f"https://autocomplete.clearbit.com/v1/companies/suggest?query={quote_plus(company_name)}"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                suggestions = response.json()
                if suggestions and len(suggestions) > 0:
                    # Return the first suggestion's domain
                    return suggestions[0].get('domain')
        except Exception as e:
            print(f"Clearbit API error for {company_name}: {str(e)}")
        return None

    def find_domain_using_search(self, company_name):
        """Backup method: Try to find domain using a search engine"""
        try:
            search_query = f"{company_name} official website"
            search_url = f"https://www.google.com/search?q={quote_plus(search_query)}"
            
            response = requests.get(search_url, headers=self.headers)
            
            if response.status_code == 200:
                # Very basic parsing - in production you'd want more robust parsing
                text = response.text.lower()
                
                # Look for common patterns in search results
                company_name_parts = company_name.lower().split()
                
                # Find URLs in the response that might match the company
                start_indices = []
                for protocol in ['https://', 'http://']:
                    pos = 0
                    while True:
                        pos = text.find(protocol, pos)
                        if pos == -1:
                            break
                        start_indices.append(pos)
                        pos += 1

                potential_domains = []
                for start in start_indices:
                    end = text.find('/', start + 8)
                    if end != -1:
                        domain = text[start:end].replace('https://', '').replace('http://', '').replace('www.', '')
                        potential_domains.append(domain)

                # Score domains based on similarity to company name
                domain_scores = defaultdict(int)
                for domain in potential_domains:
                    domain_parts = domain.split('.')
                    if len(domain_parts) >= 2:  # Must have at least a name and TLD
                        base_domain = domain_parts[0]
                        for company_part in company_name_parts:
                            if company_part in base_domain:
                                domain_scores[domain] += 1

                # Return the domain with the highest score
                if domain_scores:
                    return max(domain_scores.items(), key=lambda x: x[1])[0]
                
        except Exception as e:
            print(f"Search error for {company_name}: {str(e)}")
        return None

    def process_companies(self, companies):
        """Process a list of company names and find their domains"""
        results = []
        
        for company in companies:
            print(f"Processing: {company}")
            
            # Try Clearbit first
            domain = self.find_domain_using_clearbit(company)
            
            # If Clearbit fails, try search method
            if not domain:
                domain = self.find_domain_using_search(company)
            
            results.append({
                "company": company,
                "domain": domain
            })
            
            # Sleep to avoid rate limiting
            time.sleep(1)
        
        return results

def main():
    # Load companies from JSON file
    try:
        with open('companies.json', 'r') as f:
            companies = json.load(f)
    except FileNotFoundError:
        print("Please create a companies.json file with your company names")
        return
    except json.JSONDecodeError:
        print("Invalid JSON format in companies.json")
        return

    # Process companies
    finder = CompanyDomainFinder()
    results = finder.process_companies(companies)
    
    # Save results
    with open('company_domains.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print results
    print("\nResults:")
    for result in results:
        print(f"{result['company']}: {result['domain'] or 'Not found'}")

if __name__ == "__main__":
    main()