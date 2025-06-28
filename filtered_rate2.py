import pandas as pd

# Load existing file
df = pd.read_csv("filtered_rate.csv")

# Convert Age to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df = df.dropna(subset=["Age"])

# Filter valid age range
df = df[df["Age"].between(18, 64)]

# Keep only non-tobacco for simplicity
df = df[df["Tobacco"].str.lower() == "no"]

# Drop rows without rate info
df = df.dropna(subset=["IndividualRate"])

# Average rate per PlanId and State
avg_rates = (
    df.groupby(["PlanId", "StateCode"])["IndividualRate"]
    .mean()
    .reset_index()
    .rename(columns={"IndividualRate": "AvgIndividualRate"})
)

# Save cleaned and compressed rate file
avg_rates.to_csv("filtered_rate2.csv", index=False)
print("✅ Super-trimmed: filtered_rate2.csv")
