import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Find Your Best Plan", layout="centered")
st.title("Find the Best Plan for You")

# Load datasets
plan_df = pd.read_csv("filtered_plan2.csv")
service_df = pd.read_csv("filtered_service_area.csv")
rate_df = pd.read_csv("filtered_rate2.csv")

# Debug: Check required columns
if "AvgIndividualRate" not in rate_df.columns or "PlanId" not in rate_df.columns:
    st.error("⚠️ The rate dataset must include 'PlanId' and 'AvgIndividualRate'.")
    st.stop()

# ----- User Form -----
with st.form("plan_form"):
    st.subheader("Tell us about yourself:")

    age_group = st.selectbox("Age Group", ["18-25", "26-35", "36-45", "46-60", "61+"])
    tobacco = st.radio("Do you use tobacco?", ["No", "Yes", "Prefer not to say"])
    plan_type = st.selectbox("Type of Insurance", ["Individual", "Family", "Child-only"])
    state = st.selectbox("State (optional)", ["Any"] + sorted(service_df["StateCode"].dropna().unique()))

    needs = st.multiselect(
        "Coverage Preferences (optional)",
        ["Wellness", "Maternity", "Mental Health", "Dental"]
    )

    submit = st.form_submit_button("Show Matching Plans")

# ----- Filtering -----
if submit:
    st.markdown("## Top Matching Plans")

    filtered = plan_df.copy()

    # Optional state filter
    if state != "Any":
        valid_services = service_df[
            (service_df["StateCode"] == state)
            & (service_df["CoverEntireState"].astype(str).str.lower() == "true")
        ]["ServiceAreaId"].unique()
        filtered = filtered[filtered["ServiceAreaId"].isin(valid_services)]

    # Required: Plan type
    if plan_type == "Child-only":
        filtered = filtered[filtered["ChildOnlyOffering"].astype(str).str.lower() == "true"]
    elif plan_type == "Family":
        filtered = filtered[filtered["MarketCoverage"].str.contains("Family", na=False)]
    else:
        filtered = filtered[filtered["MarketCoverage"].str.contains("Individual", na=False)]

    # Merge with pre-aggregated rate info
    if state != "Any":
        rate_filtered = rate_df[rate_df["StateCode"] == state]
    else:
        rate_filtered = rate_df.copy()

    filtered = pd.merge(filtered, rate_filtered[["PlanId", "AvgIndividualRate"]], on="PlanId", how="left")

    # Score based on user-selected needs
    score_map = {
        "Wellness": "WellnessProgramOffered",
        "Maternity": "IsNoticeRequiredForPregnancy",
        "Mental Health": "DiseaseManagementProgramsOffered",
        "Dental": "DentalOnlyPlan"
    }

    def calculate_score(row):
        score = 0
        for need in needs:
            col = score_map.get(need)
            if col and col in row and str(row[col]).lower() in ["yes", "true", "1"]:
                score += 1
        return score

    filtered["MatchScore"] = filtered.apply(calculate_score, axis=1)

    # Sort and show top plans
    top = filtered.sort_values(by=["MatchScore", "AvgIndividualRate"], ascending=[False, True])
    top = top.drop_duplicates(subset=["PlanMarketingName"]).head(5)

    if top.empty:
        st.warning("❌ No plans match your input. Try fewer filters.")
    else:
        for _, row in top.iterrows():
            st.markdown(f"### {row['PlanMarketingName']}")
            st.write(f"- Metal Level: {row.get('MetalLevel', 'N/A')}")
            st.write(f"- Plan Type: {row.get('PlanType', 'N/A')}")
            st.write(f"- Estimated Cost: ₹{int(row['AvgIndividualRate']) if pd.notna(row['AvgIndividualRate']) else 'N/A'} / month")
            st.write(f"- Wellness: {row.get('WellnessProgramOffered', 'N/A')}")
            st.write(f"- Maternity: {row.get('IsNoticeRequiredForPregnancy', 'N/A')}")
            st.write(f"- Mental Health: {row.get('DiseaseManagementProgramsOffered', 'N/A')}")
            st.divider()

        st.session_state["matched_plans"] = top["PlanMarketingName"].tolist()
        if st.button("💬 Chat about these plans"):
            st.switch_page("Chat.py")
