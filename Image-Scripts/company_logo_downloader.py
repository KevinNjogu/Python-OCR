import json
import os
import requests
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()
logo_dev_secret_key = os.getenv("LOGO_DEV_SECRET_KEY")

def download_company_logos(companies: List[Dict[str, str]], 
                            api_token: str, 
                            output_dir: str = 'batch-9001-10_000/logos'):
    """
        Download logos for a list of companies using Logo.dev API
        
        Args:
            companies (List[Dict]): List of dictionaries with 'company' and 'domain' keys
            api_token (str): Authorization token for Logo.dev API
            output_dir (str, optional): Directory to save logos. Defaults to 'company_logos'.
        
        Returns:
            List[Dict]: Updated companies list with logo download status
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Results to track
    results = []
    
    for company in companies:
        try:
            # Prepare the API request
            search_url = f"https://api.logo.dev/search?q={company['company']}"
            headers = {
                "Authorization": f"Bearer: {api_token}"
            }
            
            # Perform the search request
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()
            
            # Parse the search results
            logo_results = response.json()
            
            # Find the best matching logo (exact domain match preferred)
            best_match = None
            for logo_info in logo_results:
                if logo_info['domain'].lower() == company['domain'].lower():
                    best_match = logo_info
                    break
            
            # If no exact match, take the first result
            if not best_match and logo_results:
                best_match = logo_results[0]
            
            if best_match:
                # Download the logo
                logo_url = best_match['logo_url']
                logo_response = requests.get(logo_url)
                logo_response.raise_for_status()
                
                # Create filename (use domain to avoid special character issues)
                filename = os.path.join(output_dir, f"{best_match['domain'].replace('.', '_')}_logo.png")
                
                # Save the logo
                with open(filename, 'wb') as f:
                    f.write(logo_response.content)
                
                # Update result with logo information
                result = company.copy()
                result.update({
                    'logo_url': logo_url,
                    'logo_path': filename,
                    'matched_name': best_match['name']
                })
                results.append(result)
                
                print(f"Downloaded logo for {company['company']} from {best_match['name']}")
            else:
                print(f"No logo found for {company['company']}")
                
        except Exception as e:
            print(f"Error processing {company['company']}: {str(e)}")
            results.append({
                **company,
                'error': str(e)
            })
    
    return results

def main():
    # Read companies from JSON
    try:
        with open('batch-9001-10_000/batch-9001-10_000-domains.json', 'r') as f:
            companies = json.load(f)
    except FileNotFoundError:
        print("batch-9001-10_000/batch-9001-10_000-domains.json not found. Using example data.")
        companies = [
            {
                "company": "Apple",
                "domain": "apple.com"
            },
            {
                "company": "Travelers Companies Inc",
                "domain": "travelers.com"
            },
            {
                "company": "Unitedhealth Group Inc",
                "domain": "unitedhealthgroup.com"
            },
            {
                "company": "Salesforce Inc",
                "domain": "salesforce.com"
            },
            {
                "company": "Verizon Communications Inc",
                "domain": "verizon.com"
            }
        ]
    
    # API Token (replace with your actual token)
    API_TOKEN = logo_dev_secret_key
    
    # Download logos
    logo_results = download_company_logos(companies, API_TOKEN)
    
    # Write results to JSON
    with open('batch-9001-10_000/batch-9001-10_000-logo-download-results.json', 'w') as f:
        json.dump(logo_results, f, indent=4)

if __name__ == "__main__":
    main()