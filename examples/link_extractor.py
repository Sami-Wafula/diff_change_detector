import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_hyperlinks_from_url(target_url):
    """
    Connects to a website, parses the HTML, and extracts all unique URLs.
    
    This function handles:
    - HTTP Request headers to bypass basic bot filters.
    - Network timeout and connection error exceptions.
    - Conversion of relative links (/about) to absolute links (https://site.com).
    - Filtering for valid web protocols (HTTP/HTTPS).
    """

    # 1. INITIALIZATION: Create a set to store unique links.
    # Using a 'set' automatically prevents duplicate URLs.
    unique_links = set()

    # 2. HEADERS: Define a User-Agent.
    # Some servers block requests that don't look like they come from a browser.
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    # 3. REQUEST: Attempt to fetch the page content.
    # We wrap this in a try-except block to handle internet outages or 404s.
    try:
        # We set a timeout of 10 seconds so the script doesn't hang forever.
        response = requests.get(target_url, headers=request_headers, timeout=10)
        
        # Raise an exception for bad status codes (like 403 or 500).
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An unexpected error occurred: {err}"

    # 4. PARSING: Use BeautifulSoup to navigate the HTML 'soup'.
    # 'html.parser' is built into Python; no extra C-dependencies required.
    html_soup = BeautifulSoup(response.text, 'html.parser')

    # 5. EXTRACTION: Find every 'a' (anchor) tag in the document.
    # We only care about tags that actually have an 'href' attribute.
    for anchor_tag in html_soup.find_all('a', href=True):
        raw_href = anchor_tag['href']

        # 6. RESOLUTION: Convert relative paths to absolute URLs.
        # Example: if target is 'google.com', it turns '/mail' into '://google.com'.
        full_url = urljoin(target_url, raw_href)

        # 7. FILTERING: Validate the URL structure.
        # We parse the URL to ensure it has a scheme (http) and a network location.
        parsed_parts = urlparse(full_url)
        if parsed_parts.scheme in ['http', 'https'] and parsed_parts.netloc:
            # Add to set (duplicates are ignored automatically).
            unique_links.add(full_url)

    # 8. OUTPUT: Convert the set back to a list and sort alphabetically.
    # This makes the output predictable and easy to read.
    sorted_links = sorted(list(unique_links))

    return sorted_links
