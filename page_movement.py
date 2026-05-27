# ============================================================
# pages_ui/page_movement.py — หน้า: รับเข้า/จำหน่าย
# ============================================================
import time
import streamlit as st
import db


def render():
    st.title("🔄 บันทึกความเคลื่อนไหว")

    prods = db.get_product_list()
    if prods.empty:
        st.info("⚠️ ไม่พบข้อมูลทรัพย์สิน กรุณาลงทะเบียนทรัพย์สินก่อน")
        return

    plist = [f"{r['product_code']} | {r['product_name']}" for _, r in prods.iterrows()]
    sel = st.selectbox("กรุณาเลือกทรัพย์สินที่ต้องการ", plist)
    code = sel.split(" | ")[0]
    name = sel.split(" | ")[1].strip()

    # แสดงสต็อกปัจจุบัน
    current_stock = db.get_stock(code)
    st.metric("สต็อกปัจจุบัน", f"{current_stock} ชิ้น")

    col1, col2 = st.columns(2)
    amt = col1.number_input("จำนวนทรัพย์สิน", min_value=1, step=1,
                             placeholder="ใส่จำนวนที่ต้องการ", key="input_amt")
    action = col2.radio("ประเภทรายการ", ["รับเข้าทรัพย์สิน", "จำหน่ายทรัพย์สิน"])
    note = st.text_input("หมายเหตุ", placeholder="ระบุเหตุผล หรือเลขที่ใบรับของ", key="input_note")

    if st.button("บันทึกรายการ"):
        if action == "รับเข้าทรัพย์สิน":
            db.stock_in(code, name, amt, note)
            st.success("✅ บันทึกรายการรับเข้าสำเร็จ!")
        else:
            # ตรวจสอบว่าสต็อกพอก่อนจำหน่าย
            success = db.stock_out(code, name, amt, note)
            if success:
                st.success("✅ บันทึกรายการจำหน่ายสำเร็จ!")
            else:
                st.error(f"❌ สต็อกไม่เพียงพอ! มีอยู่ {current_stock} ชิ้น แต่ต้องการจำหน่าย {amt} ชิ้น")
                return
        time.sleep(2)
        st.rerun()
