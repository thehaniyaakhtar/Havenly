import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import os
from utils import load_trimmed_data, create_sample_data

st.set_page_config(page_title="Dashboard - Havenly", layout="wide")

# Custom CSS with earthy color scheme
st.markdown("""
<style>
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #8B4513;
    }
    .chart-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .goal-progress {
        background: #f8fafc;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load trimmed data
def load_dashboard_data():
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
with st.spinner("Loading dashboard data..."):
    plans_df, rates_df, benefits_df = load_dashboard_data()

# Header
st.markdown("# 📊 Insurance Dashboard")
st.markdown("### Track your coverage, claims, and savings in one place")

# Sidebar filters
with st.sidebar:
    st.markdown("## 🔍 Filters")
    
    # Time range
    time_range = st.selectbox(
        "Time Range",
        ["Last 30 days", "Last 3 months", "Last 6 months", "Last year", "All time"]
    )
    
    # State filter
    states = ["All States"] + sorted(rates_df['StateCode'].unique().tolist())
    selected_state = st.selectbox("State", states)
    
    # Metal level filter
    metal_levels = ["All Levels"] + sorted(plans_df['MetalLevel'].unique().tolist())
    selected_metal = st.selectbox("Metal Level", metal_levels)
    
    # Plan type filter
    plan_types = ["All Types"] + sorted(plans_df['PlanType'].unique().tolist())
    selected_plan_type = st.selectbox("Plan Type", plan_types)
    
    st.markdown("---")
    
    # Quick stats
    st.markdown("## 📈 Quick Stats")
    st.metric("Total Plans", f"{len(plans_df):,}")
    st.metric("Avg Premium", f"₹{rates_df['AvgIndividualRate'].mean():.0f}/month")
    st.metric("Coverage Score", "92%")

# Main dashboard content
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "💰 Financial", "🎯 Goals", "📋 Activity"])

with tab1:
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>💳 Monthly Premium</h3>
            <h2 style="color: #8B4513;">₹320</h2>
            <p style="color: #228B22;">↗️ +2.5% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🏥 Total Claims</h3>
            <h2 style="color: #8B4513;">₹280</h2>
            <p style="color: #DC143C;">↘️ -5.2% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>💰 Net Savings</h3>
            <h2 style="color: #8B4513;">₹40</h2>
            <p style="color: #228B22;">↗️ +12.8% from last month</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3>❤️ Coverage Score</h3>
            <h2 style="color: #8B4513;">92%</h2>
            <p style="color: #228B22;">↗️ +1.2% from last month</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Charts row 1
    col1, col2 = st.columns(2)
    
    with col1:
        # Plan distribution by metal level
        metal_counts = plans_df['MetalLevel'].value_counts()
        fig_metal = px.pie(
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
        fig_metal.update_layout(height=400)
        st.plotly_chart(fig_metal, use_container_width=True)
    
    with col2:
        # Premium distribution
        try:
            fig_premium = px.histogram(
                rates_df,
                x='AvgIndividualRate',
                nbins=20,
                title="Premium Distribution",
                color_discrete_sequence=['#8B4513']
            )
            fig_premium.update_layout(height=400, xaxis_title="Monthly Premium (₹)", yaxis_title="Number of Plans")
            st.plotly_chart(fig_premium, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not generate premium chart: {e}")

    # Charts row 2
    col1, col2 = st.columns(2)
    
    with col1:
        # Plan types
        plan_type_counts = plans_df['PlanType'].value_counts()
        fig_plan_type = px.bar(
            x=plan_type_counts.index,
            y=plan_type_counts.values,
            title="Plan Types Distribution",
            color_discrete_sequence=['#228B22']
        )
        fig_plan_type.update_layout(height=400, xaxis_title="Plan Type", yaxis_title="Number of Plans")
        st.plotly_chart(fig_plan_type, use_container_width=True)
    
    with col2:
        # State distribution
        state_counts = rates_df['StateCode'].value_counts().head(10)
        fig_state = px.bar(
            x=state_counts.index,
            y=state_counts.values,
            title="Top 10 States by Plan Availability",
            color_discrete_sequence=['#8B4513']
        )
        fig_state.update_layout(height=400, xaxis_title="State", yaxis_title="Number of Plans")
        st.plotly_chart(fig_state, use_container_width=True)

with tab2:
    st.markdown("## 💰 Financial Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Monthly premium trend
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        premiums = [320, 325, 318, 322, 320, 320]
        
        fig_trend = px.line(
            x=months,
            y=premiums,
            title="Monthly Premium Trend",
            markers=True
        )
        fig_trend.update_layout(height=400, xaxis_title="Month", yaxis_title="Premium (₹)")
        fig_trend.update_traces(line_color='#8B4513', marker_color='#228B22')
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with col2:
        # Cost breakdown
        categories = ['Premium', 'Deductible', 'Copays', 'Other']
        costs = [320, 150, 80, 50]
        
        fig_breakdown = px.pie(
            values=costs,
            names=categories,
            title="Monthly Cost Breakdown",
            color_discrete_sequence=['#8B4513', '#A0522D', '#DAA520', '#B8860B']
        )
        fig_breakdown.update_layout(height=400)
        st.plotly_chart(fig_breakdown, use_container_width=True)

with tab3:
    st.markdown("## 🎯 Health Goals")
    
    # Goal progress
    goals = [
        {"name": "Annual Checkup", "progress": 100, "target": "Completed", "status": "✅"},
        {"name": "Dental Cleaning", "progress": 75, "target": "Next: 2 weeks", "status": "🔄"},
        {"name": "Vision Exam", "progress": 0, "target": "Due: 3 months", "status": "⏰"},
        {"name": "Flu Shot", "progress": 100, "target": "Completed", "status": "✅"}
    ]
    
    for goal in goals:
        st.markdown(f"""
        <div class="goal-progress">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>{goal['status']} {goal['name']}</h4>
                <span>{goal['target']}</span>
            </div>
            <div style="background: #e0e0e0; border-radius: 10px; height: 10px; margin: 10px 0;">
                <div style="background: #228B22; width: {goal['progress']}%; height: 100%; border-radius: 10px;"></div>
            </div>
            <p style="text-align: center; margin: 0;">{goal['progress']}% Complete</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("## 📋 Recent Activity")
    
    # Activity timeline
    activities = [
        {"date": "2024-06-28", "activity": "Premium payment processed", "type": "payment"},
        {"date": "2024-06-25", "activity": "Claim submitted for dental cleaning", "type": "claim"},
        {"date": "2024-06-20", "activity": "Annual checkup completed", "type": "appointment"},
        {"date": "2024-06-15", "activity": "Plan renewal reminder sent", "type": "notification"},
        {"date": "2024-06-10", "activity": "New prescription added", "type": "prescription"}
    ]
    
    for activity in activities:
        icon = {
            "payment": "💳",
            "claim": "📋",
            "appointment": "🏥",
            "notification": "🔔",
            "prescription": "💊"
        }.get(activity["type"], "📝")
        
        st.markdown(f"""
        <div style="display: flex; align-items: center; padding: 10px; border-left: 3px solid #8B4513; margin: 10px 0; background: white; border-radius: 5px;">
            <span style="font-size: 1.5em; margin-right: 15px;">{icon}</span>
            <div>
                <strong>{activity['activity']}</strong><br>
                <small style="color: #666;">{activity['date']}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>Dashboard updated in real-time | Last updated: {}</p>
</div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True) 