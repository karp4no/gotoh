import requests
import urllib.parse

def buscar_web(termo: str, max_resultados: int = 3) -> list:
    """
    Realiza busca resiliente combinando Wikipedia API e DuckDuckGo Direct API.
    """
    resultados = []
    headers = {
        "User-Agent": "GotohAssistant/1.0 (https://github.com/gotoh-agent)"
    }

    # 1. Busca na Wikipedia em Português
    try:
        wiki_url = f"https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(termo)}&format=json&utf8=1"
        res_wiki = requests.get(wiki_url, headers=headers, timeout=5).json()
        search_items = res_wiki.get("query", {}).get("search", [])

        for item in search_items[:max_resultados]:
            title = item.get("title", "")
            # Limpa tags HTML simples que a Wikipedia retorna no snippet (ex: <span class="searchmatch">)
            snippet = item.get("snippet", "").replace('<span class="searchmatch">', '').replace('</span>', '')
            link = f"https://pt.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"
            
            resultados.append({
                "titulo": title,
                "snippet": snippet + "...",
                "link": link
            })
    except Exception as e:
        print(f"Erro na busca Wikipedia: {e}")

    # 2. Fallback via DuckDuckGo Instant Answer API se a Wikipedia não retornar nada
    if not resultados:
        try:
            ddg_url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(termo)}&format=json&kl=br-pt"
            res_ddg = requests.get(ddg_url, headers=headers, timeout=5).json()
            
            if res_ddg.get("AbstractText"):
                resultados.append({
                    "titulo": res_ddg.get("Heading", termo),
                    "snippet": res_ddg.get("AbstractText"),
                    "link": res_ddg.get("AbstractURL", "")
                })
            elif res_ddg.get("RelatedTopics"):
                for topic in res_ddg["RelatedTopics"][:max_resultados]:
                    if "Text" in topic and "FirstURL" in topic:
                        resultados.append({
                            "titulo": termo.capitalize(),
                            "snippet": topic.get("Text"),
                            "link": topic.get("FirstURL")
                        })
        except Exception as e:
            print(f"Erro na busca DDG: {e}")

    return resultados


def formatar_resultados_web(termo: str, resultados: list) -> str:
    if not resultados:
        return f"🌐 Não encontrei registros relevantes na internet para **'{termo}'**."

    texto = f"🌐 **Pesquisa Web para:** '{termo}'\n\n"
    for i, r in enumerate(resultados, 1):
        texto += f"**{i}. {r['titulo']}**\n"
        texto += f"   • {r['snippet']}\n"
        if r['link']:
            texto += f"   🔗 {r['link']}\n"
        texto += "\n"
    return texto.strip()
