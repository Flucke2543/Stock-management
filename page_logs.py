# ============================================================
# pages_ui/page_logs.py — หน้า: ประวัติความเคลื่อนไหวสต็อค
# ============================================================
import time
import streamlit as st
import db
import auth
 
 
def render():
    st.title("🕒 ประวัติรายการทั้งหมด")
    logs = db.get_logs()
 
    if logs.empty:
        st.info("ยังไม่มีประวัติความเคลื่อนไหว")
        return
 
    st.dataframe(logs.drop(columns=["id"]), use_container_width=True, hide_index=True)
 
    # ส่วน Admin เท่านั้น: ลบประวัติ
    if auth.is_admin():
        _render_admin_delete(logs)
 
 
def _render_admin_delete(logs):
    st.divider()
    st.subheader("🗑️ ส่วนผู้ดูแลระบบ: ลบประวัติ")
 
    target_id = st.selectbox(
        "เลือก ID รายการที่ต้องการลบ (ดูลำดับจากตาราง)",
        logs["id"]
    )
 
    if st.button("🚨 ยืนยันการลบประวัติรายการนี้", type="primary"):
        db.delete_log(int(target_id))
        st.success(f"🗑️ ลบประวัติรายการ ID {target_id} เรียบร้อยแล้ว")
        time.sleep(2)
        st.rerun()
