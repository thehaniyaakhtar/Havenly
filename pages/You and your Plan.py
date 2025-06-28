import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from utils import get_gemini_response, lookup_plan_details

load_dotenv()

st.set_page_config(page_title="PoliGen - AI Insurance Advisor", layout="centered")
st.title("🛡️ Havenly")
st.subheader("Your Personalized GenAI Insurance Advisor")

# --- Cached plan loader ---
@st.cache_data
def load_policy_data():
    return pd.read_csv("filtered_plan2.csv")

policy_df = load_policy_data()
st.success(f"✅ {len(policy_df)} insurance plans loaded.")

# --- Session state init ---
for key in ["messages", "last_user_input", "last_followup_prompt", "shown_plans"]:
    if key not in st.session_state:
        st.session_state[key] = [] if key == "messages" else set() if key == "shown_plans" else ""

# --- Render previous messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
if prompt := st.chat_input("Tell me about your insurance needs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Recognize request for more details ---
    detail_phrases = [
        "can you elaborate on", "tell me more about", "more info on",
        "details of", "i want more info on"
    ]
    match_phrase = next((p for p in detail_phrases if prompt.lower().startswith(p)), None)

    if match_phrase:
        plan_name = prompt.lower().replace(match_phrase, "").strip(" ?")
        response = lookup_plan_details(plan_name)
        new_plan_names = []
    else:
        followup_keywords = [
            "yes", "show", "sure", "go ahead", "please do",
            "ok", "what if", "change", "switch", "increase"
        ]
        is_followup = any(word in prompt.lower() for word in followup_keywords)

        if is_followup and st.session_state.last_followup_prompt:
            full_prompt = f"{st.session_state.last_user_input} FOLLOW-UP: {prompt}"
        else:
            full_prompt = prompt
            st.session_state.last_user_input = prompt

        response, new_plan_names = get_gemini_response(
            full_prompt,
            exclude_names=list(st.session_state.shown_plans)
        )

        for name in new_plan_names:
            st.session_state.shown_plans.add(name)

        st.session_state.last_followup_prompt = response

    # --- Display assistant message ---
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

        # --- Plan table if available ---
        if new_plan_names:
            df_compare = policy_df[policy_df["PlanMarketingName"].isin(new_plan_names)].copy()
            cols_to_show = [
                "PlanMarketingName", "MetalLevel", "PlanType",
                "WellnessProgramOffered", "DiseaseManagementProgramsOffered",
                "IsNoticeRequiredForPregnancy"
            ]
            df_compare = df_compare[cols_to_show].drop_duplicates()
            st.markdown("### 📊 Plan Comparison")
            st.dataframe(df_compare.reset_index(drop=True), use_container_width=True)
