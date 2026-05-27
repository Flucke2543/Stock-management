# ============================================================
# app.py — Entry Point
# ============================================================
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

import db
import auth
import styles
import page_stock, page_movement, page_manage, page_logs

st.set_page_config(page_title="WMS — Warehouse Manager", layout="wide", page_icon="📦")

db.init_db()
auth.init_session()

# ── หน้า Login ───────────────────────────────────────────────
if not auth.is_logged_in():
    auth.show_login_page()
    st.stop()

# ── โปรแกรมหลัก ──────────────────────────────────────────────
styles.load_global_css()

st_autorefresh(interval=30000, key="clock_refresh")
now = datetime.now() + timedelta(hours=7)
current_time = now.strftime("%H:%M")

username = st.session_state.get("user_name", "User")
styles.load_sidebar_css(current_time, username)

# ── Menu ─────────────────────────────────────────────────────
MENU_OPTIONS = [
    "📦  สต็อกทรัพย์สินคงเหลือ",
    "🔄  รับเข้า / จำหน่าย",
    "📋  การจัดการรายการทรัพย์สิน",
    "🕒  ประวัติความเคลื่อนไหว",
]
menu = st.sidebar.radio("nav", MENU_OPTIONS, label_visibility="collapsed")

st.sidebar.markdown("<div style='flex:1'></div>", unsafe_allow_html=True)
st.sidebar.divider()
if st.sidebar.button("⏻  LOGOUT", use_container_width=True):
    auth.logout()

# ── Routing ──────────────────────────────────────────────────
if menu == MENU_OPTIONS[0]:
    page_stock.render()
elif menu == MENU_OPTIONS[1]:
    page_movement.render()
elif menu == MENU_OPTIONS[2]:
    page_manage.render()
elif menu == MENU_OPTIONS[3]:
    page_logs.render()
