import threading
import tkinter as tk
from tkinter import scrolledtext
from memory_manager import GotohMemory

from interface import tema

try:
    from sistema.agente import processar_comando
except ImportError:
    processar_comando = None

try:
    from sistema import voz
except ImportError:
    voz = None


def limpar_conteudo(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def mostrar_conversa(conteudo, memoria_db=None):
    mostrar(conteudo, memoria_db)


def mostrar(conteudo, memoria_db=None):
    if memoria_db is None:
        memoria_db = GotohMemory()

    limpar_conteudo(conteudo)

    main_frame = tk.Frame(conteudo, bg=tema.FUNDO)
    main_frame.pack(fill="both", expand=True)

    # 1. HEADER (Topo)
    header_frame = tk.Frame(main_frame, bg=tema.FUNDO, padx=20, pady=12)
    header_frame.pack(side="top", fill="x")

    tk.Label(
        header_frame,
        text="Conversa",
        font=(tema.FONTE, 18, "bold"),
        fg=tema.TEXTO,
        bg=tema.FUNDO,
        anchor="w",
    ).pack(fill="x")

    tk.Label(
        header_frame,
        text="Fale com o Gotoh e deixe ele cuidar das suas informações.",
        font=(tema.FONTE, 9),
        fg=tema.TEXTO_SECUNDARIO,
        bg=tema.FUNDO,
        anchor="w",
    ).pack(fill="x", pady=(2, 0))

    # 2. RODAPÉ (Entrada de Mensagens e Ações)
    footer_frame = tk.Frame(main_frame, bg=tema.FUNDO, padx=20, pady=12)
    footer_frame.pack(side="bottom", fill="x")

    input_container = tk.Frame(footer_frame, bg=tema.FUNDO)
    input_container.pack(side="bottom", fill="x")

    # Botão Enviar
    btn_enviar = tk.Button(
        input_container,
        text="Enviar",
        bg=tema.ROXO,
        fg=tema.TEXTO,
        font=(tema.FONTE, 10, "bold"),
        bd=0,
        padx=18,
        pady=6,
        activebackground=tema.ROXO_CLARO,
        activeforeground=tema.TEXTO,
        cursor="hand2",
    )
    btn_enviar.pack(side="right", padx=(6, 0))

    # Botão Voz
    btn_voz = tk.Button(
        input_container,
        text="🎤",
        bg=tema.FUNDO_CARD,
        fg=tema.TEXTO,
        font=(tema.FONTE, 11),
        bd=0,
        padx=12,
        pady=5,
        activebackground=tema.FUNDO_CARD_HOVER,
        activeforeground=tema.TEXTO,
        cursor="hand2",
    )
    btn_voz.pack(side="right", padx=(6, 0))

    # Campo de Entrada
    input_box = tk.Frame(
        input_container,
        bg=tema.FUNDO_INPUT,
        highlightbackground=tema.BORDA,
        highlightthickness=1,
        padx=10,
        pady=6,
    )
    input_box.pack(side="left", fill="x", expand=True)

    entry_msg = tk.Entry(
        input_box,
        bg=tema.FUNDO_INPUT,
        fg=tema.TEXTO,
        insertbackground=tema.TEXTO,
        font=(tema.FONTE, 11),
        bd=0,
    )
    entry_msg.pack(fill="x", expand=True)

    # Linha de Status
    toolbar_frame = tk.Frame(footer_frame, bg=tema.FUNDO, pady=4)
    toolbar_frame.pack(side="bottom", fill="x", pady=(0, 6))

    status_label = tk.Label(
        toolbar_frame,
        text="● Memória Ativa",
        font=(tema.FONTE, 9),
        fg=tema.VERDE,
        bg=tema.FUNDO,
    )
    status_label.pack(side="left")

    def limpar_chat():
        chat_area.config(state=tk.NORMAL)
        chat_area.delete("1.0", tk.END)
        chat_area.config(state=tk.DISABLED)

    btn_limpar = tk.Button(
        toolbar_frame,
        text="🗑️️ Limpar Tela",
        command=limpar_chat,
        bg=tema.FUNDO_CARD,
        fg=tema.TEXTO_SECUNDARIO,
        font=(tema.FONTE, 8, "bold"),
        bd=0,
        padx=8,
        pady=3,
        activebackground=tema.FUNDO_CARD_HOVER,
        activeforeground=tema.TEXTO,
        cursor="hand2",
    )
    btn_limpar.pack(side="right")

    # 3. ÁREA DE CHAT (Centro)
    chat_frame = tk.Frame(main_frame, bg=tema.FUNDO, padx=20, pady=5)
    chat_frame.pack(side="top", fill="both", expand=True)

    chat_area = scrolledtext.ScrolledText(
        chat_frame,
        wrap=tk.WORD,
        bg=tema.FUNDO_CONVERSA,
        fg=tema.TEXTO,
        insertbackground=tema.TEXTO,
        font=(tema.FONTE, 10),
        bd=0,
        highlightbackground=tema.BORDA,
        highlightthickness=1,
        padx=14,
        pady=14,
    )
    chat_area.pack(fill="both", expand=True)

    chat_area.tag_config("user", foreground=tema.ROXO_SUAVE, font=(tema.FONTE, 10, "bold"), justify="right")
    chat_area.tag_config("gotoh", foreground=tema.ROXO_CLARO, font=(tema.FONTE, 10, "bold"), justify="left")
    chat_area.tag_config("text_user", foreground=tema.TEXTO_USUARIO, justify="right")
    chat_area.tag_config("text_gotoh", foreground=tema.TEXTO_GOTOH, justify="left")

    def carregar_historico():
        chat_area.config(state=tk.NORMAL)
        chat_area.delete("1.0", tk.END)
        try:
            historico = memoria_db.obter_historico_recente(limite=30)
        except Exception:
            historico = []

        if not historico:
            chat_area.insert(tk.END, "Gotoh\n", "gotoh")
            chat_area.insert(
                tk.END,
                "Olá! Estou pronto. Você pode me pedir para guardar informações, criar tarefas ou consultar suas memórias.\n\n",
                "text_gotoh",
            )
        else:
            for rem, msg in historico:
                if rem == "user":
                    chat_area.insert(tk.END, "Você\n", "user")
                    chat_area.insert(tk.END, f"{msg}\n\n", "text_user")
                else:
                    chat_area.insert(tk.END, "Gotoh\n", "gotoh")
                    chat_area.insert(tk.END, f"{msg}\n\n", "text_gotoh")

        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)

    carregar_historico()

    def processar_resposta(texto_usuario):
        try:
            memoria_db.salvar_mensagem("user", texto_usuario)
        except Exception:
            pass

        try:
            if processar_comando:
                resposta = processar_comando(texto_usuario)
            else:
                resposta = "Módulo de agente (sistema.agente) não pôde ser carregado."

            if not resposta:
                resposta = "Não recebi nenhuma resposta do modelo local."
        except Exception as e:
            resposta = f"Ocorreu um erro ao processar a mensagem: {e}"

        try:
            memoria_db.salvar_mensagem("gotoh", resposta)
        except Exception:
            pass

        def atualizar_ui():
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, "Gotoh\n", "gotoh")
            chat_area.insert(tk.END, f"{resposta}\n\n", "text_gotoh")
            chat_area.config(state=tk.DISABLED)
            chat_area.see(tk.END)
            status_label.config(text="● Memória Ativa", fg=tema.VERDE)

        conteudo.after(0, atualizar_ui)

    def enviar():
        txt = entry_msg.get().strip()
        if not txt:
            return
        entry_msg.delete(0, tk.END)

        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Você\n", "user")
        chat_area.insert(tk.END, f"{txt}\n\n", "text_user")
        chat_area.config(state=tk.DISABLED)
        chat_area.see(tk.END)

        status_label.config(text="⏳ Gotoh está pensando...", fg="#F59E0B")

        threading.Thread(target=processar_resposta, args=(txt,), daemon=True).start()

    btn_enviar.config(command=enviar)
    entry_msg.bind("<Return>", lambda event: enviar())

    def ouvir_voz():
        if voz and hasattr(voz, "ouvir"):
            status_label.config(text="🎙️ Ouvindo...", fg="#F59E0B")
            texto_ouvido = voz.ouvir()
            status_label.config(text="● Memória Ativa", fg=tema.VERDE)
            if texto_ouvido:
                entry_msg.delete(0, tk.END)
                entry_msg.insert(0, texto_ouvido)
                enviar()
        else:
            status_label.config(text="⚠️ Módulo de voz indisponível", fg=tema.VERMELHO)

    btn_voz.config(command=lambda: threading.Thread(target=ouvir_voz, daemon=True).start())
