# ============================================================
# pages_ui/page_stock.py — หน้า: สต็อกทรัพย์สินคงเหลือ
# ============================================================
import streamlit as st
import db


def render():
    st.title("📦 จำนวนทรัพย์สินคงเหลือในโกดัง")
    df = db.get_all_products()
    if not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("ยังไม่มีข้อมูลสินค้าในคลัง")
