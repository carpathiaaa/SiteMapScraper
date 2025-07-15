import pandas as pd
from urllib.parse import urlparse

# Load your DataFrame
df = pd.read_excel(r'C:\Users\Charles Jung\Documents\CebPacOperations\RyanAirSitemap\parsed_urls_long_format_loctext_only.xlsx')

df_eng = df[df['LOC'].str.contains('gb/en')].copy()

# Function to split path into segments
def split_url_segments(url):
    try:
        parsed = urlparse(url)
        path_parts = parsed.path.strip("/").split("/")
        return path_parts
    except Exception:
        return []

# Apply and expand into new columns
split_cols = df_eng['URLS'].apply(split_url_segments).apply(pd.Series)

# Rename columns dynamically: SEG_1, SEG_2, ...
split_cols.columns = [f'SEG_{i+1}' for i in range(split_cols.shape[1])]

# Combine with original DataFrame if you want
df_split = pd.concat([df_eng, split_cols], axis=1)

# Optional: Save or inspect
print(df_split.head())
df_split.to_excel("urls_split_by_segments.xlsx", index=False)
