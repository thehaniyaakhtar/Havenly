import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plan Details", layout="centered")
st.title("Plan Details")

# Load dataset
df = pd.read_csv("filtered_plan2.csv")

# Get unique plan names
plan_names = sorted(df["PlanMarketingName"].dropna().unique())

# Let user select a plan
selected = st.selectbox("Select a plan to explore", plan_names)

# Get selected plan details
plan = df[df["PlanMarketingName"] == selected].iloc[0]

st.markdown("### Plan Overview")


st.markdown(f"""
- **Metal Level**: {plan.get('MetalLevel', 'N/A')}
- **Plan Type**: {plan.get('PlanType', 'N/A')}
- **Wellness Program**: {plan.get('WellnessProgramOffered', 'N/A')}
- **Disease Management**: {plan.get('DiseaseManagementProgramsOffered', 'N/A')}
- **Maternity Support**: {plan.get('IsNoticeRequiredForPregnancy', 'N/A')}
- **Dental Coverage**: {plan.get('DentalOnlyPlan', 'N/A')}
- **Specialist Referral Needed**: {plan.get('SpecialistRequiringReferral', 'N/A')}
- **Out-of-Network Coverage**: {plan.get('OutOfServiceAreaCoverage', 'N/A')}
- **Out-of-Country Coverage**: {plan.get('OutOfCountryCoverage', 'N/A')}
- **HSA Contribution from Employer**: {plan.get('HSAOrHRAEmployerContribution', 'N/A')}
- **Child-Only Plan**: {plan.get('ChildOnlyOffering', 'N/A')}
""")
