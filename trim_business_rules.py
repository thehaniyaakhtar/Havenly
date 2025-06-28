import pandas as pd

input_path = "data/BusinessRules.csv"
output_path = "data/filtered_business_rules.csv"

columns_to_keep = [
    "StandardComponentId",
    "DependentMaximumAgRule",
    "TwoParentFamilyMaxDependentsRule",
    "SingleParentFamilyMaxDependentsRule",
    "ChildrenOnlyContractMaxChildrenRule",
    "DomesticPartnerAsSpouseIndicator",
    "SameSexPartnerAsSpouseIndicator",
    "MinimumTobaccoFreeMonthsRule",
    "DentalOnlyPlan",
    "MarketCoverage",
    "StateCode"
]

chunksize = 100000
chunks = pd.read_csv(input_path, chunksize=chunksize, usecols=lambda col: col in columns_to_keep, low_memory=False)

first_chunk = True
for chunk in chunks:
    chunk = chunk.dropna(subset=["StandardComponentId"])
    chunk.to_csv(output_path, mode='w' if first_chunk else 'a', index=False, header=first_chunk)
    first_chunk = False

print("✅ Trimmed business rules saved to:", output_path)
