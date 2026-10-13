import tkinter as tk
from memory_manager import GotohMemory
from interface.tema import (
    FUNDO, FUNDO_SECUNDARIO, FUNDO_CARD_HOVER, TEXTO, TEXTO_SECUNDARIO, 
    ROXO_SUAVE, BORDA, FONTE
)

# Imports de todos os módulos de tela
import interface.telas.inicio as inicio
import interface.telas.conversa as conversa
import interface.telas.tarefas as tarefas
import interface.telas.estudos as estudos
import interface.telas.conhecimento as conhecimento
import interface.telas.projetos as projetos
import interface.telas.notas as notas
import interface.telas.progresso as progresso
import interface.telas.configuracoes as configuracoes

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gotoh — Agente Pessoal")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(bg=FUNDO)

        # Instâncias de dados e estado
        self.memoria_db = GotohMemory()
        self.config_data = {}  # Dict simples para configurações caso o módulo exija

        # Sidebar / Menu Lateral
        self.sidebar = tk.Frame(self, bg=FUNDO_SECUNDARIO, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Divisor Vertical Fino
        self.divisor = tk.Frame(self, bg=BORDA, width=1)
        self.divisor.pack(side="left", fill="y")

        # Container Principal de Conteúdo
        self.area_conteudo = tk.Frame(self, bg=FUNDO)
        self.area_conteudo.pack(side="right", fill="both", expand=True)

        self.botoes_menu = {}
        
        self.construir_sidebar()
        self.navegar_para("inicio")

    def construir_sidebar(self):
        # Header da Sidebar
        lbl_logo = tk.Label(
            self.sidebar, 
            text="GOTOH", 
            font=(FONTE, 14, "bold"), 
            bg=FUNDO_SECUNDARIO, 
            fg=ROXO_SUAVE, 
            anchor="w"
        )
        lbl_logo.pack(fill="x", padx=20, pady=(25, 2))

        lbl_sub = tk.Label(
            self.sidebar, 
            text="Agente Pessoal", 
            font=(FONTE, 9), 
            bg=FUNDO_SECUNDARIO, 
            fg=TEXTO_SECUNDARIO, 
            anchor="w"
        )
        lbl_sub.pack(fill="x", padx=20, pady=(0, 20))

        # Lista completa do Menu
        itens = [
            ("inicio", "Início"),
            ("conversa", "Conversa"),
            ("estudos", "Estudos"),
            ("conhecimento", "Conhecimento"),
            ("tarefas", "Tarefas"),
            ("projetos", "Projetos"),
            ("notas", "Notas"),
            ("progresso", "Progresso"),
            ("configuracoes", "Configurações"),
        ]

        for chave, rotulo in itens:
            btn = tk.Button(
                self.sidebar,
                text=rotulo,
                font=(FONTE, 10),
                bg=FUNDO_SECUNDARIO,
                fg=TEXTO_SECUNDARIO,
                activebackground=FUNDO_CARD_HOVER,
                activeforeground=TEXTO,
                bd=0,
                highlightthickness=0,
                relief="flat",
                anchor="w",
                padx=20,
                pady=8,
                cursor="hand2",
                command=lambda c=chave: self.navegar_para(c)
            )
            btn.pack(fill="x", pady=1)
            self.botoes_menu[chave] = btn

    def navegar_para(self, chave_tela):
        # Limpa o container principal
        for widget in self.area_conteudo.winfo_children():
            widget.destroy()

        # Destaque visual do botão ativo
        for chave, btn in self.botoes_menu.items():
            if chave == chave_tela:
                btn.configure(
                    bg=FUNDO_CARD_HOVER, 
                    fg=TEXTO, 
                    font=(FONTE, 10, "bold")
                )
            else:
                btn.configure(
                    bg=FUNDO_SECUNDARIO, 
                    fg=TEXTO_SECUNDARIO, 
                    font=(FONTE, 10)
                )

        # Mapeamento e chamada exata para cada tela
        if chave_tela == "inicio":
            if hasattr(inicio, "renderizar_inicio"):
                inicio.renderizar_inicio(self.area_conteudo)
            elif hasattr(inicio, "mostrar"):
                inicio.mostrar(self.area_conteudo)

        elif chave_tela == "conversa":
            conversa.mostrar(self.area_conteudo, self.memoria_db)

        elif chave_tela == "tarefas":
            tarefas.mostrar(self.area_conteudo)

        elif chave_tela == "estudos":
            estudos.mostrar(self.area_conteudo)

        elif chave_tela == "conhecimento":
            conhecimento.mostrar(self.area_conteudo)

        elif chave_tela == "projetos":
            projetos.mostrar(self.area_conteudo)

        elif chave_tela == "notas":
            notas.mostrar(self.area_conteudo)

        elif chave_tela == "progresso":
            progresso.mostrar(self.area_conteudo)

        elif chave_tela == "configuracoes":
            configuracoes.mostrar(self.area_conteudo, self.config_data)

def iniciar():
    app = App()
    app.mainloop()
