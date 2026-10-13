import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.expanduser("~/Gotoh/gotoh_memory.db")
CONFIG_PATH = os.path.expanduser("~/Gotoh/config.json")

class GotohMemory:
    def __init__(self):
        self._init_db()
        self._init_config()

    def _init_db(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                remetente TEXT,
                mensagem TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fatos_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chave TEXT UNIQUE,
                valor TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def _init_config(self):
        if not os.path.exists(CONFIG_PATH):
            default_config = {"theme": "dark", "user_name": "Rodrigo"}
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(default_config, f, indent=4)

    def salvar_mensagem(self, remetente, mensagem):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO conversas (timestamp, remetente, mensagem) VALUES (?, ?, ?)", (now, remetente, mensagem))
        conn.commit()
        conn.close()

    def obter_fatos(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT chave, valor FROM fatos_usuario")
        fatos = {row[0]: row[1] for row in cursor.fetchall()}
        conn.close()
        return fatos
