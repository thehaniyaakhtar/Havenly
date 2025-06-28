import google.generativeai as genai
import pandas as pd
import re

genai.configure(api_key="AIzaSyAPBF6D_wymLzS4t4l95O2xfV0swzD91Qc")
model = genai.GenerativeModel("models/gemini-1.5-flash-002")
policy_df = pd.read_csv("filtered_plans.csv")

def filter_policies(user_input, exclude_names=None):
    if exclude_names is None:
        exclude_names = []

    keywords = {
        "wellness": "WellnessProgramOffered",
        "maternity": "IsNoticeRequiredForPregnancy",
        "pregnancy": "IsNoticeRequiredForPregnancy",
        "child": "ChildOnlyOffering",
        "disease": "DiseaseManagementProgramsOffered",
        "ppo": "PlanType",
        "hmo": "PlanType",
    }

    mask = pd.Series([False] * len(policy_df))

    for word, col in keywords.items():
        if re.search(rf"\b{word}\b", user_input.lower()) and col in policy_df.columns:
            mask |= policy_df[col].astype(str).str.contains("Yes|1|True|PPO|HMO", case=False, na=False)

    metal_levels = ["gold", "silver", "bronze", "platinum"]
    requested_levels = [lvl.capitalize() for lvl in metal_levels if lvl in user_input.lower()]

    filtered = policy_df[mask].dropna(subset=["PlanMarketingName"])

    if requested_levels:
        filtered = filtered[filtered["MetalLevel"].isin(requested_levels)]

    if exclude_names:
        filtered = filtered[~filtered["PlanMarketingName"].isin(exclude_names)]

    return filtered.drop_duplicates(subset=["PlanMarketingName"]).head(3)

def format_policies(df):
    output = []
    for _, row in df.iterrows():
        plan = f"""🔹 **{row['PlanMarketingName']}**
- Metal Level: {row.get('MetalLevel', 'N/A')}
- Plan Type: {row.get('PlanType', 'N/A')}
- Wellness: {row.get('WellnessProgramOffered', 'N/A')}
- Disease Mgmt: {row.get('DiseaseManagementProgramsOffered', 'N/A')}
- Maternity Support: {row.get('IsNoticeRequiredForPregnancy', 'N/A')}
"""
        output.append(plan)
    return "\n".join(output)

def get_gemini_response(user_input: str, exclude_names: list = []) -> tuple[str, list[str]]:
    try:
        policies = filter_policies(user_input, exclude_names)
        if policies.empty:
            return "❌ I couldn't find any new matching policies.", []

        policy_str = format_policies(policies)

        prompt = f"""
You’re a helpful AI insurance advisor.

The user said:
\"{user_input}\"

Here are 3 new relevant plans:

{policy_str}

Pick the most suitable plan from the options above.
Always explain your reasoning in human terms.
If none are a perfect match, recommend the closest one anyway — never say “none are suitable.” 
Offer a solution or workaround (like suggesting a rider or budget tweak).

If the user asks a follow-up "what if" question (like changing tier, increasing budget, or adding coverage), treat it as a change to the previous request and recommend a new plan set accordingly.

End your message with a friendly follow-up question like:
- “Want me to show other plans with maternity support?”
- “Would you like to compare these with Bronze plans instead?”
"""

        response = model.generate_content(prompt)
        return response.text.strip(), list(policies["PlanMarketingName"])

    except Exception as e:
        return f"❌ Gemini error: {e}", []

def lookup_plan_details(plan_name: str) -> str:
    # Normalize input
    plan_name_clean = plan_name.lower().strip()

    # Try to find closest match using contains
    matches = policy_df[policy_df["PlanMarketingName"].str.lower().str.contains(plan_name_clean)]

    if matches.empty:
        return "❌ Sorry, I couldn't find that plan in the dataset."

    # Just use the first match
    row = matches.iloc[0]
    fields = {
        "Metal Level": row.get("MetalLevel", "N/A"),
        "Plan Type": row.get("PlanType", "N/A"),
        "Wellness Program": row.get("WellnessProgramOffered", "N/A"),
        "Disease Management": row.get("DiseaseManagementProgramsOffered", "N/A"),
        "Maternity Support": row.get("IsNoticeRequiredForPregnancy", "N/A"),
        "Dental Only": row.get("DentalOnlyPlan", "N/A"),
        "Out of Network Coverage": row.get("OutOfServiceAreaCoverage", "N/A"),
        "Effective Date": row.get("PlanEffictiveDate", "N/A"),
        "Expiration Date": row.get("PlanExpirationDate", "N/A"),
        "Summary URL": row.get("URLForSummaryofBenefitsCoverage", "N/A")
    }

    details = "\n".join([f"- **{k}**: {v}" for k, v in fields.items()])
    return f"### 📄 Plan Details: {row['PlanMarketingName']}\n\n{details}"
