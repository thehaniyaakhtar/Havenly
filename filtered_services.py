import pandas as pd

# Load service area file
df = pd.read_csv("filtered_service_area.csv", low_memory=False)

keep_cols = [
    "ServiceAreaId", "StateCode", "CoverEntireState"
]

df = df[keep_cols]

# Drop rows missing ServiceAreaId
df.dropna(subset=["ServiceAreaId"], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned file
df.to_csv("filtered_service_area2.csv", index=False)
print("✅ Cleaned: filtered_service_area_clean.csv")
