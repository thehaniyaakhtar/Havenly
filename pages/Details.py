import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plan Details", layout="centered")

# Custom earthy CSS
st.markdown("""
<style>
    .plan-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #8B4513;
        margin: 2rem 0 1rem 0;
    }
    .plan-header {
        color: #228B22;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .plan-attr {
        color: #8B4513;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("# 📝 Plan Details")

# Load dataset
df = pd.read_csv("filtered_plan2.csv")

# Get unique plan names
plan_names = sorted(df["PlanMarketingName"].dropna().unique())

# Let user select a plan
selected = st.selectbox("Select a plan to explore", plan_names)

# Get selected plan details
plan = df[df["PlanMarketingName"] == selected].iloc[0]

st.markdown(f"""
<div class="plan-card">
    <div class="plan-header">{plan.get('PlanMarketingName', 'N/A')}</div>
    <ul style='font-size:1.1rem;line-height:1.7;'>
        <li><span class="plan-attr">Metal Level:</span> {plan.get('MetalLevel', 'N/A')}</li>
        <li><span class="plan-attr">Plan Type:</span> {plan.get('PlanType', 'N/A')}</li>
        <li><span class="plan-attr">Wellness Program:</span> {plan.get('WellnessProgramOffered', 'N/A')}</li>
        <li><span class="plan-attr">Disease Management:</span> {plan.get('DiseaseManagementProgramsOffered', 'N/A')}</li>
        <li><span class="plan-attr">Maternity Support:</span> {plan.get('IsNoticeRequiredForPregnancy', 'N/A')}</li>
        <li><span class="plan-attr">Dental Coverage:</span> {plan.get('DentalOnlyPlan', 'N/A')}</li>
        <li><span class="plan-attr">Specialist Referral Needed:</span> {plan.get('SpecialistRequiringReferral', 'N/A')}</li>
        <li><span class="plan-attr">Out-of-Network Coverage:</span> {plan.get('OutOfServiceAreaCoverage', 'N/A')}</li>
        <li><span class="plan-attr">Out-of-Country Coverage:</span> {plan.get('OutOfCountryCoverage', 'N/A')}</li>
        <li><span class="plan-attr">HSA Contribution from Employer:</span> {plan.get('HSAOrHRAEmployerContribution', 'N/A')}</li>
        <li><span class="plan-attr">Child-Only Plan:</span> {plan.get('ChildOnlyOffering', 'N/A')}</li>
    </ul>
</div>
""", unsafe_allow_html=True)
