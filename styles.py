# ============================================================
# styles.py — CSS ทั้งหมดรวมไว้ที่นี่
# Design Direction: Industrial Dark
# โทน: ดำ/เทาเข้ม + accent เขียว neon #00ff87
# Font: Rajdhani (display) + DM Sans (body)
# ============================================================
import streamlit as st


# ── Palette ──────────────────────────────────────────────────
# BG_DEEP   = #080c10  (พื้นหลังลึกสุด)
# BG_PANEL  = #0d1117  (panel/sidebar)
# BG_CARD   = #161b22  (card surface)
# BG_HOVER  = #1c2333  (hover state)
# BORDER    = #30363d  (เส้นขอบ)
# ACCENT    = #00ff87  (เขียว neon — primary action)
# ACCENT2   = #00b4d8  (ฟ้า — secondary)
# TEXT_PRI  = #e6edf3  (ข้อความหลัก)
# TEXT_SEC  = #7d8590  (ข้อความรอง)
# RED       = #ff4b4b  (warning/danger)

GOOGLE_FONTS = "https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=DM+Sans:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap"


def load_fonts():
    st.markdown(f'<link href="{GOOGLE_FONTS}" rel="stylesheet">', unsafe_allow_html=True)


def load_global_css():
    """CSS พื้นฐานที่ใช้ทุกหน้า"""
    st.markdown(f"""
    <link href="{GOOGLE_FONTS}" rel="stylesheet">
    <style>
    :root {{
        --bg-deep:   #080c10;
        --bg-panel:  #0d1117;
        --bg-card:   #161b22;
        --bg-hover:  #1c2333;
        --border:    #30363d;
        --accent:    #00ff87;
        --accent2:   #00b4d8;
        --text-pri:  #e6edf3;
        --text-sec:  #7d8590;
        --red:       #ff4b4b;
        --font-dis:  'Rajdhani', sans-serif;
        --font-bod:  'DM Sans', sans-serif;
        --font-mon:  'JetBrains Mono', monospace;
    }}

    html, body, .stApp {{
        background-color: var(--bg-deep) !important;
        color: var(--text-pri) !important;
        font-family: var(--font-bod) !important;
    }}

    header[data-testid="stHeader"] {{ visibility: hidden; height: 0; }}

    /* ── Titles ── */
    h1, h2, h3 {{
        font-family: var(--font-dis) !important;
        color: var(--text-pri) !important;
        letter-spacing: 1px;
    }}
    h1 {{ font-size: 2rem !important; font-weight: 700 !important; }}

    /* ── Dataframe ── */
    [data-testid="stDataFrame"] {{
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        overflow: hidden;
    }}

    /* ── Metric ── */
    [data-testid="stMetric"] {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 16px 20px !important;
    }}
    [data-testid="stMetricValue"] {{
        font-family: var(--font-mon) !important;
        color: var(--accent) !important;
        font-size: 2rem !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: var(--text-sec) !important;
        font-size: 0.75rem !important;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}

    /* ── Inputs ── */
    div[data-baseweb="input"] > div,
    div[data-baseweb="textarea"] > div {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
    }}
    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="textarea"] > div:focus-within {{
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(0,255,135,0.15) !important;
    }}
    input, textarea {{
        color: var(--text-pri) !important;
        font-family: var(--font-bod) !important;
        -webkit-text-fill-color: var(--text-pri) !important;
        caret-color: var(--accent) !important;
    }}
    input::placeholder, textarea::placeholder {{
        color: var(--text-sec) !important;
        -webkit-text-fill-color: var(--text-sec) !important;
    }}
    label[data-testid="stWidgetLabel"] p {{
        color: var(--text-sec) !important;
        font-size: 0.72rem !important;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        font-family: var(--font-bod) !important;
    }}

    /* ── Select / Dropdown ── */
    div[data-baseweb="select"] > div {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
        color: var(--text-pri) !important;
    }}
    div[data-baseweb="select"] > div:focus-within {{
        border-color: var(--accent) !important;
    }}

    /* ── Number input ── */
    div[data-testid="stNumberInput"] div[data-baseweb="input"] > div {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
    }}

    /* ── Buttons ── */
    div.stButton > button {{
        background: transparent !important;
        color: var(--accent) !important;
        border: 1px solid var(--accent) !important;
        border-radius: 4px !important;
        font-family: var(--font-dis) !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        padding: 8px 24px !important;
        transition: all 0.2s ease !important;
    }}
    div.stButton > button:hover {{
        background: var(--accent) !important;
        color: #080c10 !important;
        box-shadow: 0 0 20px rgba(0,255,135,0.3) !important;
    }}
    div.stButton > button[kind="primary"] {{
        background: var(--accent) !important;
        color: #080c10 !important;
        border-color: var(--accent) !important;
        font-weight: 700 !important;
    }}
    div.stButton > button[kind="primary"]:hover {{
        box-shadow: 0 0 28px rgba(0,255,135,0.45) !important;
    }}

    /* ── Tabs ── */
    div[data-testid="stTabs"] button {{
        font-family: var(--font-dis) !important;
        color: var(--text-sec) !important;
        font-size: 1rem !important;
        letter-spacing: 1px;
        border-bottom: 2px solid transparent !important;
        background: transparent !important;
        border-top: none !important;
        border-left: none !important;
        border-right: none !important;
    }}
    div[data-testid="stTabs"] button[aria-selected="true"] {{
        color: var(--accent) !important;
        border-bottom-color: var(--accent) !important;
    }}

    /* ── Radio (เมนู sidebar override ด้านล่าง) ── */
    div[role="radiogroup"] label {{
        color: var(--text-pri) !important;
    }}

    /* ── Alerts ── */
    div[data-testid="stAlert"] {{
        border-radius: 6px !important;
        border-left-width: 3px !important;
    }}

    /* ── Divider ── */
    hr {{ border-color: var(--border) !important; }}

    /* ── Form ── */
    div[data-testid="stForm"] {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 24px !important;
    }}

    /* ── Spinner / info ── */
    .stInfo {{ background: rgba(0,180,216,0.08) !important; border-left: 3px solid var(--accent2) !important; }}
    .stSuccess {{ background: rgba(0,255,135,0.08) !important; border-left: 3px solid var(--accent) !important; }}
    .stWarning {{ background: rgba(255,190,0,0.08) !important; }}
    .stError   {{ background: rgba(255,75,75,0.08) !important; border-left: 3px solid var(--red) !important; }}
    </style>
    """, unsafe_allow_html=True)


def load_sidebar_css(current_time: str, username: str):
    """Sidebar พร้อมนาฬิกาและ user info"""
    st.markdown(f"""
    <style>
    /* ── Sidebar shell ── */
    [data-testid="stSidebar"] {{
        background-color: var(--bg-panel) !important;
        border-right: 1px solid var(--border) !important;
        min-width: 280px !important;
        max-width: 280px !important;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        padding: 0 !important;
    }}

    /* ── ซ่อน radio dot ── */
    [data-testid="stSidebar"] div[role="radiogroup"] > label > div:first-child {{
        display: none;
    }}

    /* ── Menu items ── */
    [data-testid="stSidebar"] div[role="radiogroup"] > label {{
        background: transparent !important;
        border: none !important;
        border-left: 3px solid transparent !important;
        border-radius: 0 !important;
        color: var(--text-sec) !important;
        padding: 12px 20px !important;
        margin: 2px 0 !important;
        font-family: var(--font-dis) !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.5px;
        transition: all 0.18s ease !important;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }}
    [data-testid="stSidebar"] div[role="radiogroup"] > label:hover {{
        background: var(--bg-hover) !important;
        color: var(--text-pri) !important;
        border-left-color: var(--accent2) !important;
    }}
    [data-testid="stSidebar"] div[role="radiogroup"] > label[data-checked="true"] {{
        background: rgba(0,255,135,0.07) !important;
        color: var(--accent) !important;
        border-left-color: var(--accent) !important;
        font-weight: 600 !important;
    }}

    /* ── Logout button override ── */
    [data-testid="stSidebar"] div.stButton > button {{
        width: 100% !important;
        background: transparent !important;
        color: var(--text-sec) !important;
        border: 1px solid var(--border) !important;
        border-radius: 4px !important;
        font-family: var(--font-dis) !important;
        letter-spacing: 1px;
        margin-top: 8px;
        transition: all 0.2s !important;
    }}
    [data-testid="stSidebar"] div.stButton > button:hover {{
        border-color: var(--red) !important;
        color: var(--red) !important;
        background: rgba(255,75,75,0.07) !important;
        box-shadow: none !important;
    }}
    </style>

    <style>
    .sb-clock-wrap {{
        padding: 20px 20px 12px 20px;
        border-bottom: 1px solid var(--border);
        margin-bottom: 8px;
    }}
    .sb-clock-label {{
        font-family: var(--font-bod);
        font-size: 0.65rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: var(--text-sec);
        margin-bottom: 2px;
    }}
    .sb-clock-time {{
        font-family: var(--font-mon);
        font-size: 2.8rem;
        font-weight: 500;
        color: var(--accent);
        line-height: 1;
        letter-spacing: -1px;
        text-shadow: 0 0 24px rgba(0,255,135,0.4);
    }}
    .sb-clock-sec {{
        font-family: var(--font-mon);
        font-size: 0.8rem;
        color: var(--text-sec);
        margin-top: 4px;
    }}
    .sb-user-wrap {{
        padding: 14px 20px;
        border-bottom: 1px solid var(--border);
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    .sb-avatar {{
        width: 36px; height: 36px;
        border-radius: 50%;
        background: linear-gradient(135deg, #00ff87 0%, #00b4d8 100%);
        display: flex; align-items: center; justify-content: center;
        font-family: var(--font-dis);
        font-weight: 700;
        font-size: 1rem;
        color: #080c10;
        flex-shrink: 0;
    }}
    .sb-user-name {{
        font-family: var(--font-dis);
        font-weight: 600;
        font-size: 1rem;
        color: var(--text-pri);
        letter-spacing: 0.5px;
    }}
    .sb-user-role {{
        font-size: 0.68rem;
        color: var(--text-sec);
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }}
    .sb-menu-label {{
        padding: 6px 20px 4px 20px;
        font-family: var(--font-bod);
        font-size: 0.62rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--text-sec);
    }}
    </style>
    """, unsafe_allow_html=True)

    avatar_char = username[0].upper() if username else "U"

    st.sidebar.markdown(f"""
        <div class="sb-clock-wrap">
            <div class="sb-clock-label">&#9711; Local Time</div>
            <div class="sb-clock-time">{current_time}</div>
        </div>
        <div class="sb-user-wrap">
            <div class="sb-avatar">{avatar_char}</div>
            <div>
                <div class="sb-user-name">{username}</div>
                <div class="sb-user-role">Warehouse Staff</div>
            </div>
        </div>
        <div class="sb-menu-label">Navigation</div>
    """, unsafe_allow_html=True)


def load_login_css():
    st.markdown(f"""
    <link href="{GOOGLE_FONTS}" rel="stylesheet">
    <style>
    html, body, .stApp {{
        background-color: var(--bg-deep) !important;
        font-family: var(--font-bod) !important;
    }}
    header {{ visibility: hidden; }}

    /* ── Input (login page) ── */
    div[data-baseweb="input"] > div {{
        background-color: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
        transition: border 0.2s;
    }}
    div[data-baseweb="input"] > div:focus-within {{
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(0,255,135,0.12) !important;
    }}
    input {{
        color: var(--text-pri) !important;
        font-family: var(--font-bod) !important;
        -webkit-text-fill-color: var(--text-pri) !important;
        caret-color: var(--accent) !important;
    }}
    input::placeholder {{
        color: var(--text-sec) !important;
        -webkit-text-fill-color: var(--text-sec) !important;
    }}

    /* ── Login main button ── */
    div.stButton > button {{
        width: 100% !important;
        background: var(--accent) !important;
        color: #080c10 !important;
        border: none !important;
        border-radius: 6px !important;
        font-family: var(--font-dis) !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        padding: 12px !important;
        transition: all 0.2s !important;
    }}
    div.stButton > button:hover {{
        box-shadow: 0 0 28px rgba(0,255,135,0.4) !important;
        transform: translateY(-1px) !important;
    }}

    /* ── Forgot password (tertiary) ── */
    div.stButton > button[kind="tertiary"] {{
        background: transparent !important;
        color: var(--text-sec) !important;
        border: none !important;
        font-family: var(--font-bod) !important;
        font-size: 0.8rem !important;
        font-weight: 300 !important;
        padding: 0 !important;
        letter-spacing: 0 !important;
        float: right;
        margin-top: -18px !important;
        box-shadow: none !important;
        transform: none !important;
    }}
    div.stButton > button[kind="tertiary"]:hover {{
        color: var(--accent) !important;
        text-decoration: underline !important;
        box-shadow: none !important;
        transform: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)


def load_dialog_css():
    st.markdown("""
    <style>
    div[data-testid="stDialog"] div[role="dialog"] {{
        background: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 12px !important;
    }}
    button[aria-label="Close"] {{
        color: #7d8590 !important;
        background: transparent !important;
        border: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)
