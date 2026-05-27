# ============================================================
# auth.py — ระบบ Login และ Session
# ============================================================
import streamlit as st
from styles import load_login_css, load_dialog_css


@st.dialog("กู้คืนรหัสผ่าน")
def show_contact_admin():
    load_dialog_css()
    st.markdown("""
        <div style="text-align:center; padding: 8px 0;">
            <div style="font-family:'Rajdhani',sans-serif; font-size:1.4rem;
                        font-weight:600; color:#e6edf3; letter-spacing:1px;
                        margin-bottom:16px;">
                ติดต่อผู้ดูแลระบบ
            </div>
            <div style="background:#0d1117; border:1px solid #30363d;
                        border-left: 3px solid #00ff87;
                        border-radius:8px; padding:18px; margin:12px 0; text-align:left;">
                <div style="font-size:0.7rem; letter-spacing:2px; color:#7d8590;
                            text-transform:uppercase; margin-bottom:6px;">อีเมลแอดมิน</div>
                <div style="font-family:'JetBrains Mono',monospace; color:#00ff87;
                            font-size:0.95rem;">
                    Poonawitmuenwat@gmail.com
                </div>
            </div>
            <div style="color:#7d8590; font-size:0.82rem; margin-top:12px;">
                โปรดระบุชื่อผู้ใช้งานและแผนกของคุณเมื่อติดต่อ
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("ปิด", use_container_width=True):
        st.rerun()


def show_login_page():
    load_login_css()

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown("""
            <div style="height:90vh; background:#0d1117;
                        border: 1px solid #30363d; border-radius:16px;
                        display:flex; flex-direction:column;
                        justify-content:center; align-items:center;
                        padding:48px; position:relative; overflow:hidden;">

                <!-- Grid pattern overlay -->
                <div style="position:absolute; inset:0; opacity:0.04;
                    background-image: linear-gradient(#00ff87 1px, transparent 1px),
                                      linear-gradient(90deg, #00ff87 1px, transparent 1px);
                    background-size: 40px 40px; border-radius:16px;"></div>

                <!-- Accent corner -->
                <div style="position:absolute; top:0; left:0;
                            width:3px; height:80px; background:#00ff87;
                            border-radius:16px 0 0 0;"></div>
                <div style="position:absolute; top:0; left:0;
                            width:80px; height:3px; background:#00ff87;
                            border-radius:16px 0 0 0;"></div>
                <div style="position:absolute; bottom:0; right:0;
                            width:3px; height:80px; background:#00b4d8;
                            border-radius:0 0 16px 0;"></div>
                <div style="position:absolute; bottom:0; right:0;
                            width:80px; height:3px; background:#00b4d8;
                            border-radius:0 0 16px 0;"></div>

                <div style="text-align:center; position:relative; z-index:1;">
                    <div style="font-family:'Rajdhani',sans-serif; font-size:4.5rem;
                                font-weight:700; color:#00ff87; line-height:1;
                                letter-spacing:4px; text-shadow:0 0 40px rgba(0,255,135,0.5);">
                        WMS
                    </div>
                    <div style="width:60px; height:2px; background:#00ff87;
                                margin:12px auto; opacity:0.5;"></div>
                    <div style="font-family:'Rajdhani',sans-serif; font-size:1.1rem;
                                font-weight:500; color:#7d8590; letter-spacing:4px;
                                text-transform:uppercase;">
                        Warehouse Management
                    </div>
                    <div style="font-family:'Rajdhani',sans-serif; font-size:0.85rem;
                                font-weight:400; color:#30363d; letter-spacing:3px;
                                text-transform:uppercase; margin-top:4px;">
                        System v2.0
                    </div>
                </div>

                <div style="position:absolute; bottom:28px; left:0; right:0;
                            text-align:center;">
                    <div style="display:inline-flex; align-items:center; gap:8px;">
                        <div style="width:6px; height:6px; border-radius:50%;
                                    background:#00ff87;
                                    box-shadow:0 0 8px #00ff87;"></div>
                        <span style="font-family:'DM Sans'; font-size:0.72rem;
                                     color:#7d8590; letter-spacing:2px;">SYSTEM ONLINE</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        # Vertical center
        st.markdown("<div style='height:14vh'></div>", unsafe_allow_html=True)

        st.markdown("""
            <div style="padding: 0 8%;">
                <div style="font-family:'Rajdhani',sans-serif; font-size:0.75rem;
                            letter-spacing:4px; color:#00ff87; text-transform:uppercase;
                            margin-bottom:8px;">
                    ── เข้าสู่ระบบ
                </div>
                <div style="font-family:'Rajdhani',sans-serif; font-size:2.8rem;
                            font-weight:700; color:#e6edf3; line-height:1;
                            margin-bottom:32px;">
                    Sign In
                </div>
            </div>
        """, unsafe_allow_html=True)

        _, col_form, _ = st.columns([0.08, 0.84, 0.08])
        with col_form:
            st.markdown("<div style='margin-bottom:4px; font-size:0.68rem; letter-spacing:2px; color:#7d8590; text-transform:uppercase;'>Username</div>", unsafe_allow_html=True)
            username = st.text_input("u", placeholder="กรอก username", label_visibility="collapsed")

            st.markdown("<div style='margin-bottom:4px; margin-top:12px; font-size:0.68rem; letter-spacing:2px; color:#7d8590; text-transform:uppercase;'>Password</div>", unsafe_allow_html=True)
            password = st.text_input("p", type="password", placeholder="กรอก password", label_visibility="collapsed")

            _, col_forgot = st.columns([1.8, 1])
            with col_forgot:
                if st.button("Forgot Password?", type="tertiary"):
                    show_contact_admin()

            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            if st.button("SIGN IN", use_container_width=True):
                _authenticate(username, password)


def _authenticate(username: str, password: str):
    users = st.secrets.get("users", {})
    if username in users and users[username] == password:
        st.session_state["logged_in"] = True
        st.session_state["user_name"] = username
        st.query_params["login"] = "true"
        st.rerun()
    else:
        st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")


def init_session():
    if st.query_params.get("login") == "true":
        st.session_state["logged_in"] = True
    elif "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False


def is_logged_in() -> bool:
    return st.session_state.get("logged_in", False)


def is_admin() -> bool:
    admin_list = st.secrets.get("admin_users", {}).get("list", [])
    return st.session_state.get("user_name", "") in admin_list


def logout():
    st.session_state["logged_in"] = False
    st.query_params.clear()
    st.rerun()
