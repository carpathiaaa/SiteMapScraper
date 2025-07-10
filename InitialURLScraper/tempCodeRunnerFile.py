import pandas as pd
import re

# Load your Excel file (replace with your actual file name)
df = pd.read_excel("ryanair_valid_urls.xlsx")  # Make sure it has a 'URL' column

# Define a list of common ISO 639-1 language codes
common_lang_codes = {
    'en', 'de', 'fr', 'it', 'es', 'pt', 'pl', 'nl', 'da', 'no', 'fi', 'sv', 'cs', 'sk',
    'ro', 'hu', 'bg', 'hr', 'lt', 'lv', 'et', 'sl', 'el', 'tr', 'ru', 'uk', 'zh', 'sr', 'mt', 'ma', 'cy'
}

# Function to extract language code from anywhere in the URL after '.com/'
def extract_language(url):
    match = re.search(r"\.com/((?:[a-z]{2}/)+)", url)
    if match:
        parts = match.group(1).split('/')
        for part in parts:
            if part in common_lang_codes:
                return part
    return None

# Apply the function to extract language codes
df['Language'] = df['URL'].apply(extract_language)

# Sort by the extracted language
df_sorted = df.sort_values(by='Language', na_position='last')

# Save the result
df_sorted.to_excel("sorted_by_language.xlsx", index=False)
