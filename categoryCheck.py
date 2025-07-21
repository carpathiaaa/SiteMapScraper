import pandas as pd

# Load your data
df = pd.read_excel(r'C:\Users\Charles Jung\Documents\CebPacOperations\RyanAirSitemap\urls_split_by_segments.xlsx')

# List of segments of concern
segments_of_concern = [
    'flights',
    'try-somewhere-new',
    'plan-trip',
    'corporate',
    'useful-info',
    'airports-and-tourism0',
    'special-offer',
    'check-in',
    'fare-finder',
    'flight-info',
    'gift-vouchers',
    'header',
    'register',
    'timetable',
    'lp'
]

# Normalize flight-related values
def normalize_flight(value):
    if isinstance(value, str) and 'flight' in value:
        return 'flight'
    return value

# Apply normalization to SEG_3
df['SEG_3_NORMALIZED'] = df['SEG_3'].apply(normalize_flight)

# Identify matches in SEG_1 or SEG_3
seg1_concern = df[df['SEG_1'].isin(segments_of_concern)].copy()
seg1_concern['Segment_of_Concern'] = seg1_concern['SEG_1']
seg1_concern['Source_SEG'] = 'SEG_1'

seg3_concern = df[df['SEG_3_NORMALIZED'].isin(segments_of_concern)].copy()
seg3_concern['Segment_of_Concern'] = df['SEG_3_NORMALIZED']
seg3_concern['Source_SEG'] = 'SEG_3'

# Combine both
concern_df = pd.concat([seg1_concern, seg3_concern], ignore_index=True)

# Ensure consistent columns
columns = ['Segment_of_Concern', 'Source_SEG'] + [col for col in concern_df.columns if col not in ['Segment_of_Concern', 'Source_SEG']]
concern_df = concern_df[columns]

# Build collection from SEG_4
collected = {segment: [] for segment in segments_of_concern}

for _, row in concern_df.iterrows():
    seg_concern = row['Segment_of_Concern']
    seg4_val = row.get('SEG_4', None)
    if pd.notna(seg4_val):
        collected[seg_concern].append(seg4_val)

# Remove duplicates
for key in collected:
    collected[key] = list(dict.fromkeys(collected[key]))

# Pad for equal-length columns
max_len = max(len(v) for v in collected.values())
for key in collected:
    while len(collected[key]) < max_len:
        collected[key].append(None)

# Create final DataFrame
result_df = pd.DataFrame(collected)

# Save to Excel
result_df.to_excel("segment_of_concern_from_SEG4.xlsx", index=False)

# Preview
print(result_df.head())
