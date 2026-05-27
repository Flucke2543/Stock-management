# ============================================================
# db.py — Database Layer
# ทุกอย่างที่เกี่ยวกับ SQLite อยู่ที่นี่ที่เดียว
# ============================================================
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

DB_FILE = "warehouse_storage.db"


# ── Helpers ─────────────────────────────────────────────────

def _now_th() -> str:
    """คืนค่าเวลาปัจจุบัน +7 ชั่วโมง เป็น string"""
    return (datetime.now() + timedelta(hours=7)).strftime("%Y-%m-%d %H:%M:%S")


def run_query(query: str, params: tuple = (), is_select: bool = False):
    """รันคำสั่ง SQL ถ้า is_select=True คืนค่า DataFrame"""
    with sqlite3.connect(DB_FILE) as conn:
        if is_select:
            return pd.read_sql_query(query, conn, params=params)
        conn.execute(query, params)
        conn.commit()


# ── Init ─────────────────────────────────────────────────────

def init_db():
    """สร้างตารางถ้ายังไม่มี และ migrate column ที่อาจขาด"""
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                product_code TEXT UNIQUE,
                product_name TEXT,
                location     TEXT,
                stock        INTEGER DEFAULT 0,
                damaged      INTEGER DEFAULT 0,
                cost         REAL    DEFAULT 0.0,
                price        REAL    DEFAULT 0.0
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                product_code TEXT,
                product_name TEXT,
                action       TEXT,
                amount       INTEGER,
                note         TEXT,
                time         TEXT
            )
        """)
        # Migrate: เพิ่ม column ที่อาจไม่มีในฐานข้อมูลเก่า
        for col, col_type in [("cost", "REAL"), ("price", "REAL")]:
            try:
                c.execute(f"ALTER TABLE products ADD COLUMN {col} {col_type} DEFAULT 0.0")
            except sqlite3.OperationalError:
                pass  # column มีอยู่แล้ว — ปกติ
        conn.commit()


# ── Products ─────────────────────────────────────────────────

def get_all_products() -> pd.DataFrame:
    return run_query("""
        SELECT
            product_code AS 'รหัสทรัพย์สิน',
            product_name AS 'ชื่อทรัพย์สิน',
            location     AS 'จุดเก็บทรัพย์สิน',
            stock        AS 'จำนวนที่ยังเหลือ',
            damaged      AS 'จำหน่าย',
            printf('%.2f', cost)  AS 'ราคาต้นทุน (บาท)',
            printf('%.2f', price) AS 'ราคาปรับ (บาท)'
        FROM products
    """, is_select=True)


def get_product_list() -> pd.DataFrame:
    return run_query(
        "SELECT product_code, product_name FROM products", is_select=True
    )


def get_stock(product_code: str) -> int:
    df = run_query(
        "SELECT stock FROM products WHERE product_code = ?",
        (product_code,), is_select=True
    )
    return int(df.iloc[0]["stock"]) if not df.empty else 0


def product_code_exists(product_code: str) -> bool:
    df = run_query(
        "SELECT product_code FROM products WHERE product_code = ?",
        (product_code,), is_select=True
    )
    return not df.empty


def add_product(code: str, name: str, location: str,
                stock: int, cost: float, price: float):
    run_query("""
        INSERT INTO products (product_code, product_name, location, stock, cost, price)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (code, name, location, stock, cost, price))
    _log(code, name, "🆕 ลงทะเบียนใหม่", stock, f"จุดเก็บ: {location}")


def delete_product(code: str, name: str):
    """ลบสินค้า และบันทึก log การลบ (ไม่ลบประวัติเดิม)"""
    run_query("DELETE FROM products WHERE product_code = ?", (code,))
    _log(code, name, "🗑️ ลบทรัพย์สิน", 0, "ลบออกจากระบบ")


# ── Stock Movement ───────────────────────────────────────────

def stock_in(code: str, name: str, amount: int, note: str):
    run_query(
        "UPDATE products SET stock = stock + ? WHERE product_code = ?",
        (amount, code)
    )
    _log(code, name, "รับเข้าทรัพย์สิน", amount, note)


def stock_out(code: str, name: str, amount: int, note: str) -> bool:
    """จำหน่ายสินค้า — คืน False ถ้าสต็อกไม่พอ"""
    if get_stock(code) < amount:
        return False
    run_query(
        "UPDATE products SET stock = stock - ? WHERE product_code = ?",
        (amount, code)
    )
    _log(code, name, "จำหน่ายทรัพย์สิน", amount, note)
    return True


# ── Logs ─────────────────────────────────────────────────────

def _log(code: str, name: str, action: str, amount: int, note: str):
    run_query("""
        INSERT INTO logs (product_code, product_name, action, amount, note, time)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (code, name, action, amount, note, _now_th()))


def get_logs() -> pd.DataFrame:
    return run_query("""
        SELECT id, time AS 'เวลา', product_code AS 'รหัสทรัพย์สิน',
               product_name AS 'ชื่อทรัพย์สิน', action AS 'กิจกรรม',
               amount AS 'จำนวน', note AS 'หมายเหตุ'
        FROM logs ORDER BY id DESC
    """, is_select=True)


def delete_log(log_id: int):
    run_query("DELETE FROM logs WHERE id = ?", (log_id,))
