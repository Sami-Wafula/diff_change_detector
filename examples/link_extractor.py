import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_unique_links(url):
    """
    Fetches a URL and returns a sorted list of unique absolute URLs found on the page.
    """
    links = set()
    
    try:
        # 1. Set a user-agent to look like a real browser
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        # 2. Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return []

        # 3. Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 4. Find all 'a' tags with an 'href' attribute
        for anchor in soup.find_all('a', href=True):
            link = anchor['href']
            
            # 5. Convert relative links to absolute URLs
            absolute_link = urljoin(url, link)
            
            # 6. Basic validation: ensure it's a web link (http or https)
            parsed_link = urlparse(absolute_link)
            if parsed_link.scheme in ['http', 'https']:
                links.add(absolute_link)
                
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return []
    
    # 7. Return sorted list for readability
    return sorted(list(links))

# Example Usage (Note: Requires 'pip install requests beautifulsoup4'):
# print(get_unique_links("https://www.python.org"))
