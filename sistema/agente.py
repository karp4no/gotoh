import re
import json
import urllib.parse
import urllib.request
import sqlite3
from memory_manager import GotohMemory

def montar_contexto_sistema():
    fatos_dict = {}
    try:
        conn = sqlite3.connect('gotoh_memory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT chave, valor FROM fatos_usuario")
        for k, v in cursor.fetchall():
            fatos_dict[str(k).strip().lower()] = str(v).strip()
        conn.close()
    except Exception:
        pass
    return fatos_dict

def buscar_wikipedia_search(termo):
    try:
        url_search = f"https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(termo)}&format=json"
        req = urllib.request.Request(url_search, headers={'User-Agent': 'GotohBot/1.0'})
        
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            search_results = data.get('query', {}).get('search', [])
            
        if not search_results:
            return None

        resumos = []
        for item in search_results[:2]:
            titulo = item.get('title', '')
            snippet = item.get('snippet', '')
            snippet_limpo = re.sub(r'<[^>]+>', '', snippet)
            resumos.append(f"• **{titulo}**: {snippet_limpo}...")

        return "\n".join(resumos)
    except Exception:
        return None

def pesquisar_web_autonomo(termo_bruto):
    termo = termo_bruto.lower()
    expressoes = [
        "fala goto", "goto", "gotoh", "me diz", "me fala", "pesquise sobre",
        "o que voce sabe sobre", "o que você sabe sobre", "qual o", "qual é o",
        "qual", "quais", "me diga", "que foi", "em qual", "meu", "minha"
    ]
    for expr in expressoes:
        termo = termo.replace(expr, "")
    termo = termo.strip()

    if not termo or len(termo) < 3:
        return None

    resultado = buscar_wikipedia_search(termo)
    if resultado:
        return f"Resultados da pesquisa para '{termo}':\n{resultado}"

    return f"Não encontrei resultados claros na web para '{termo}'."

def responder_trecho(trecho, fatos):
    texto_lc = trecho.lower()

    # 1. Checagem de Memória - Idade
    if "idade" in texto_lc or "quantos anos" in texto_lc:
        idade = fatos.get("idade")
        if idade:
            return f"Você tem {idade}."
        return "Sua idade ainda não está registrada na memória."

    # 2. Checagem de Memória - Faculdade / Curso / Estudo
    if any(p in texto_lc for p in ["faculdade", "curso", "estudo", "estuda", "universidade"]):
        curso = fatos.get("curso", fatos.get("formacao_atual", "Ciência da Computação"))
        faculdade = fatos.get("faculdade", fatos.get("universidade", "Cruzeiro do Sul"))
        return f"Você estuda {curso} na instituição {faculdade}."

    # 3. Checagem de Memória - Objetivo
    if "objetivo" in texto_lc and ("voce" in texto_lc or "seu" in texto_lc or "gotoh" in texto_lc):
        obj = fatos.get("objetivo_gotoh", fatos.get("objetivo", "Ser um assistente de IA pessoal autônomo"))
        return f"O objetivo principal é: {obj}."

    # 4. Trava de Perfil Pessoal ("minha", "meu")
    if any(pronome in texto_lc.split() for pronome in ["minha", "meu", "meus", "minhas"]):
        if "mãe" in texto_lc or "mae" in texto_lc:
            mae = fatos.get("nome_mae") or fatos.get("mae")
            if mae:
                return f"O nome da sua mãe é: {mae}."
            return "Essa informação sobre sua mãe ainda não está registrada na minha memória."

        if "pai" in texto_lc:
            pai = fatos.get("nome_pai") or fatos.get("pai")
            if pai:
                return f"O nome do seu pai é: {pai}."
            return "Essa informação sobre seu pai ainda não está registrada na minha memória."

        palavras_frase = set(re.findall(r'\w+', texto_lc))
        for chave, valor in fatos.items():
            if chave in palavras_frase:
                return f"Conforme registrado em sua memória, seu/sua {chave} é: {valor}."

        return "Essa informação sobre você ainda não está registrada na minha memória."

    # 5. Busca Web Autônoma
    web_res = pesquisar_web_autonomo(trecho)
    if web_res:
        return web_res
    
    return f"Não encontrei registros na memória nem na web sobre '{trecho}'."

def processar_comando(texto_usuario):
    db = GotohMemory()
    db.salvar_mensagem("usuario", texto_usuario)
    fatos = montar_contexto_sistema()

    texto_lc = texto_usuario.lower()
    
    if any(pronome in texto_lc.split() for pronome in ["minha", "meu", "meus", "minhas"]) or \
       any(p in texto_lc for p in ["faculdade", "curso", "estudo", "idade", "quantos anos"]):
        resposta_direta = responder_trecho(texto_usuario, fatos)
        db.salvar_mensagem("gotoh", resposta_direta)
        return resposta_direta

    sub_perguntas = re.split(r';|,\s*e\s+|,', texto_usuario, flags=re.IGNORECASE)

    respostas = []
    for parte in sub_perguntas:
        parte_limpa = parte.strip()
        if parte_limpa:
            resp = responder_trecho(parte_limpa, fatos)
            respostas.append(resp)

    resposta_final = "\n\n".join(respostas)
    db.salvar_mensagem("gotoh", resposta_final)
    return resposta_final
