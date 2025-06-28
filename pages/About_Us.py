# -*- coding: utf-8 -*-
import streamlit as st
import sys

try:
    st.set_page_config(page_title="About Havenly", layout="wide")

    # Custom CSS with earthy color scheme
    st.markdown("""
    <style>
        .about-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #8B4513;
            margin: 1rem 0;
        }
        .mission-card {
            background: linear-gradient(135deg, #8B4513 0%, #228B22 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
        }
        .team-card {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid #e9ecef;
            text-align: center;
            margin: 1rem 0;
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
    st.markdown("# 🛡️ About Havenly")
    st.markdown("### Your personal insurance companion, designed for real people with real needs")

    # Mission statement
    st.markdown("""
    <div class="mission-card">
        <h2>Our Mission</h2>
        <p style="font-size: 1.2rem; line-height: 1.6;">
            To make health insurance simple, transparent, and accessible for everyone. 
            We believe choosing coverage shouldn't be a guessing game — it should be 
            a confident decision that gives you peace of mind.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Main content
    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown("## 💡 Our Story")
        
        st.markdown("""
        <div class="about-card">
            <p style="font-size: 1.1rem; line-height: 1.7;">
                <strong>Havenly was born from frustration.</strong> We saw too many people struggling 
                with confusing insurance options, hidden costs, and overwhelming paperwork. 
                Whether you're raising a family, just starting out, working freelance, or 
                thinking about retirement — insurance decisions affect us all.
            </p>
            
            <p style="font-size: 1.1rem; line-height: 1.7;">
                You don't have to be an expert. You just have to know what you care about — 
                and we'll help you find the right fit. Our AI-powered platform analyzes 
                thousands of plans to match you with options that actually work for your life.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("## 🎯 Who We Serve")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("""
            <div class="team-card">
                <h4>👨‍👩‍👧‍👦 Families</h4>
                <p>Parents choosing security for their families with comprehensive coverage options.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="team-card">
                <h4>🎓 Students & Young Professionals</h4>
                <p>First-time insurance buyers figuring out coverage for the first time.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            st.markdown("""
            <div class="team-card">
                <h4>💼 Freelancers & Gig Workers</h4>
                <p>Independent workers needing flexible plans that adapt to changing income.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="team-card">
                <h4>🔄 Life Transitions</h4>
                <p>Anyone starting over, settling down, or looking ahead to retirement.</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("## 📊 Our Impact")
        
        metrics = [
            {"label": "Plans Analyzed", "value": "50,000+", "icon": "📋"},
            {"label": "Happy Customers", "value": "25,000+", "icon": "😊"},
            {"label": "Total Savings", "value": "₹15M+", "icon": "💰"},
            {"label": "Average Rating", "value": "4.8/5", "icon": "⭐"}
        ]
        
        for metric in metrics:
            st.markdown(f"""
            <div class="about-card">
                <div style="text-align: center;">
                    <h2 style="color: #8B4513; margin-bottom: 0.5rem;">{metric['icon']}</h2>
                    <h3 style="color: #8B4513; margin-bottom: 0.5rem;">{metric['value']}</h3>
                    <p style="color: #666; margin: 0;">{metric['label']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Values section
    st.markdown("## 🌟 Our Values")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="about-card">
            <h3 style="color: #8B4513;">🤝 Transparency</h3>
            <p>No hidden fees, no confusing jargon. We believe in clear, honest communication about what you're getting and what it costs.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="about-card">
            <h3 style="color: #8B4513;">🎯 Personalization</h3>
            <p>Your insurance should fit your life, not the other way around. We use AI to find plans that match your unique needs and budget.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="about-card">
            <h3 style="color: #8B4513;">❤️ Care</h3>
            <p>We genuinely care about your health and financial well-being. Every recommendation is made with your best interests in mind.</p>
        </div>
        """, unsafe_allow_html=True)

    # Technology section
    st.markdown("## 🔬 Our Technology")

    st.markdown("""
    <div class="about-card">
        <h3 style="color: #8B4513;">AI-Powered Matching</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Our advanced artificial intelligence analyzes thousands of insurance plans in real-time, 
            considering factors like your age, location, health needs, and budget to find the 
            perfect match. We continuously learn from user interactions to improve our recommendations.
        </p>
        <h3 style="color: #8B4513;">Data Security</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Your privacy is paramount. We use enterprise-grade security to protect your personal 
            information and never share your data without your explicit consent.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Team section
    st.markdown("## 👥 Meet Our Team")

    st.markdown("""
    <div class="about-card">
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Havenly was founded by a team of insurance experts, data scientists, and healthcare 
            professionals who believe that everyone deserves access to quality, affordable health 
            coverage. Our diverse backgrounds give us unique insights into the challenges people 
            face when choosing insurance.
        </p>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            We're committed to continuous improvement and innovation, always looking for ways to 
            make the insurance selection process easier and more transparent for our users.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Contact section
    st.markdown("## 📞 Get in Touch")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="team-card">
            <h4>📧 Email</h4>
            <p>hello@havenly.com</p>
            <p>support@havenly.com</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="team-card">
            <h4>📞 Phone</h4>
            <p>1-800-HAVENLY</p>
            <p>Mon-Fri 9AM-6PM</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="team-card">
            <h4>🌐 Social</h4>
            <p>@havenly_insurance</p>
            <p>LinkedIn: Havenly</p>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>© 2024 Havenly. All rights reserved. | Privacy Policy | Terms of Service</p>
        <p>Making insurance simple, one plan at a time.</p>
    </div>
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"An error occurred while loading the About Us page: {str(e)}")
    st.info("Please try refreshing the page or contact support if the issue persists.")
    st.exception(e)
