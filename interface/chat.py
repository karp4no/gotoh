import tkinter as tk
from tkinter import ttk
import webbrowser
import re
import math
import interface.tema as tema
from sistema.agente import processar_comando
from sistema.voz import voz

class ChatFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=tema.FUNDO_CONVERSA)
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Header com Esfera Pulsante
        header_frame = tk.Frame(self, bg=tema.FUNDO_CONVERSA, height=60)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(5, 5))
        header_frame.grid_columnconfigure(1, weight=1)

        self.canvas_orb = tk.Canvas(header_frame, width=50, height=50, bg=tema.FUNDO_CONVERSA, highlightthickness=0)
        self.canvas_orb.grid(row=0, column=0, padx=10)

        self.lbl_status = tk.Label(
            header_frame,
            text="GOTOH // SISTEMA ATIVO",
            font=(tema.FONTE, 9, "bold"),
            fg=tema.ROXO_SUAVE,
            bg=tema.FUNDO_CONVERSA
        )
        self.lbl_status.grid(row=0, column=1, sticky="w")

        self.orb_angle = 0
        self.is_thinking = False
        self._animar_orb()

        # Área de Mensagens
        main_container = tk.Frame(self, bg=tema.FUNDO_CONVERSA)
        main_container.grid(row=1, column=0, sticky="nsew")
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        self.text_area = tk.Text(
            main_container,
            wrap="word",
            state="disabled",
            bg=tema.FUNDO_CONVERSA,
            fg=tema.TEXTO,
            insertbackground="white",
            font=(tema.FONTE, 10),
            padx=15,
            pady=15,
            bd=0
        )
        self.text_area.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(main_container, command=self.text_area.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_area["yscrollcommand"] = scrollbar.set

        # Tags
        self.text_area.tag_config("user_tag", foreground=tema.VERDE, font=(tema.FONTE, 10, "bold"), justify="right")
        self.text_area.tag_config("user_msg", foreground=tema.TEXTO_USUARIO, font=(tema.FONTE, 10), justify="right")
        self.text_area.tag_config("gotoh_tag", foreground=tema.ROXO_SUAVE, font=(tema.FONTE, 10, "bold"), justify="left")
        self.text_area.tag_config("gotoh_msg", foreground=tema.TEXTO_GOTOH, font=(tema.FONTE, 10), justify="left")

        self.text_area.bind("<Motion>", self._on_mouse_move)
        self.text_area.bind("<Button-1>", self._on_mouse_click)

        # Entrada & Chips
        input_container = tk.Frame(self, bg=tema.FUNDO_CONVERSA)
        input_container.grid(row=2, column=0, sticky="ew", pady=(5, 0))
        input_container.grid_columnconfigure(0, weight=1)

        chips_frame = tk.Frame(input_container, bg=tema.FUNDO_CONVERSA)
        chips_frame.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 8))

        self._criar_chip(chips_frame, "📋 Tarefas", "Quais são as minhas tarefas cadastradas?")
        self._criar_chip(chips_frame, "📚 Dica de Estudos", "Me dê uma dica rápida de como organizar meus estudos hoje.")
        self._criar_chip(chips_frame, "🌐 Pesquisar", "pesquise sobre ")
        self.btn_voz_toggle = self._criar_chip(chips_frame, "🔇 Voz: OFF", comando_especial="toggle_voz")
        self._criar_chip(chips_frame, "🧹 Limpar", comando_especial="limpar")

        input_frame = tk.Frame(input_container, bg=tema.FUNDO_CONVERSA)
        input_frame.grid(row=1, column=0, sticky="ew")
        input_frame.grid_columnconfigure(0, weight=1)

        self.entry_msg = tk.Entry(
            input_frame,
            bg=tema.FUNDO_INPUT,
            fg=tema.TEXTO,
            insertbackground="white",
            font=(tema.FONTE, 10),
            bd=1,
            relief="solid"
        )
        self.entry_msg.grid(row=0, column=0, sticky="ew", ipady=8, padx=(0, 10))
        self.entry_msg.bind("<Return>", lambda e: self.enviar_mensagem())

        self.btn_enviar = tk.Button(
            input_frame,
            text="Enviar",
            bg=tema.ROXO,
            fg=tema.TEXTO,
            font=(tema.FONTE, 10, "bold"),
            activebackground=tema.ROXO_CLARO,
            activeforeground=tema.TEXTO,
            bd=0,
            cursor="hand2",
            command=self.enviar_mensagem
        )
        self.btn_enviar.grid(row=0, column=1, ipadx=20, ipady=6)

        self.exibir_saudacao_inicial()

    def _animar_orb(self):
        self.canvas_orb.delete("all")
        cx, cy = 25, 25
        fator_pulsacao = 6 if self.is_thinking else 2
        raio_base = 14 + math.sin(self.orb_angle) * fator_pulsacao
        
        self.canvas_orb.create_oval(
            cx - raio_base - 4, cy - raio_base - 4,
            cx + raio_base + 4, cy + raio_base + 4,
            outline="#4d2a7a", width=1
        )
        
        cor_central = tema.AZUL if self.is_thinking else tema.ROXO
        self.canvas_orb.create_oval(
            cx - raio_base, cy - raio_base,
            cx + raio_base, cy + raio_base,
            fill=cor_central, outline=tema.ROXO_CLARO, width=2
        )
        
        self.orb_angle += 0.15 if self.is_thinking else 0.05
        self.after(50, self._animar_orb)

    def _criar_chip(self, parent, texto, prompt_texto="", comando_especial=None):
        def acao():
            if comando_especial == "limpar":
                self.limpar_chat()
            elif comando_especial == "toggle_voz":
                voz.enabled = not voz.enabled
                novo_texto = "🔊 Voz: ON" if voz.enabled else "🔇 Voz: OFF"
                btn.config(text=novo_texto)
            elif prompt_texto.endswith(" "):
                self.entry_msg.delete(0, tk.END)
                self.entry_msg.insert(0, prompt_texto)
                self.entry_msg.focus()
            else:
                self.entry_msg.delete(0, tk.END)
                self.entry_msg.insert(0, prompt_texto)
                self.enviar_mensagem()

        btn = tk.Button(
            parent,
            text=texto,
            command=acao,
            font=(tema.FONTE, 8, "bold"),
            fg=tema.TEXTO_SECUNDARIO,
            bg=tema.FUNDO_SECUNDARIO,
            activeforeground=tema.TEXTO,
            activebackground=tema.FUNDO_CARD_HOVER,
            bd=0,
            cursor="hand2",
            padx=10,
            pady=4
        )
        btn.pack(side="left", padx=(0, 6))
        return btn

    def _on_mouse_move(self, event):
        try:
            index = self.text_area.index(f"@{event.x},{event.y}")
            tags = self.text_area.tag_names(index)
            if any(t.startswith("link_") for t in tags):
                self.text_area.config(cursor="hand2")
            else:
                self.text_area.config(cursor="xterm")
        except tk.TclError:
            pass

    def _on_mouse_click(self, event):
        try:
            index = self.text_area.index(f"@{event.x},{event.y}")
            tags = self.text_area.tag_names(index)
            for tag in tags:
                if tag.startswith("link_"):
                    ranges = self.text_area.tag_ranges(tag)
                    if ranges:
                        url = self.text_area.get(ranges[0], ranges[1]).strip().rstrip(").,*'\"")
                        if url.startswith("http://") or url.startswith("https://"):
                            webbrowser.open_new_tab(url)
                            return "break"
        except tk.TclError:
            pass

    def exibir_saudacao_inicial(self):
        saudacao = "Olá! Como posso ajudar você hoje? Podemos revisar tarefas, continuar os estudos ou realizar alguma pesquisa."
        self.exibir_mensagem_gotoh(saudacao)

    def limpar_chat(self):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.config(state="disabled")
        self.exibir_saudacao_inicial()

    def enviar_mensagem(self):
        msg = self.entry_msg.get().strip()
        if not msg:
            return

        self.exibir_mensagem_usuario(msg)
        self.entry_msg.delete(0, tk.END)

        # Atualiza status e força a interface a atualizar antes de processar
        self.is_thinking = True
        self.lbl_status.config(text="GOTOH // PESQUISANDO...")
        self.update_idletasks()

        # Processamento direto sem bloqueios
        resposta = processar_comando(msg)

        # Exibe o resultado imediatamente
        self.exibir_mensagem_gotoh(resposta)
        self.lbl_status.config(text="GOTOH // SISTEMA ATIVO")
        self.is_thinking = False

        # Tenta a voz se estiver ligada, mas sem impedir a exibição da tela
        if voz.enabled:
            voz.falar(resposta)

    def exibir_mensagem_usuario(self, texto: str):
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, "Você\n", "user_tag")
        self.text_area.insert(tk.END, f"{texto}\n\n", "user_msg")
        self.text_area.see(tk.END)
        self.text_area.config(state="disabled")

    def exibir_mensagem_gotoh(self, texto: str):
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, "Gotoh\n", "gotoh_tag")
        
        pattern = r'(https?://[^\s()<>]+(?:\([\w\d]+\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
        
        pos_atual = 0
        for match in re.finditer(pattern, texto):
            start, end = match.span()
            if start > pos_atual:
                self.text_area.insert(tk.END, texto[pos_atual:start], "gotoh_msg")
            
            url = match.group(0)
            tag_id = f"link_{self.text_area.index(tk.END).replace('.', '_')}"
            
            self.text_area.tag_config(tag_id, foreground=tema.AZUL, underline=True, justify="left")
            self.text_area.insert(tk.END, url, (tag_id, "gotoh_msg"))
            
            pos_atual = end

        if pos_atual < len(texto):
            self.text_area.insert(tk.END, texto[pos_atual:], "gotoh_msg")

        self.text_area.insert(tk.END, "\n\n")
        self.text_area.see(tk.END)
        self.text_area.config(state="disabled")
