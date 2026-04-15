import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import plotly.graph_objects as go
import os
from dotenv import load_dotenv

# 1. Page Configuration
st.set_page_config(
    page_title="Fintech Auto Lab | Master Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()

# 2. Database Connection (with Mock Fallback for Demo)
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "quant_db"),
            user=os.getenv("DB_USER", "quant_user"),
            password=os.getenv("DB_PASS", "secure_password_123")
        )
        return conn
    except:
        return None

# 3. Sidebar Navigation
st.sidebar.title("⚡ Quant Lab")
page = st.sidebar.radio("Go to", ["Dashboard Overview", "Strategy Monitor", "Risk Desk", "Execution Analytics", "Ops & Compliance"])

st.sidebar.markdown("---")
st.sidebar.info(f"**System Status:** 🟢 Online\n\n**Active Bots:** 51\n\n**Last Update:** {pd.Timestamp.now().strftime('%H:%M:%S')}")

# ==========================================
# PAGE 1: DASHBOARD OVERVIEW
# ==========================================
if page == "Dashboard Overview":
    st.title("🚀 Command Center")
    
    # Top Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("AUM", "₹ 1,25,00,000", "+1.2%")
    col2.metric("Daily P&L", "₹ 45,200", "+0.36%")
    col3.metric("Sharpe Ratio", "2.1", "0.05")
    col4.metric("Active Alerts", "3", "-2", delta_color="inverse")
    
    # Main Chart: Portfolio vs Benchmark
    st.subheader("Performance Curve")
    # Mock Data for Visualization
    chart_data = pd.DataFrame({
        "Date": pd.date_range(start="2024-01-01", periods=100),
        "Portfolio": [100 + i + (i*0.1 * (-1 if i%5==0 else 1)) for i in range(100)],
        "Nifty 50": [100 + i*0.8 for i in range(100)]
    })
    fig = px.line(chart_data, x="Date", y=["Portfolio", "Nifty 50"], title="Cumulative Returns")
    st.plotly_chart(fig, use_container_width=True)

    # Recent Alerts (Mocked from Process 39, 48, etc.)
    st.subheader("🚨 Live Alert Feed")
    alerts = pd.DataFrame([
        {"Time": "14:30", "Process": "Yield Curve Monitor", "Message": "Inversion Detected (-5bps)", "Severity": "HIGH"},
        {"Time": "14:15", "Process": "Slippage Watchdog", "Message": "VWAP Algo slippage > 15bps", "Severity": "MEDIUM"},
        {"Time": "12:00", "Process": "Factor Exposure", "Message": "Oil Correlation > 0.6", "Severity": "LOW"},
    ])
    st.dataframe(alerts, use_container_width=True)

# ==========================================
# PAGE 2: STRATEGY MONITOR
# ==========================================
elif page == "Strategy Monitor":
    st.title("🧠 Strategy Allocations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Trend Following (Process 51)")
        # Mock Data from trend_directions table
        trend_data = pd.DataFrame([
            {"Asset": "NIFTY", "Trend": "LONG", "Strength": "85%"},
            {"Asset": "GOLD", "Trend": "LONG", "Strength": "92%"},
            {"Asset": "CRUDE", "Trend": "SHORT", "Strength": "45%"},
            {"Asset": "USDINR", "Trend": "NEUTRAL", "Strength": "10%"}
        ])
        st.dataframe(trend_data, hide_index=True)
        
    with col2:
        st.subheader("Sector Rotation (Process 45)")
        sector_data = pd.DataFrame({
            "Sector": ["Pharma", "Auto", "Bank", "IT", "Metal"],
            "Score": [8.5, 7.2, 5.0, -2.1, -5.5],
            "Action": ["BUY", "BUY", "HOLD", "SELL", "SELL"]
        })
        fig = px.bar(sector_data, x="Score", y="Sector", orientation='h', color="Action", 
                     color_discrete_map={"BUY": "green", "SELL": "red", "HOLD": "grey"})
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# PAGE 3: RISK DESK
# ==========================================
elif page == "Risk Desk":
    st.title("🛡️ Risk Management")
    
    # Process 23 (VaR) & Process 50 (Vol Control)
    col1, col2, col3 = st.columns(3)
    col1.metric("Portfolio VaR (95%)", "₹ 2,10,000", "Safe")
    col2.metric("Current Volatility", "14.5%", "Target: 12%")
    col3.metric("Leverage Ratio", "1.1x", "De-leveraging")
    
    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Delta Profile (Process 40)")
        greeks = pd.DataFrame([
            {"Instrument": "Calls", "Delta": 450},
            {"Instrument": "Puts", "Delta": -320},
            {"Instrument": "Futures Hedge", "Delta": -130}
        ])
        st.bar_chart(greeks.set_index("Instrument"))
        st.caption("Net Delta: 0 (Neutral)")
        
    with c2:
        st.subheader("Factor Exposure (Process 26)")
        factors = pd.DataFrame({
            "Factor": ["Market", "Interest Rates", "Oil", "Momentum"],
            "Beta": [0.95, -0.2, 0.65, 0.1]
        })
        fig = px.radar(factors, r='Beta', theta='Factor', fill='toself', range_r=[-1, 1])
        st.plotly_chart(fig)

# ==========================================
# PAGE 4: EXECUTION ANALYTICS
# ==========================================
elif page == "Execution Analytics":
    st.title("⚙️ Execution Quality (TCA)")
    
    st.subheader("Slippage by Algo (Process 39)")
    slippage_data = pd.DataFrame({
        "Algo": ["VWAP", "TWAP", "Pegging", "Iceberg"],
        "Slippage (bps)": [12.5, 4.2, -1.5, 2.0]
    })
    
    fig = px.bar(slippage_data, x="Algo", y="Slippage (bps)", 
                 color="Slippage (bps)", color_continuous_scale="RdYlGn_r")
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("ℹ️ **Insight:** 'Pegging' algo is generating negative slippage (Alpha). VWAP needs parameter tuning.")

# ==========================================
# PAGE 5: OPS & COMPLIANCE
# ==========================================
elif page == "Ops & Compliance":
    st.title("zz Back Office")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Reconciliation (Process 28)")
        st.success("✅ T+0 Recs Matched: 142/142 trades")
        st.warning("⚠️ Cash Break: ₹ 4.50 (Rounding Error)")
        
    with col2:
        st.subheader("Treasury Sweep (Process 29)")
        st.info("💰 ₹ 4,50,000 swept to Liquid Bees at 3:15 PM")

    st.subheader("System Health (Process 5)")
    health = pd.DataFrame({
        "Service": ["Database", "n8n Engine", "Broker API", "Market Data"],
        "Status": ["UP", "UP", "UP", "UP"],
        "Latency": ["12ms", "45ms", "120ms", "85ms"]
    })
    st.dataframe(health, use_container_width=True)