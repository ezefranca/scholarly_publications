import requests
from bs4 import BeautifulSoup
import time

# Constants for headers, cookies, etc., can be defined here
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}

COOKIES = {
    'CONSENT': 'PENDING+300',
}

def fetch_all_publications(author_id, max_publications=None):
    all_publications = []
    start_index = 0
    page_size = 100
    total_fetched = 0

    while True:
        if max_publications is not None and total_fetched >= max_publications:
            break

        params = {
            'user': author_id,
            'oi': 'ao',
            'cstart': start_index,
            'pagesize': page_size,
        }

        response = requests.get('https://scholar.google.com/citations', params=params, cookies=COOKIES, headers=HEADERS)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            publications = parse_publications(soup)
            if publications:
                if max_publications is not None:
                    remaining = max_publications - total_fetched
                    publications = publications[:remaining]

                all_publications.extend(publications)
                total_fetched += len(publications)

                if len(publications) < page_size:
                    break
                start_index += page_size
            else:
                break
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            break
        # Delay to prevent hitting rate limits
        time.sleep(1)  

    return all_publications

def parse_publications(soup):
    publications_list = []
    for row in soup.select('.gsc_a_tr'):
        title_element = row.select_one('.gsc_a_at')
        title = title_element.text.replace(':', ' -') if title_element else "No title"
        year_element = row.select_one('.gsc_a_h')
        year = year_element.text if year_element else "No year"
        link = f'https://scholar.google.com{title_element["href"]}' if title_element else "No link"
        citation_element = row.select_one('.gsc_a_ac')
        citations = citation_element.text if citation_element and citation_element.text.strip() else "0"  # Check if text exists and is not empty

        publications_list.append({
            'title': title,
            'year': year,
            'link': link,
            'citations': citations,
        })

    return publications_list