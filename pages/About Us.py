import streamlit as st

st.set_page_config(page_title="About Havenly", layout="wide")

# Layout: Left text, right image
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("## About Havenly")
    st.markdown("""
    **Havenly is your personal insurance companion.**  
    It's designed to help you navigate health insurance without the confusion or overwhelm. Whether you're raising a family, just starting out, working freelance, or thinking about retirement — Havenly is built with you in mind.

    You don’t have to be an expert. You just have to know what you care about — and we’ll help you find the right fit.

    ---  
    ### Why we built this

    Because choosing insurance shouldn't be a guessing game.  
    Havenly makes it feel less like paperwork — and more like peace of mind.

    ---  
    ### Who is Havenly for?

    - Parents choosing security for their families  
    - Students and young professionals figuring it out for the first time  
    - Freelancers and gig workers needing flexible plans  
    - Anyone starting over, settling down, or looking ahead
    """)

with col2:
    st.image("imgg.jfif", use_container_width=True)
