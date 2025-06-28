import streamlit as st

st.set_page_config(page_title="Havenly - AI Insurance Advisor", layout="wide")

# Layout: left for text, right for image
col1, col2 = st.columns([1.5, 1.5])

with col1:
    st.markdown("## 🛡️Havenly")
    st.markdown("### Not just policies — a plan that fits right")
    st.markdown(
        """
        **Because whether you're starting out or starting over — we've got you.**
        """
    )
    st.markdown("### How we help you:")
    st.markdown(
        """
        - Explore plans that make sense for your life and your budget
        - Understand the differences without the fine-print headache
        - See what matters most — side-by-side comparisons, real examples
        - Get suggestions based on your stage of life, needs, and goals
        -Ask anything — even “what if my situation changes?”
        """
    )
    

with col2:
    st.image("img.jfif", use_container_width=True)


