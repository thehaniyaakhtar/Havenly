import pandas as pd

# Step 1: Define path and desired columns
input_path = "data/BenefitsCostSharing.csv"
output_path = "data/filtered_benefits.csv"
columns_to_keep = [
    "PlanId",
    "BenefitName",
    "IsCovered",
    "CoinsInnTier1",
    "CopayInnTier1",
    "Exclusions",
    "Explanation",
    "StateCode"
]

# Step 2: Read file in chunks
chunksize = 100000  # Adjust based on your system
chunks = pd.read_csv(input_path, chunksize=chunksize, usecols=lambda col: col in columns_to_keep, low_memory=False)

# Step 3: Write filtered chunks to new CSV
first_chunk = True
for chunk in chunks:
    chunk = chunk.dropna(subset=["PlanId", "BenefitName"])  # Drop invalid rows
    chunk.to_csv(output_path, mode='w' if first_chunk else 'a', index=False, header=first_chunk)
    first_chunk = False

print("✅ Trimmed benefits saved to:", output_path)
