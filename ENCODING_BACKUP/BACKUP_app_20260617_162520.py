import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import streamlit as st
from datetime import datetime


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="IOTEC GLOBAL EXPERIENCE",
    page_icon="ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ'Ã‚Â¢ ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ADVANCED CSS
# =========================================================

st.markdown(
    """
    <style>

    html, body, [class*="css"] {

        background-color: #07090f;
        color: white;
        font-family: 'Segoe UI';
    }

    .main {

        background:
        radial-gradient(
            circle at top right,
            rgba(255,180,60,0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at bottom left,
            rgba(255,140,0,0.08),
            transparent 30%
        ),
        #07090f;
    }

    section[data-testid="stSidebar"] {

        background: rgba(10,10,15,0.95);

        border-right: 1px solid rgba(255,180,60,0.15);
    }

    .glass {

        background: rgba(255,255,255,0.05);

        border: 1px solid rgba(255,255,255,0.08);

        border-radius: 22px;

        padding: 22px;

        backdrop-filter: blur(14px);

        box-shadow:
        0 0 30px rgba(255,180,60,0.05);
    }

    .title {

        font-size: 42px;

        font-weight: 700;

        color: #ffcc70;
    }

    .subtitle {

        color: rgba(255,255,255,0.7);

        font-size: 18px;
    }

    .metric-card {

        background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.06),
            rgba(255,255,255,0.02)
        );

        border-radius: 24px;

        padding: 28px;

        border:
        1px solid rgba(255,180,60,0.12);

        transition: 0.3s;

        box-shadow:
        0 0 30px rgba(255,180,60,0.06);
    }

    .metric-title {

        font-size: 15px;

        color: rgba(255,255,255,0.6);
    }

    .metric-value {

        font-size: 34px;

        font-weight: bold;

        color: #ffcc70;
    }

    .panel-title {

        font-size: 24px;

        font-weight: 600;

        margin-bottom: 12px;

        color: #ffcc70;
    }

    .live {

        color: #6dff8b;

        font-weight: bold;
    }

    .log-box {

        background: rgba(0,0,0,0.35);

        border-radius: 16px;

        padding: 12px;

        border:
        1px solid rgba(255,255,255,0.05);

        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    # ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ'Ã‚Â¢  IOTEC

    ### GLOBAL EXPERIENCE
    """
)

st.sidebar.markdown("---")

menu = st.sidebar.radio(

    "NAVIGATION",

    [
        "Command Center",
        "Revenue",
        "AI Concierge",
        "Governance",
        "Modules",
        "Marketplace"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("CORE ONLINE")

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="glass">

        <div class="title">
        IOTEC GLOBAL EXPERIENCE
        </div>

        <div class="subtitle">
        Executive Cinematic Command Center
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    pass

    st.markdown(
        """
        <div class="metric-card">

            <div class="metric-title">
            ACTIVE MODULES
            </div>

            <div class="metric-value">
            4
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    pass

    st.markdown(
        """
        <div class="metric-card">

            <div class="metric-title">
            MONTHLY REVENUE
            </div>

            <div class="metric-value">
            $3700
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    pass

    st.markdown(
        """
        <div class="metric-card">

            <div class="metric-title">
            CLIENTS
            </div>

            <div class="metric-value">
            12
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    pass

    st.markdown(
        """
        <div class="metric-card">

            <div class="metric-title">
            SYSTEM STATUS
            </div>

            <div class="metric-value live">
            STABLE
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# MAIN PANELS
# =========================================================

left, right = st.columns([2,1])

# =========================================================
# LEFT
# =========================================================

with left:
    pass

    st.markdown(
        """
        <div class="glass">

            <div class="panel-title">
            LIVE MODULES
            </div>

            <div class="log-box">
            Commercial Intelligence ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ ACTIVE
            </div>

            <div class="log-box">
            Automation Spine ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ ACTIVE
            </div>

            <div class="log-box">
            Luxury Media Engine ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ ACTIVE
            </div>

            <div class="log-box">
            Technical Advisor ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ ACTIVE
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="glass">

            <div class="panel-title">
            MIDAS STRATEGIC INSIGHTS
            </div>

            <div class="log-box">
            Expand recurring revenue pipelines
            </div>

            <div class="log-box">
            Strengthen cinematic premium identity
            </div>

            <div class="log-box">
            Scale AI orchestration infrastructure
            </div>

            <div class="log-box">
            Expand enterprise acquisition systems
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# RIGHT
# =========================================================

with right:
    pass

    st.markdown(
        """
        <div class="glass">

            <div class="panel-title">
            AI CONCIERGE
            </div>

            AURELION ONLINE

            <br><br>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Ecosystem stable

            <br>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Governance active

            <br>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Revenue systems operational

            <br>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Expansion ready

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="glass">

            <div class="panel-title">
            GOVERNANCE
            </div>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Backup structure active

            <br>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Recovery protocol online

            <br>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Integrity scan stable

            <br>

            ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ Core protected

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.caption(
    f"IOTEC GLOBAL EXPERIENCE | "
    f"{datetime.now()}"
)



