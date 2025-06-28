import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Find Your Best Plan", layout="centered")
st.title("Find the Best Plan for You")

# Load datasets
plan_df = pd.read_csv("filtered_plan2.csv")
service_df = pd.read_csv("filtered_service_area.csv")
rate_df = pd.read_csv("filtered_rate2.csv")

# ----- User Form -----
with st.form("plan_form"):
    st.subheader("Tell us about yourself:")

    age_group = st.selectbox("Age Group", ["18-25", "26-35", "36-45", "46-60", "61+"])
    age_ranges = {
        "18-25": list(range(18, 26)),
        "26-35": list(range(26, 36)),
        "36-45": list(range(36, 46)),
        "46-60": list(range(46, 61)),
        "61+": list(range(61, 65)),
    }
    selected_ages = age_ranges[age_group]

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

    # Optional state filter (only if selected)
    if state != "Any":
        valid_services = service_df[
            (service_df["StateCode"] == state)
            & (service_df["CoverEntireState"].astype(str).str.lower() == "true")
        ]["ServiceAreaId"].unique()
        filtered = filtered[filtered["ServiceAreaId"].isin(valid_services)]

    # Plan type is mandatory
    if plan_type == "Child-only":
        filtered = filtered[filtered["ChildOnlyOffering"].astype(str).str.lower() == "true"]
    elif plan_type == "Family":
        filtered = filtered[filtered["MarketCoverage"].str.contains("Family", na=False)]
    else:
        filtered = filtered[filtered["MarketCoverage"].str.contains("Individual", na=False)]

    # Merge with rate data based on age group
    rate_filtered = rate_df[
        rate_df["Age"].isin(selected_ages)
    ].copy()

    if state != "Any":
        rate_filtered = rate_filtered[rate_filtered["StateCode"] == state]

    if tobacco != "Prefer not to say":
        rate_filtered = rate_filtered[rate_filtered["Tobacco"].str.lower() == tobacco.lower()]
    else:
        rate_filtered = rate_filtered[rate_filtered["Tobacco"].str.lower() == "no"]

    rate_avg = rate_filtered.groupby("PlanId")["IndividualRate"].mean().reset_index()

    filtered = pd.merge(filtered, rate_avg, on="PlanId", how="left")

    # Scoring based on needs
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

    # Sort by score then price
    ranked = filtered.sort_values(by=["MatchScore", "IndividualRate"], ascending=[False, True])
    top = ranked.drop_duplicates(subset=["PlanMarketingName"]).head(5)

    if top.empty:
        st.warning("❌ No plans match your input. Try fewer filters.")
    else:
        for _, row in top.iterrows():
            st.markdown(f"### {row['PlanMarketingName']}")
            st.write(f"- Metal Level: {row.get('MetalLevel', 'N/A')}")
            st.write(f"- Plan Type: {row.get('PlanType', 'N/A')}")
            st.write(f"- Estimated Cost: ₹{int(row['IndividualRate']) if pd.notna(row['IndividualRate']) else 'N/A'} / month")
            st.write(f"- Wellness: {row.get('WellnessProgramOffered', 'N/A')}")
            st.write(f"- Maternity: {row.get('IsNoticeRequiredForPregnancy', 'N/A')}")
            st.write(f"- Mental Health: {row.get('DiseaseManagementProgramsOffered', 'N/A')}")
            st.divider()

        st.session_state["matched_plans"] = top["PlanMarketingName"].tolist()
        if st.button("💬 Chat about these plans"):
            st.switch_page("pages/Chat.py")
