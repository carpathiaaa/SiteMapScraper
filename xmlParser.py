import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.read_excel(r"C:\Users\Charles Jung\Documents\CebPacOperations\RyanAirSitemap\InitialURLScraper\ryanair_valid_urls.xlsx")
second_half = df.iloc[118::]

second_half_urls = second_half['URL'].tolist()
print(len(second_half_urls))

entry = {}

def parse_xml(xml_content):
    soup = BeautifulSoup(xml_content, "xml")
    urls = []

    for url_tag in soup.find_all('url'):
        loc_tag = url_tag.find('loc')
        if loc_tag:
            urls.append(loc_tag.text)

        href_tags = url_tag.find_all('xhtml:link')

        for tag in href_tags:
            href = tag.get('href')
            urls.append(href)

    return urls


for url in second_half_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        xml_content = response.text
        parsed_urls = parse_xml(xml_content)
        entry[url] = parsed_urls
        print(f"Parsed {len(parsed_urls)} URLs from {url}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

# Flatten the dictionary into a list of dictionaries
flat_data = []

for filepath, urls in entry.items():
    for url in urls:
        flat_data.append({"LOC": filepath, "URLS": url})

# Create long-format DataFrame
df_long = pd.DataFrame(flat_data)

# Save to Excel
df_long.to_excel("parsed_urls_long_format.xlsx", index=False)