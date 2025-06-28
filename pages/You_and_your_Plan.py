import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from utils import get_gemini_response, lookup_plan_details, load_trimmed_data, create_sample_data
import os

load_dotenv()

st.set_page_config(page_title="AI Insurance Advisor", layout="wide")

# Custom CSS with earthy color scheme
st.markdown("""
<style>
    .chat-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #e9ecef;
        margin: 1rem 0;
    }
    .plan-comparison {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #8B4513;
        margin: 1rem 0;
    }
    .metric-highlight {
        color: #8B4513;
        font-weight: bold;
    }
    .success-text {
        color: #228B22;
    }
    .stChatMessage {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #8B4513;
    }
    .stChatInput {
        border-radius: 25px;
        border: 2px solid #8B4513;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 💬 AI Insurance Advisor")
st.markdown("### Chat with our AI to get personalized insurance recommendations")

# Load trimmed policy data
def load_policy_data():
    try:
        # Use trimmed datasets for deployment
        plans_df, rates_df, benefits_df, service_areas_df = load_trimmed_data()
        
        # If any file failed to load, use sample data
        if plans_df is None:
            st.info("ℹ️ Some data files could not be loaded. Using sample data.")
            plans_df, rates_df, benefits_df, service_areas_df = create_sample_data()
        
        st.success(f"✅ Loaded trimmed data: {len(plans_df):,} insurance plans")
        return plans_df
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Using sample data instead.")
        plans_df, rates_df, benefits_df, service_areas_df = create_sample_data()
        return plans_df

policy_df = load_policy_data()

# Initialize session state
for key in ["messages", "last_user_input", "last_followup_prompt", "shown_plans"]:
    if key not in st.session_state:
        st.session_state[key] = [] if key == "messages" else set() if key == "shown_plans" else ""

# Two-column layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🤖 Chat Interface")
    
    # Display previous messages
    if st.session_state.messages:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    else:
        st.markdown("### 👋 Welcome! I'm your AI insurance advisor.")
        st.markdown("I can help you with:")
        st.markdown("- 🔍 Finding plans that match your needs and budget")
        st.markdown("- 📊 Comparing different coverage options")
        st.markdown("- 📝 Explaining insurance terms and concepts")
        st.markdown("- 💰 Understanding costs, deductibles, and copays")
        st.markdown("- 🏥 Claims process and eligibility questions")
        st.markdown("- 🔄 Plan switching and enrollment guidance")
        st.markdown("- 📋 Coverage details and benefits")
        
        st.markdown("**Try asking:**")
        st.markdown("- \"I need a family plan with dental coverage\"")
        st.markdown("- \"What's the difference between HMO and PPO?\"")
        st.markdown("- \"How do I file a claim?\"")
        st.markdown("- \"When can I switch plans?\"")

    # Chat input
    if prompt := st.chat_input("Tell me about your insurance needs..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Process the input
        with st.spinner("🤔 Thinking..."):
            try:
                # Enhanced query recognition
                query_types = {
                    "plan_search": ["find", "search", "looking for", "need a plan", "recommend"],
                    "comparison": ["compare", "difference", "vs", "versus", "better"],
                    "claims": ["claim", "file", "submit", "reimbursement", "bill"],
                    "eligibility": ["eligible", "qualify", "enrollment", "when can i"],
                    "coverage": ["cover", "coverage", "benefits", "what's included"],
                    "switching": ["switch", "change", "enroll", "cancel", "terminate"],
                    "costs": ["cost", "price", "premium", "deductible", "copay", "out of pocket"],
                    "concepts": ["what is", "explain", "meaning", "definition", "how does"],
                    "details": ["more info", "details", "tell me more", "elaborate"]
                }
                
                prompt_lower = prompt.lower()
                detected_type = None
                for query_type, keywords in query_types.items():
                    if any(keyword in prompt_lower for keyword in keywords):
                        detected_type = query_type
                        break

                # Recognize request for more details
                detail_phrases = [
                    "can you elaborate on", "tell me more about", "more info on",
                    "details of", "i want more info on"
                ]
                match_phrase = next((p for p in detail_phrases if prompt_lower.startswith(p)), None)

                if match_phrase:
                    plan_name = prompt_lower.replace(match_phrase, "").strip(" ?")
                    response = lookup_plan_details(plan_name)
                    new_plan_names = []
                else:
                    followup_keywords = [
                        "yes", "show", "sure", "go ahead", "please do",
                        "ok", "what if", "change", "switch", "increase"
                    ]
                    is_followup = any(word in prompt_lower for word in followup_keywords)

                    if is_followup and st.session_state.last_followup_prompt:
                        full_prompt = f"{st.session_state.last_user_input} FOLLOW-UP: {prompt}"
                    else:
                        full_prompt = prompt
                        st.session_state.last_user_input = prompt

                    # Enhanced prompt with query type context
                    if detected_type:
                        enhanced_prompt = f"QUERY TYPE: {detected_type}. USER QUESTION: {full_prompt}"
                    else:
                        enhanced_prompt = full_prompt

                    response, new_plan_names = get_gemini_response(
                        enhanced_prompt,
                        exclude_names=list(st.session_state.shown_plans)
                    )

                    for name in new_plan_names:
                        st.session_state.shown_plans.add(name)

                    st.session_state.last_followup_prompt = response

            except Exception as e:
                st.error(f"❌ Error processing request: {str(e)}")
                response = f"""🔧 **Technical Issue**

I encountered an error while processing your request. This might be due to:

1. **API Configuration:** The Google Gemini API key might not be set up correctly
2. **Network Issues:** Please check your internet connection
3. **Service Temporarily Unavailable:** The AI service might be down

**What you can do:**
- Try asking a simpler question
- Refresh the page and try again
- Check the API configuration in the `.env` file
- Contact support if the issue persists

**For now, here's some helpful information:**

🔍 **Finding Insurance Plans:**
- Consider your monthly budget for premiums
- Think about your expected healthcare needs
- Check if your preferred doctors are in-network
- Compare deductibles and out-of-pocket maximums

Would you like me to help you understand any specific aspect of health insurance?"""
                new_plan_names = []

        # Display assistant message
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

            # Plan comparison table if available
            if new_plan_names:
                try:
                    df_compare = policy_df[policy_df["PlanMarketingName"].isin(new_plan_names)].copy()
                    
                    if not df_compare.empty:
                        cols_to_show = [
                            "PlanMarketingName", "MetalLevel", "PlanType",
                            "WellnessProgramOffered", "DiseaseManagementProgramsOffered"
                        ]
                        
                        # Filter columns that exist in the dataframe
                        available_cols = [col for col in cols_to_show if col in df_compare.columns]
                        
                        if available_cols:
                            st.markdown("### 📊 Plan Comparison")
                            st.dataframe(
                                df_compare[available_cols].reset_index(drop=True),
                                use_container_width=True
                            )
                except Exception as e:
                    st.warning(f"Could not display plan comparison: {e}")

with col2:
    st.markdown("### 📊 Quick Stats")
    
    # Display some quick statistics
    st.metric("Total Plans Available", f"{len(policy_df):,}")
    
    if 'MetalLevel' in policy_df.columns:
        metal_counts = policy_df['MetalLevel'].value_counts()
        st.markdown("**Plan Distribution:**")
        for metal, count in metal_counts.items():
            st.markdown(f"- {metal}: {count:,}")
    
    if 'PlanType' in policy_df.columns:
        plan_type_counts = policy_df['PlanType'].value_counts()
        st.markdown("**Plan Types:**")
        for plan_type, count in plan_type_counts.head(3).items():
            st.markdown(f"- {plan_type}: {count:,}")
    
    st.markdown("---")
    
    # Check if API is configured
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key or api_key == 'your_google_gemini_api_key_here':
        st.markdown("### ⚠️ API Setup Required")
        st.markdown("""
        The AI chat feature requires a Google Gemini API key.
        
        **To set up:**
        1. Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Edit the `.env` file in your project root
        3. Add: `GOOGLE_API_KEY=your_actual_key`
        4. Restart the app
        
        **Or run:** `python setup_env.py`
        """)
        st.info("💡 The chat will still work with helpful insurance information!")
    
    st.markdown("### 💡 Tips")
    st.markdown("- **Be specific** about your needs and budget")
    st.markdown("- **Ask follow-up questions** for more details")
    st.markdown("- **Compare plans** side by side")
    st.markdown("- **Consider your health** and family situation")
    
    st.markdown("---")
    
    st.markdown("### 🔄 Clear Chat")
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.shown_plans = set()
        st.session_state.last_user_input = ""
        st.session_state.last_followup_prompt = ""
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>💬 Need human assistance? Contact us at 1-800-HAVENLY</p>
    <p>🔒 Your conversations are private and secure</p>
</div>
""", unsafe_allow_html=True)
