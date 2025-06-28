import pandas as pd

input_path = "data/ServiceArea.csv"
output_path = "data/filtered_service_area.csv"

columns_to_keep = [
    "ServiceAreaId",
    "StateCode",
    "County",
    "ZipCodes",
    "CoverEntireState"
]

chunksize = 100000
chunks = pd.read_csv(input_path, chunksize=chunksize, usecols=lambda col: col in columns_to_keep, low_memory=False)

first_chunk = True
for chunk in chunks:
    chunk = chunk.dropna(subset=["ServiceAreaId", "StateCode"])
    chunk.to_csv(output_path, mode='w' if first_chunk else 'a', index=False, header=first_chunk)
    first_chunk = False

print("✅ Trimmed service area data saved to:", output_path)
