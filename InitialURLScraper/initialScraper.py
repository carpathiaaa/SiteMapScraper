from bs4 import BeautifulSoup
import pandas as pd

# Load the uploaded XML file
with open("sitemap.xml", "r", encoding="utf-8") as file:
    xml_content = file.read()

# Parse XML and extract all <loc> elements
soup = BeautifulSoup(xml_content, "xml")
urls = [loc_tag.text for loc_tag in soup.find_all("loc")]

# Create a DataFrame and save to Excel
df = pd.DataFrame(urls, columns=["URL"])
excel_path = "ryanair_valid_urls.xlsx"
df.to_excel(excel_path, index=False)

excel_path
