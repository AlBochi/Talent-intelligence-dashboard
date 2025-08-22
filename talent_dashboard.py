#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Dashboard setup
st.set_page_config(page_title="Talent Intelligence Dashboard", layout="wide")
st.title("🚀 Talent Intelligence Dashboard")
st.markdown("Real-time market analytics for Cloud Security & AI/ML talent")

# Mock data generation
def generate_market_data():
    roles = ['Cloud Security Engineer', 'MLOps Engineer', 'DevSecOps', 'AI Research Scientist']
    data = []
    for role in roles:
        for company in ['FAANG', 'Series B+ Startups', 'Enterprise', 'Crypto/NFT']:
            supply = np.random.randint(20, 100)
            demand = np.random.randint(50, 150)
            avg_salary = np.random.randint(140000, 250000)
            data.append([role, company, supply, demand, avg_salary])
    return pd.DataFrame(data, columns=['Role', 'Company_Type', 'Talent_Supply', 'Job_Demand', 'Avg_Salary'])

df = generate_market_data()

# Market Heatmap
st.header("🔍 Supply vs. Demand Heatmap")
fig = px.density_heatmap(df, x='Role', y='Company_Type', z='Job_Demand', 
                         title="Job Demand Concentration")
st.plotly_chart(fig, use_container_width=True)

# Compensation Analysis
st.header("💰 Compensation Benchmarks")
fig2 = px.box(df, x='Role', y='Avg_Salary', color='Company_Type',
             title="Salary Distributions by Role & Company Type")
st.plotly_chart(fig2, use_container_width=True)

# Talent Availability Score
st.header("🎯 Talent Availability Score")
df['Availability_Score'] = (df['Talent_Supply'] / df['Job_Demand']) * 100
fig3 = px.bar(df, x='Role', y='Availability_Score', color='Company_Type',
             title="Talent Availability (%) - Higher is Better")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.caption("Dashboard built with Streamlit | Data refreshed every 24 hours")
