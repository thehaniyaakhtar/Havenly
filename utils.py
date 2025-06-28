import google.generativeai as genai
import pandas as pd
import re
import os
import numpy as np
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Try different model names in case one is not available
def get_model():
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        return model
    except Exception as e:
        return None

model = get_model()

# Load trimmed plan data
try:
    policy_df = pd.read_csv("filtered_plan2.csv")
except FileNotFoundError:
    st.warning("filtered_plan2.csv not found. Using sample data.")
    policy_df = pd.DataFrame({
        'PlanId': range(1, 101),
        'PlanMarketingName': [f'Sample Plan {i}' for i in range(1, 101)],
        'MetalLevel': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], 100),
        'PlanType': np.random.choice(['HMO', 'PPO', 'EPO'], 100),
        'WellnessProgramOffered': np.random.choice(['Yes', 'No'], 100),
        'DiseaseManagementProgramsOffered': np.random.choice(['Yes', 'No'], 100),
        'IsNoticeRequiredForPregnancy': np.random.choice(['Yes', 'No'], 100),
        'ChildOnlyOffering': np.random.choice(['Yes', 'No'], 100)
    })

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

def load_data_memory_efficient(file_path, sample_size=10000):
    """
    Load data with memory optimization for large files
    """
    try:
        if not os.path.exists(file_path):
            return None
            
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
        
        if file_size > 100:  # If file is larger than 100MB
            st.info(f"Large file detected ({file_size:.1f}MB). Loading sample for better performance.")
            return pd.read_csv(file_path, nrows=sample_size)
        else:
            return pd.read_csv(file_path)
            
    except Exception as e:
        st.error(f"Error loading {file_path}: {e}")
        return None

def load_trimmed_data():
    """
    Load trimmed datasets for deployment
    """
    try:
        # Load trimmed datasets
        plans_df = pd.read_csv("filtered_plan2.csv")
        rates_df = pd.read_csv("filtered_rate2.csv")
        benefits_df = pd.read_csv("filtered_benefits2.csv")
        service_areas_df = pd.read_csv("filtered_service_area.csv")
        
        st.success(f"✅ Loaded trimmed data: {len(plans_df):,} plans, {len(rates_df):,} rates, {len(benefits_df):,} benefits")
        return plans_df, rates_df, benefits_df, service_areas_df
        
    except Exception as e:
        st.error(f"Error loading trimmed data: {e}")
        st.info("Using sample data instead.")
        return create_sample_data()

def get_gemini_response(prompt, exclude_names=None):
    """
    Get response from Google Gemini AI
    """
    try:
        # Check if API key is configured
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key or api_key == 'your_google_gemini_api_key_here':
            return "API Configuration Required: Please set up your Google Gemini API key in the .env file. Visit https://makersuite.google.com/app/apikey to get an API key.", []
        
        # Check if model is available
        if model is None:
            return "Model Configuration Error: Unable to connect to Google Gemini AI service. Please check your API key and try again.", []
        
        # Add context about insurance plans
        context = "You are an AI insurance advisor for Havenly. You help users find the best health insurance plans. Be helpful, informative, and suggest relevant plans when appropriate. Keep responses concise but informative."
        
        full_prompt = f"{context}\n\nUser: {prompt}"
        
        response = model.generate_content(full_prompt)
        
        # Extract plan names if mentioned
        plan_names = []
        if "plan" in prompt.lower() or "coverage" in prompt.lower():
            plan_names = ["Sample Plan A", "Sample Plan B", "Sample Plan C"]
        
        return response.text, plan_names
        
    except Exception as e:
        return f"API Error: {str(e)}. Please check your API key and try again.", []

def lookup_plan_details(plan_name):
    """
    Look up details for a specific plan
    """
    try:
        # In a real application, this would query a database
        # For now, return sample information
        return f"""
        **Plan Details for {plan_name}**
        
        **Coverage Level:** Silver
        **Monthly Premium:** ₹450
        **Deductible:** ₹2,500
        **Out-of-Pocket Maximum:** ₹7,000
        
        **Key Benefits:**
        - Primary care visits: ₹25 copay
        - Specialist visits: ₹40 copay
        - Emergency room: ₹200 copay
        - Prescription drugs: Tiered copays
        
        **Network:** PPO
        **Wellness Programs:** Yes
        **Mental Health Coverage:** Yes
        
        This plan offers a good balance of coverage and cost for most individuals and families.
        """
    except Exception as e:
        return f"Sorry, I couldn't find details for {plan_name}. Error: {e}"

def create_sample_data():
    """
    Create sample data for demonstration when real data is not available
    """
    np.random.seed(42)
    
    # Sample plans
    plans_df = pd.DataFrame({
        'PlanId': range(1, 1001),
        'PlanMarketingName': [f'Sample Plan {i}' for i in range(1, 1001)],
        'MetalLevel': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'], 1000),
        'PlanType': np.random.choice(['HMO', 'PPO', 'EPO'], 1000),
        'WellnessProgramOffered': np.random.choice(['Yes', 'No'], 1000),
        'DiseaseManagementProgramsOffered': np.random.choice(['Yes', 'No'], 1000),
        'IsNoticeRequiredForPregnancy': np.random.choice(['Yes', 'No'], 1000),
        'ChildOnlyOffering': np.random.choice(['Yes', 'No'], 1000),
        'MarketCoverage': np.random.choice(['Individual', 'Family', 'Child-only'], 1000)
    })
    
    # Sample rates
    rates_df = pd.DataFrame({
        'PlanId': np.random.choice(range(1, 1001), 5000),
        'Age': np.random.randint(18, 65, 5000),
        'IndividualRate': np.random.uniform(200, 800, 5000),
        'StateCode': np.random.choice(['CA', 'NY', 'TX', 'FL', 'IL'], 5000),
        'Tobacco': np.random.choice(['Yes', 'No'], 5000)
    })
    
    # Sample benefits
    benefits_df = pd.DataFrame({
        'PlanId': np.random.choice(range(1, 1001), 3000),
        'BenefitName': np.random.choice(['Primary Care', 'Specialist', 'Emergency', 'Prescription', 'Dental', 'Vision'], 3000),
        'Copay': np.random.uniform(10, 50, 3000),
        'Deductible': np.random.uniform(500, 5000, 3000)
    })
    
    # Sample service areas
    service_areas_df = pd.DataFrame({
        'StateCode': np.random.choice(['CA', 'NY', 'TX', 'FL', 'IL'], 1000),
        'ServiceAreaId': [f"{state}S001" for state in np.random.choice(['CA', 'NY', 'TX', 'FL', 'IL'], 1000)],
        'CoverEntireState': np.random.choice(['Yes', 'No'], 1000),
        'County': np.random.randint(10000, 99999, 1000),
        'ZipCodes': [f"{np.random.randint(10000, 99999)}" for _ in range(1000)]
    })
    
    return plans_df, rates_df, benefits_df, service_areas_df
