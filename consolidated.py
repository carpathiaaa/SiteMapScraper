import pandas as pd
from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.ryanair.com/sitemap.xml")
soup = BeautifulSoup(response.content, "xml")
urls = [loc_tag.text for loc_tag in soup.find_all("loc")]

entry = {}

def parse_xml(xml_content):
    soup = BeautifulSoup(xml_content, "xml")
    urls = []

    for url_tag in soup.find_all('url'):
        loc_tag = url_tag.find('loc')
        if loc_tag:
            urls.append(loc_tag.text)

        '''href_tags = url_tag.find_all('xhtml:link')

        for tag in href_tags:
            href = tag.get('href')
            urls.append(href)'''

    return urls


for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        xml_content = response.text
        parsed_urls = parse_xml(xml_content)
        entry[url] = parsed_urls
        print(f"Parsed {len(parsed_urls)} URLs from {url}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

flat_data = []

for filepath, urls in entry.items():
    for url in urls:
        flat_data.append({"LOC": filepath, "URLS": url})

df_long = pd.DataFrame(flat_data)
print(df_long.duplicated().sum())
#df_long = df_long.drop_duplicates()


df_long.to_excel("parsed_urls_long_format_loctext_only.xlsx", index=False)