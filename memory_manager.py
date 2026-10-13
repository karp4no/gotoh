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
        """Cria o banco de dados SQLite e as tabelas se não existirem."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Tabela para histórico de conversas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                remetente TEXT,
                mensagem TEXT
            )
        ''')
        
        # Tabela para fatos aprendidos sobre o usuário
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
        """Cria o JSON de configurações caso não exista."""
        if not os.path.exists(CONFIG_PATH):
            default_config = {
                "theme": "dark",
                "user_name": "Usuário",
                "notion_enabled": False
            }
            with open(CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(default_config, f, indent=4)

    # --- MÉTODOS DE CONVERSA ---
    def salvar_mensagem(self, remetente, mensagem):
        """Salva uma mensagem no histórico."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO conversas (timestamp, remetente, mensagem) VALUES (?, ?, ?)",
            (now, remetente, mensagem)
        )
        conn.commit()
        conn.close()

    def obter_historico_recente(self, limite=10):
        """Retorna as últimas N mensagens salvas."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT remetente, mensagem FROM conversas ORDER BY id DESC LIMIT ?", 
            (limite,)
        )
        mensagens = cursor.fetchall()
        conn.close()
        return mensagens[::-1] # Inverte para ordem cronológica

    # --- MÉTODOS DE FATOS/APRENDIZADO ---
    def guardar_fato(self, chave, valor):
        """Guarda ou atualiza uma informação específica do usuário."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO fatos_usuario (chave, valor) VALUES (?, ?)",
            (chave, valor)
        )
        conn.commit()
        conn.close()

    def obter_fatos(self):
        """Retorna todos os fatos salvos sobre o usuário."""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT chave, valor FROM fatos_usuario")
        fatos = cursor.fetchall()
        conn.close()
        return {chave: valor for chave, valor in fatos}

# Teste simples do módulo
if __name__ == "__main__":
    mem = GotohMemory()
    mem.salvar_mensagem("user", "Olá Gotoh, lembra de mim?")
    mem.salvar_mensagem("gotoh", "Com certeza! Em que posso ajudar?")
    mem.guardar_fato("curso", "Ciência da Computação")
    
    print("Histórico:", mem.obter_historico_recente())
    print("Fatos:", mem.obter_fatos())
