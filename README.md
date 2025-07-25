# Ryanair Sitemap Parser

A Python script that crawls and parses Ryanair's sitemap structure to extract all URLs and save them to an Excel file.

---

## Description

This script fetches Ryanair's main sitemap XML file, discovers all linked sitemaps, and extracts URLs from each sitemap. The results are compiled into a structured Excel file with the source sitemap and extracted URLs.

---

## Features

- Fetches the main Ryanair sitemap (`https://www.ryanair.com/sitemap.xml`)
- Discovers and parses all linked sitemap files
- Extracts URLs from each sitemap using XML parsing
- Outputs results to Excel format in long format (one URL per row)
- Includes duplicate detection and reporting
- Error handling for failed requests

---

## Requirements

Install the required dependencies:

```bash
pip install pandas beautifulsoup4 requests lxml
```

---

## Dependencies

- `pandas` - Data manipulation and Excel output
- `beautifulsoup4` - XML/HTML parsing
- `requests` - HTTP requests
- `lxml` - XML parser backend for BeautifulSoup

---

## Usage

Run the script directly:

```bash
python sitemap_parser.py
```

The script will:

1. Fetch the main sitemap
2. Extract all sitemap URLs
3. Parse each sitemap for URLs
4. Save results to `parsed_urls_long_format_loctext_only.xlsx`

---

## Output

The script generates an Excel file with two columns:

- `LOC`: The source sitemap URL
- `URLS`: The extracted URL from that sitemap

---

## Output Format

The data is stored in "long format" where each row represents one URL with its source sitemap. This format is useful for analysis and filtering.

---

## Error Handling

The script includes error handling for:

- Failed HTTP requests
- Invalid XML content
- Network timeouts

Errors are printed to console with details about which URL failed to process.

---

## Code Structure

- `parse_xml()` - Function to extract URLs from XML sitemap content
- Main loop processes each sitemap URL
- Results are flattened into a pandas DataFrame
- Duplicate detection (reported but not removed by default)

---

## Notes

- The script reports the number of duplicates found but doesn't remove them by default
- Commented code shows alternative approach for extracting `xhtml:link` elements
- Processing time depends on the number of sitemaps and network speed

---

## Customization

To modify the script:

- Change the base sitemap URL in the `requests.get()` call
- Uncomment the duplicate removal line if needed: `df_long = df_long.drop_duplicates()`
- Modify the output filename in the `to_excel()` call
- Adjust the XML parsing logic in `parse_xml()` for different sitemap structures
