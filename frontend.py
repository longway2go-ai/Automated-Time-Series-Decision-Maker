import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="🚀 AI Stock Prophet - Smart Investment Decisions",
    layout="wide",
    page_icon="💹"
)

# Minimal CSS that actually works in Streamlit
st.markdown("""
<style>
    /* Simple, reliable styling */
    .main-container {
        background: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .mode-card {
        background: white;
        border: 2px solid #ddd;
        padding: 30px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .beginner-card { border-color: #27ae60; }
    .expert-card { border-color: #e74c3c; }
    
    .btn {
        background: #3498db;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin: 10px 0;
    }
    
    .btn-green { background: #27ae60; }
    .btn-red { background: #e74c3c; }
    
    .btn:hover { opacity: 0.9; transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

# --------- HERO SECTION ---------
st.markdown("""
<div class="hero">
    <h1>🚀 AI STOCK PROPHET</h1>
    <h3>Unleash the Power of AI for Smarter Investment Decisions</h3>
    <p>📊 Advanced Analytics • 🎯 Precise Predictions • 💡 Expert Insights</p>
</div>
""", unsafe_allow_html=True)

# --------- INTRO SECTION ---------
st.markdown("## 🧠 Welcome to the Future of Stock Analysis")

st.write("""
Transform your investment strategy with our cutting-edge AI platform. Whether you're taking your first steps 
in the stock market or you're a seasoned trader seeking advanced analytics, we've crafted the perfect 
tools to elevate your decision-making process.
""")

# Feature highlights using native Streamlit
col1, col2, col3 = st.columns(3)
with col1:
    st.info("🎯 **AI-Powered Predictions**\n\nSmart analysis using advanced machine learning")
with col2:
    st.info("📈 **Visual Analytics**\n\nBeautiful charts and trend visualizations")  
with col3:
    st.info("⚡ **User-Friendly Interface**\n\nDesigned for both beginners and experts")

st.markdown("---")

# --------- CHOICE SECTION ---------
st.markdown("## 🎪 Choose Your Experience Level")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="mode-card beginner-card">
        <h3 style="color: #27ae60;">🌱 BEGINNER MODE</h3>
        <h4 style="color: #2c3e50;">Perfect for New Investors</h4>
        <p style="color: #2c3e50;">Start your investment journey with confidence! Our beginner-friendly interface provides:</p>
        <ul style="color: #2c3e50;">
            <li>🎯 Simple buy/sell/hold recommendations</li>
            <li>🤖 AI-powered predictions in plain English</li>
            <li>💡 Educational tips and market insights</li>
            <li>📱 Mobile-friendly, intuitive design</li>
            <li>⚡ Quick analysis in under a minute</li>
        </ul>
        <div style="text-align: center;">
            <a href="https://huggingface.co/spaces/ArnabDeo/ai-stock-predictor" target="_blank">
                <button class="btn btn-green">🚀 Start Your Investment Journey</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="mode-card expert-card">
        <h3 style="color: #e74c3c;">⚡ EXPERT MODE</h3>
        <h4 style="color: #2c3e50;">Advanced Analytics Hub</h4>
        <p style="color: #2c3e50;">Dive deep with professional-grade analysis tools designed for serious traders:</p>
        <ul style="color: #2c3e50;">
            <li>📊 ARIMA & SARIMA statistical modeling</li>
            <li>🔬 Comprehensive exploratory data analysis</li>
            <li>📁 Custom dataset upload capabilities</li>
            <li>🎯 Technical indicators & trading signals</li>
            <li>💾 Downloadable professional reports</li>
        </ul>
        <div style="text-align: center;">
            <a href="https://time-series-for-experts.streamlit.app/" target="_blank">
                <button class="btn btn-red">🔬 Enter the Expert Zone</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --------- COMPARISON TABLE ---------
st.markdown("## 📋 Platform Comparison")

# Using Streamlit's native table for better visibility
import pandas as pd

comparison_df = pd.DataFrame({
    "Feature": [
        "Learning Curve", "AI Predictions", "Statistical Models", 
        "Custom Data Upload", "Visual Charts", "Analysis Time",
        "Mobile Friendly", "Export Reports", "Best For"
    ],
    "🌱 Beginner Mode": [
        "✅ Minimal", "✅ Yes", "❌ No", "❌ No", "✅ Interactive",
        "⚡ ~30 seconds", "✅ Fully Responsive", "❌ No", "New Investors"
    ],
    "⚡ Expert Mode": [
        "🔄 Moderate", "❌ No", "✅ ARIMA/SARIMA", "✅ Yes", "✅ Professional",
        "⏱️ 2-5 minutes", "🔄 Desktop Optimized", "✅ PDF/CSV", "Traders & Analysts"
    ]
})

st.table(comparison_df)

# --------- TECHNOLOGY SECTION ---------
st.markdown("## 🔮 Powered by Advanced Technology")

st.write("**🚀 AI Models & Algorithms**")
st.write("""
Our platform leverages state-of-the-art machine learning models including Amazon Chronos and 
Salesforce Moirai for time series forecasting, combined with traditional statistical methods 
like ARIMA and SARIMA for comprehensive market analysis.
""")

st.write("**⚡ Real-Time Data Processing**")
st.write("""
Get instant analysis on US stocks with live data feeds from Yahoo Finance. Our systems 
process historical trends, price patterns, and market indicators to provide you with 
actionable investment insights.
""")

# --------- FEATURES SECTION ---------
st.markdown("## 🛠️ What's Under the Hood")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🤖 AI Technology")
    st.write("• Amazon Chronos Models")
    st.write("• Salesforce Moirai Framework")
    st.write("• PyTorch & Transformers")
    st.write("• Real-time Processing")

with col2:
    st.markdown("### 📊 Statistical Models")
    st.write("• ARIMA Time Series")
    st.write("• SARIMA Seasonal Analysis")
    st.write("• Exponential Smoothing")
    st.write("• Trend Decomposition")

with col3:
    st.markdown("### 🔧 Built With")
    st.write("• Gradio & Streamlit")
    st.write("• Plotly Visualizations")
    st.write("• Yahoo Finance API")
    st.write("• HuggingFace Spaces")

# --------- CALL TO ACTION ---------
st.markdown("---")
st.markdown("## 🎯 Ready to Start?")
st.write("Choose your preferred experience level above and start analyzing stocks with AI!")

# --------- FOOTER ---------
st.markdown("---")
st.markdown("""
**© 2025 AI Stock Prophet** | Powered by Advanced AI & Machine Learning

⚠️ **Educational purposes only. Not financial advice. Always do your own research before investing.**
""")

