# ============================================================
# pages_ui/page_manage.py — หน้า: จัดการรายการทรัพย์สิน
# ============================================================
import time
import streamlit as st
import db


def render():
    st.title("📋 ลงทะเบียนทรัพย์สินในระบบ")
    t1, t2 = st.tabs(["เพิ่มทรัพย์สินใหม่", "ลบทรัพย์สิน"])

    with t1:
        _render_add_tab()

    with t2:
        _render_delete_tab()


def _render_add_tab():
    with st.form("add_form", clear_on_submit=True):
        c = st.text_input("รหัสสินค้า / Barcode", placeholder="กรุณาระบุรหัสสินค้า")
        n = st.text_input("ชื่อสินค้า", placeholder="กรุณาระบุชื่อสินค้า")
        loc = st.text_input("ตำแหน่งที่เก็บ (Location)", placeholder="กรุณาระบุจุดจัดเก็บ")

        col1, col2 = st.columns(2)
        p_cost_raw = col1.text_input("ราคาต้นทุน (บาท)", placeholder="0.00")
        p_adj_raw = col2.text_input("ราคาปรับ (บาท)", placeholder="0.00")
        p_stock_raw = st.text_input("จำนวนสต็อกเริ่มต้น", placeholder="0")

        if st.form_submit_button("บันทึก"):
            _handle_add(c, n, loc, p_cost_raw, p_adj_raw, p_stock_raw)


def _handle_add(c, n, loc, p_cost_raw, p_adj_raw, p_stock_raw):
    if not c or not n:
        st.warning("⚠️ กรุณากรอกรหัสและชื่อสินค้าให้ครบถ้วน")
        return

    if db.product_code_exists(c):
        st.warning(f"⚠️ รหัสสินค้า '{c}' นี้มีอยู่ในระบบแล้ว กรุณาใช้รหัสอื่น")
        return

    try:
        final_cost = float(p_cost_raw) if p_cost_raw else 0.0
        final_adj = float(p_adj_raw) if p_adj_raw else 0.0
        final_stock = int(p_stock_raw) if p_stock_raw else 0
    except ValueError:
        st.error("⚠️ กรุณากรอกเฉพาะตัวเลขในช่องราคาและสต็อก")
        return

    db.add_product(c, n, loc, final_stock, final_cost, final_adj)
    st.success(f"✅ บันทึกสำเร็จ: {n}")
    time.sleep(2)
    st.rerun()


def _render_delete_tab():
    del_items = db.get_product_list()
    if del_items.empty:
        st.info("📂 ไม่พบข้อมูลรายการสินค้าในระบบ")
        return

    del_list = [f"{r['product_code']} | {r['product_name']}" for _, r in del_items.iterrows()]
    to_del = st.selectbox("กรุณาเลือกทรัพย์สินที่ต้องการลบ", del_list)

    # แสดง stock ปัจจุบันก่อนลบ
    code_preview = to_del.split(" | ")[0]
    stock_preview = db.get_stock(code_preview)
    if stock_preview > 0:
        st.warning(f"⚠️ ทรัพย์สินนี้ยังมีสต็อกเหลืออยู่ {stock_preview} ชิ้น คุณแน่ใจหรือไม่?")

    if st.button("ยืนยันการลบ", type="primary"):
        code_to_del = to_del.split(" | ")[0]
        name_to_del = to_del.split(" | ")[1]
        db.delete_product(code_to_del, name_to_del)
        st.info("🗑️ ลบรายการแล้ว")
        time.sleep(2)
        st.rerun()
