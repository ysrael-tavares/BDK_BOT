import sqlite3

conn = sqlite3.connect('database/data.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_group INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    nick_group TEXT NOT NULL,
    atk INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    ca INTEGER NOT NULL,
    gold INTEGER NOT NULL,
    xp INTEGER NOT NULL,
    level INTEGER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER NOT NULL,
    id_group INTEGER NOT NULL,
    role INTEGER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER NOT NULL,
    nickname TEXT NOT NULL
);
""")