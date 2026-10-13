import urllib.parse
import urllib.request
import json
import re
from memory_manager import GotohMemory

def pesquisar_web(termo):
    try:
        url = f"https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(termo)}&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'GotohBot/1.0'})
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            resultados = data.get('query', {}).get('search', [])
            if resultados:
                snippet = re.sub(r'<[^>]+>', '', resultados[0].get('snippet', ''))
                return f"**{resultados[0].get('title')}**: {snippet}..."
    except Exception:
        pass
    return None

def processar_comando(texto_usuario):
    db = GotohMemory()
    db.salvar_mensagem("usuario", texto_usuario)
    
    texto_lc = texto_usuario.lower()
    fatos = db.obter_fatos()

    # Resposta baseada em memória registrada
    for chave, valor in fatos.items():
        if chave in texto_lc:
            resposta = f"Sobre {chave}: {valor}"
            db.salvar_mensagem("gotoh", resposta)
            return resposta

    # Consulta rápida na web se necessário
    if any(p in texto_lc for p in ["pesquise", "quem foi", "o que é", "fale sobre"]):
        termo = re.sub(r'pesquise|quem foi|o que é|fale sobre', '', texto_lc).strip()
        web_res = pesquisar_web(termo)
        if web_res:
            db.salvar_mensagem("gotoh", web_res)
            return web_res

    resposta = f"Compreendido. Salvando contexto para: '{texto_usuario}'."
    db.salvar_mensagem("gotoh", resposta)
    return resposta
