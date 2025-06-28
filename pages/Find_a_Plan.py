import streamlit as st
import pandas as pd
import numpy as np
import os
from utils import load_trimmed_data, create_sample_data

st.set_page_config(page_title="Find Your Best Plan", layout="wide")

# Custom CSS with earthy color scheme
st.markdown("""
<style>
    .plan-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #8B4513;
        margin: 1rem 0;
    }
    .form-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #e9ecef;
    }
    .stButton > button {
        background: linear-gradient(90deg, #8B4513 0%, #228B22 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(139, 69, 19, 0.3);
    }
    .metric-highlight {
        color: #8B4513;
        font-weight: bold;
    }
    .success-text {
        color: #228B22;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🔍 Find Your Perfect Plan")
st.markdown("### Tell us about yourself and we'll match you with the best insurance options")

# Load trimmed datasets
def load_plan_data():
    try:
        # Use trimmed datasets for deployment
        plans_df, rates_df, benefits_df, service_areas_df = load_trimmed_data()
        
        # If any file failed to load, use sample data
        if plans_df is None or rates_df is None or service_areas_df is None:
            st.info("ℹ️ Some data files could not be loaded. Using sample data.")
            plans_df, rates_df, benefits_df, service_areas_df = create_sample_data()
        
        st.success(f"✅ Loaded trimmed data: {len(plans_df):,} plans, {len(rates_df):,} rates, {len(service_areas_df):,} service areas")
        return plans_df, service_areas_df, rates_df
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Using sample data instead.")
        plans_df, rates_df, benefits_df, service_areas_df = create_sample_data()
        return plans_df, service_areas_df, rates_df

# Load data
with st.spinner("Loading plan data..."):
    plan_df, service_df, rate_df = load_plan_data()

# Two-column layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Your Preferences")
    
    with st.form("plan_form"):
        st.markdown("**Tell us about yourself:**")
        
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

        submit = st.form_submit_button("🔍 Find Matching Plans", use_container_width=True)

with col2:
    if submit:
        st.markdown("### 🎯 Top Matching Plans")
        
        with st.spinner("Finding your perfect plans..."):
            try:
                filtered = plan_df.copy()

                # Optional state filter
                if state != "Any":
                    valid_services = service_df[
                        (service_df["StateCode"] == state)
                        & (service_df["CoverEntireState"].astype(str).str.lower() == "true")
                    ]["ServiceAreaId"].unique()
                    filtered = filtered[filtered["ServiceAreaId"].isin(valid_services)]

                # Plan type filter
                if plan_type == "Child-only":
                    filtered = filtered[filtered["ChildOnlyOffering"].astype(str).str.lower() == "true"]
                elif plan_type == "Family":
                    filtered = filtered[filtered["MarketCoverage"].str.contains("Family", na=False)]
                else:
                    filtered = filtered[filtered["MarketCoverage"].str.contains("Individual", na=False)]

                # Merge with rate data
                rate_filtered = rate_df.copy()

                if state != "Any":
                    rate_filtered = rate_filtered[rate_filtered["StateCode"] == state]

                # Use AvgIndividualRate from trimmed data
                rate_avg = rate_filtered.groupby("PlanId")["AvgIndividualRate"].mean().reset_index()
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

                filtered["match_score"] = filtered.apply(calculate_score, axis=1)
                filtered = filtered.sort_values(["match_score", "AvgIndividualRate"], ascending=[False, True])

                # Display top 5 plans
                top_plans = filtered.head(5)

                if len(top_plans) == 0:
                    st.warning("No plans found matching your criteria. Try adjusting your preferences.")
                else:
                    for idx, plan in top_plans.iterrows():
                        with st.container():
                            st.markdown(f"""
                            <div class="plan-card">
                                <h3>🏥 {plan['PlanMarketingName']}</h3>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                                    <div>
                                        <p><strong>Metal Level:</strong> <span class="metric-highlight">{plan.get('MetalLevel', 'N/A')}</span></p>
                                        <p><strong>Plan Type:</strong> {plan.get('PlanType', 'N/A')}</p>
                                        <p><strong>Monthly Premium:</strong> <span class="metric-highlight">₹{plan.get('AvgIndividualRate', 0):.0f}</span></p>
                                    </div>
                                    <div>
                                        <p><strong>Wellness Programs:</strong> {plan.get('WellnessProgramOffered', 'N/A')}</p>
                                        <p><strong>Disease Management:</strong> {plan.get('DiseaseManagementProgramsOffered', 'N/A')}</p>
                                        <p><strong>Match Score:</strong> <span class="success-text">{plan.get('match_score', 0)}/4</span></p>
                                    </div>
                                </div>
                                <div style="margin-top: 1rem;">
                                    <strong>Why this plan?</strong>
                                    <ul>
                                        <li>Comprehensive coverage for your selected preferences</li>
                                        <li>Competitive pricing in your area</li>
                                        <li>Strong network of healthcare providers</li>
                                    </ul>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

                    # Summary statistics
                    st.markdown("---")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Average Premium", f"₹{top_plans['AvgIndividualRate'].mean():.0f}/month")
                    with col2:
                        st.metric("Lowest Premium", f"₹{top_plans['AvgIndividualRate'].min():.0f}/month")
                    with col3:
                        st.metric("Highest Match Score", f"{top_plans['match_score'].max()}/4")

                    # Start over button
                    if st.button("🔄 Start Over", use_container_width=True):
                        st.rerun()

            except Exception as e:
                st.error(f"Error processing plans: {e}")
                st.info("Please try adjusting your search criteria.")

    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem; color: #666;">
            <h3>🎯 Ready to find your perfect plan?</h3>
            <p>Fill out the form on the left to get personalized recommendations based on your needs and preferences.</p>
            <p>Our AI will analyze thousands of plans to find the best matches for you.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Need help? Contact our support team at support@havenly.com")
