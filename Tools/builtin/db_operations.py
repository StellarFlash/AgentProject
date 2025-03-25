import sqlite3
from pathlib import Path
from Models.user_model import User

def init_db(db_path: str = "d:\\Agent\\AgentProject\\Resources\\test.db"):
    """初始化数据库连接"""
    Path(db_path).parent.mkdir(exist_ok=True)
    return sqlite3.connect(db_path)

def create_users_table(conn):
    """创建用户表"""
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()

def insert_user(conn, user: User):
    """插入用户数据"""
    conn.execute(
        "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
        (user.id, user.name, user.email)
    )
    conn.commit()