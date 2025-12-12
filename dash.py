import time
import streamlit as st
from db import get_top_managers, get_company_totals, get_connection
from decimal import Decimal
from styles import get_dashboard_styles
import os
from PIL import Image


TARGET_TOTAL = 10000000

st.set_page_config(
    page_title="Credit Excellence Leaderboard",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(get_dashboard_styles(), unsafe_allow_html=True)

# Hide Streamlit UI chrome
hide_streamlit_style = """
    <style>
        #MainMenu, footer, header { display: none !important; }
        .stDeployButton { display: none !important; }
        #stDecoration { display: none !important; }
        .st-emotion-cache-zq5wmm, .st-emotion-cache-cio0dv { display: none !important; }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Logo at top center
logo_path = "/Users/mruthunjai_govindaraju/Documents/Workspace/BharatFincare/assests/image.png"
if os.path.exists(logo_path):
    try:
        col1, col2, col3 = st.columns([1.1, 1, 1])
        with col2:
            st.image(logo_path, width=400)
    except Exception as e:
        st.warning(f"Could not load image: {e}")

# Dashboard Header
st.markdown("""
    <div class="dashboard-header">
        <h1 class='dashboard-title'>🏆 Credit Excellence</h1>
        <p>Live Leaderboard • Sanction Performance Tracker</p>
    </div>
""", unsafe_allow_html=True)

placeholder = st.empty()


def get_initials(name):
    if not name:
        return "NA"
    parts = name.split()
    if len(parts) >= 2:
        return f"{parts[0][0]}{parts[-1][0]}".upper()
    return name[:2].upper() if len(name) >= 2 else name[0].upper()


def format_currency_inr(amount):
    amount_float = float(amount)
    if amount_float >= 10000000:
        return f"₹{amount_float/10000000:.2f}Cr"
    elif amount_float >= 100000:
        return f"₹{amount_float/100000:.1f}L"
    else:
        return f"₹{amount_float:,.0f}"


# 🔥 REAL-TIME REFRESH LOOP
while True:
    top_managers = get_top_managers(3)

    # NEW: Replace MySQL query with Supabase aggregated total
    total_sanction, _ = get_company_totals()

    with placeholder.container():

        total_float = float(total_sanction)
        completion_percentage = min(total_float / TARGET_TOTAL, 1.0) * 100

        # PROGRESS BAR
        st.markdown(f"""
            <div class="target-container">
                <div class="progress-label">
                    <div class="target-label">📊 TEAM PROGRESS</div>
                    <div class="target-value">{format_currency_inr(total_float)} / ₹1 Cr</div>
                </div>
                <div class="progress-wrapper">
                    <div class="simple-progress-bar">
                        <div class="progress-fill" style="width: {completion_percentage}%;">
                            <span class="percentage-badge">{completion_percentage:.1f}%</span>
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # LEADERBOARD
        st.markdown("""
            <div class="leaderboard-container">
                <div class="leaderboard-title">
                    <h3>Top Performers</h3>
                    <p class="leaderboard-subtitle">Real-time Sanction Rankings</p>
                </div>
        """, unsafe_allow_html=True)

        cols = st.columns([1, 1, 1], gap="medium")

        for i, (manager, total) in enumerate(top_managers):
            with cols[i]:
                total_float = float(total)
                initials = get_initials(manager)
                rank_class = f"rank-{i+1}"
                manager_percentage = (total_float / TARGET_TOTAL * 100)

                st.markdown(f"""
                    <div class='manager-card'>
                        <div class='card-top'>
                            <div class='manager-rank {rank_class}'>{i+1}</div>
                            <div class='manager-avatar'>{initials}</div>
                            <div class='manager-name'>{manager}</div>
                        </div>
                        <div class='card-bottom'>
                            <div class='manager-amount'>{format_currency_inr(total_float)}</div>
                            <div class='manager-target'><strong>{manager_percentage:.1f}%</strong> of target</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    time.sleep(5)
