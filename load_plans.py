import pandas as pd

# Load the raw dataset
df = pd.read_csv("filtered_plans.csv", low_memory=False)

# Select only useful columns
columns_to_keep = [
    "PlanId", "PlanMarketingName", "MetalLevel", "PlanType", "MarketCoverage",
    "ChildOnlyOffering", "ChildOnlyPlanId", "IsHSAEligible", "IsNewPlan", "IsGuaranteedRate",
    "WellnessProgramOffered", "DiseaseManagementProgramsOffered", "OutOfCountryCoverage",
    "OutOfCountryCoverageDescription", "OutOfServiceAreaCoverage", "OutOfServiceAreaCoverageDescription",
    "SpecialistRequiringReferral", "IssuerActuarialValue", "StateCode",
    "ServiceAreaId", "NetworkId", "StandardComponentId", "DentalOnlyPlan",
    "IsNoticeRequiredForPregnancy"
]

# Apply filter
df_filtered = df[columns_to_keep]

# Drop rows missing key plan info
df_filtered.dropna(subset=["PlanMarketingName", "MetalLevel", "PlanType"], inplace=True)

# Drop duplicate plans
df_filtered.drop_duplicates(subset=["PlanId"], inplace=True)

# Save final cleaned dataset
df_filtered.to_csv("filtered_plan_attributes_trimmed.csv", index=False)

print("✅ Cleaned dataset saved as 'filtered_plan_attributes_trimmed.csv'")
