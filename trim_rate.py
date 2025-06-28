import pandas as pd

input_path = "data/Rate.csv"
output_path = "data/filtered_rate.csv"

columns_to_keep = [
    "PlanId",
    "Age",
    "Tobacco",
    "IndividualRate",
    "IndividualTobaccoRate",
    "PrimarySubscriberAndOneDependent",
    "PrimarySubscriberAndTwoDependents",
    "Couple",
    "CoupleAndOneDependent",
    "CoupleAndTwoDependents",
    "StateCode",
    "RateEffectiveDate",
    "RateExpirationDate"
]

chunksize = 100000
chunks = pd.read_csv(input_path, chunksize=chunksize, usecols=lambda col: col in columns_to_keep, low_memory=False)

first_chunk = True
for chunk in chunks:
    chunk = chunk.dropna(subset=["PlanId", "Age", "IndividualRate"])
    chunk.to_csv(output_path, mode='w' if first_chunk else 'a', index=False, header=first_chunk)
    first_chunk = False

print("✅ Trimmed rate data saved to:", output_path)
