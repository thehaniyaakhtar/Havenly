import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import os
from utils import load_trimmed_data, create_sample_data

# Page configuration
st.set_page_config(
    page_title="Havenly - AI Insurance Advisor", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with earthy color scheme
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #8B4513 0%, #228B22 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #8B4513;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
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
    .text-gradient {
        background: linear-gradient(90deg, #8B4513 0%, #228B22 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# Load trimmed data
def load_data():
    try:
        # Use trimmed datasets for deployment
        plans_df, rates_df, benefits_df, service_areas_df = load_trimmed_data()
        
        # If any file failed to load, use sample data
        if plans_df is None or rates_df is None or benefits_df is None:
            st.info("ℹ️ Some data files could not be loaded. Using sample data.")
            plans_df, rates_df, benefits_df, service_areas_df = create_sample_data()
        
        return plans_df, rates_df, benefits_df
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Using sample data instead.")
        plans_df, rates_df, benefits_df, service_areas_df = create_sample_data()
        return plans_df, rates_df, benefits_df

# Load data with progress indicator
with st.spinner("Loading insurance data..."):
    plans_df, rates_df, benefits_df = load_data()

# Sidebar
with st.sidebar:
    st.markdown("## 🛡️ Havenly")
    st.markdown("### AI Insurance Advisor")
    
    st.markdown("---")
    
    st.markdown("### Quick Actions")
    if st.button("🔍 Find Plans", use_container_width=True):
        st.switch_page("pages/Find_a_Plan.py")
    
    if st.button("📊 View Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")
    
    if st.button("💬 Chat with AI", use_container_width=True):
        st.switch_page("pages/You_and_your_Plan.py")
    
    st.markdown("---")
    
    st.markdown("### Market Insights")
    st.metric("Total Plans", f"{len(plans_df):,}")
    st.metric("Avg Premium", f"₹{rates_df['AvgIndividualRate'].mean():.0f}/month")
    st.metric("Coverage Score", "92%")
    
    st.markdown("---")
    
    st.markdown("### Contact")
    st.markdown("📞 1-800-HAVENLY")
    st.markdown("📧 hello@havenly.com")
    st.markdown("🌐 havenly.com")

# Main content
st.markdown('<h1 class="main-header">🛡️ Havenly</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: #666; margin-bottom: 3rem;">Not just policies — a plan that fits right</h2>', unsafe_allow_html=True)

# Hero section with metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📈 Plans Available</h3>
        <h2 style="color: #8B4513;">{len(plans_df):,}</h2>
        <p style="color: #228B22;">↗️ +12% this month</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>👥 Happy Customers</h3>
        <h2 style="color: #8B4513;">50,000+</h2>
        <p style="color: #228B22;">↗️ +8% this month</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>💰 Total Savings</h3>
        <h2 style="color: #8B4513;">₹2.5M+</h2>
        <p style="color: #228B22;">↗️ +15% this month</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>⭐ Satisfaction</h3>
        <h2 style="color: #8B4513;">98%</h2>
        <p style="color: #228B22;">↗️ +2% this month</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Features section
st.markdown("## 🚀 How we help you")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🔍 AI-Powered Matching</h3>
        <p>Our advanced AI analyzes your needs and finds the perfect plan match from thousands of options.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>💰 Smart Cost Analysis</h3>
        <p>Compare premiums, deductibles, and out-of-pocket costs side by side with our intelligent comparison tools.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>❤️ Health-First Approach</h3>
        <p>Plans that prioritize your health with wellness programs, preventive care, and comprehensive coverage.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>👨‍👩‍👧‍👦 Family Coverage</h3>
        <p>Comprehensive family plans that grow with your changing needs and provide peace of mind.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Simple market overview (not dashboard-like)
st.markdown("## 📊 Market Overview")

col1, col2 = st.columns(2)

with col1:
    # Plan distribution pie chart
    metal_counts = plans_df['MetalLevel'].value_counts()
    fig_distribution = px.pie(
        values=metal_counts.values, 
        names=metal_counts.index,
        title="Plan Distribution by Metal Level",
        color_discrete_map={
            'Bronze': '#8B4513',
            'Silver': '#A0522D', 
            'Gold': '#DAA520',
            'Platinum': '#B8860B'
        }
    )
    fig_distribution.update_layout(height=400)
    st.plotly_chart(fig_distribution, use_container_width=True)

with col2:
    # Simple premium overview - Fixed the groupby operation
    try:
        # Merge plans and rates data properly
        plans_with_rates = plans_df.merge(rates_df, on='PlanId', how='inner')
        avg_premium_by_metal = plans_with_rates.groupby('MetalLevel')['AvgIndividualRate'].mean().reset_index()
        
        fig_premium = px.bar(
            avg_premium_by_metal,
            x='MetalLevel',
            y='AvgIndividualRate',
            title="Average Premium by Metal Level",
            color='MetalLevel',
            color_discrete_map={
                'Bronze': '#8B4513',
                'Silver': '#A0522D',
                'Gold': '#DAA520',
                'Platinum': '#B8860B'
            }
        )
        fig_premium.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_premium, use_container_width=True)
    except Exception as e:
        st.warning(f"Could not generate premium chart: {e}")
        # Fallback to sample data
        sample_data = pd.DataFrame({
            'MetalLevel': ['Bronze', 'Silver', 'Gold', 'Platinum'],
            'AvgIndividualRate': [320, 450, 580, 720]
        })
        fig_premium = px.bar(
            sample_data,
            x='MetalLevel',
            y='AvgIndividualRate',
            title="Average Premium by Metal Level (Sample)",
            color='MetalLevel',
            color_discrete_map={
                'Bronze': '#8B4513',
                'Silver': '#A0522D',
                'Gold': '#DAA520',
                'Platinum': '#B8860B'
            }
        )
        fig_premium.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_premium, use_container_width=True)

st.markdown("---")

# Testimonials
st.markdown("## 💬 What our customers say")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>⭐⭐⭐⭐⭐</h4>
        <p>"Havenly helped me find a plan that actually fits my budget and covers what I need. The AI recommendations were spot-on!"</p>
        <strong>- Sarah Johnson, Small Business Owner</strong>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>⭐⭐⭐⭐⭐</h4>
        <p>"Switching our family insurance was a breeze. The comparison tools made it easy to see exactly what we were getting."</p>
        <strong>- Michael Chen, Family of 4</strong>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>⭐⭐⭐⭐⭐</h4>
        <p>"As a freelancer, I was worried about finding affordable coverage. Havenly found me a great plan with dental included!"</p>
        <strong>- Emily Rodriguez, Freelancer</strong>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# CTA section
st.markdown("## 🎯 Ready to find your perfect plan?")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style="background: linear-gradient(90deg, #8B4513 0%, #228B22 100%); padding: 2rem; border-radius: 15px; color: white;">
        <h2>Join thousands of customers who've already found their ideal insurance coverage</h2>
        <p>Get personalized recommendations in seconds with our AI-powered platform.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Get Started Now", use_container_width=True):
        st.switch_page("pages/Find_a_Plan.py")
    
    if st.button("💬 Chat with AI", use_container_width=True):
        st.switch_page("pages/You_and_your_Plan.py")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>© 2024 Havenly. All rights reserved. | Privacy Policy | Terms of Service</p>
    <p>📞 1-800-HAVENLY | 📧 hello@havenly.com | 🌐 havenly.com</p>
</div>
""", unsafe_allow_html=True)


