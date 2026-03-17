import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import re
import html
import csv # Import necessário para o salvamento blindado

def coletor_unicamp_definitivo():
    url_api = "https://tecnologias.inova.unicamp.br/wp-json/wp/v2/tecnologia"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    todas_tecnologias = []
    page = 1
    
    print("📡 Fase 1: Coletando lista completa via API...")
    while True:
        params = {'per_page': 100, 'page': page}
        try:
            res = requests.get(url_api, headers=headers, params=params, timeout=15)
            if res.status_code != 200: break
            dados = res.json()
            if not dados: break
            
            for item in dados:
                todas_tecnologias.append({
                    'titulo': item.get('title', {}).get('rendered'),
                    'link': item.get('link'),
                    'data': item.get('date'),
                    'descricao_bruta': item.get('content', {}).get('rendered', '')
                })
            print(f"✅ Página {page} capturada...")
            page += 1
        except: break

    print(f"\n🔍 Fase 2: Extraindo texto limpo (ignorando códigos)...")
    
    for i, item in enumerate(todas_tecnologias):
        # Se a descrição da API está suja ou vazia, buscamos o texto limpo no site
        if not item['descricao_bruta'] or "[" in item['descricao_bruta']:
            try:
                r_web = requests.get(item['link'], headers=headers, timeout=10)
                soup = BeautifulSoup(r_web.text, 'html.parser')
                # O BeautifulSoup ignora as tags e pega só o texto
                conteudo = soup.find('div', class_='entry-content') or soup.find('article')
                texto_recuperado = conteudo.get_text(separator=' ') if conteudo else ""
                time.sleep(0.1) 
            except:
                texto_recuperado = ""
        else:
            # Se vier da API, passamos pelo BeautifulSoup para remover tags HTML
            texto_recuperado = BeautifulSoup(item['descricao_bruta'], 'html.parser').get_text(separator=' ')

        # LIMPEZA DE CÓDIGOS (Ignorando Shortcodes do WordPress e Quebras de Linha)
        texto_limpo = html.unescape(str(texto_recuperado))
        # Remove códigos tipo [vc_row]
        texto_limpo = re.sub(r'\[/?vc_.*?\]', ' ', texto_limpo)
        # Remove qualquer tag HTML que tenha sobrado
        texto_limpo = re.sub(r'<[^>]+>', ' ', texto_limpo)
        # IMPORTANTE: Transforma quebras de linha em espaços para não quebrar o Excel
        texto_limpo = re.sub(r'[\n\r\t]+', ' ', texto_limpo)
        # Remove espaços duplos
        texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()
        
        item['descricao_final'] = texto_limpo
        if (i+1) % 50 == 0: print(f"⏳ Processados {i+1} itens...")

    # Salvamento final - Usando quoting para proteger o texto
    df = pd.DataFrame(todas_tecnologias)
    df.to_csv('vitrine_unicamp_FINAL_TOTAL.csv', index=False, encoding='utf-8-sig', quoting=csv.QUOTE_ALL)
    print(f"\n🏆 PROCESSO CONCLUÍDO! Arquivo 'vitrine_unicamp_FINAL_TOTAL.csv' gerado corretamente.")

def lapidacao_cirurgica(arquivo_entrada):
    # Lendo com tratamento de erro para garantir que o CSV seja bem interpretado
    df = pd.read_csv(arquivo_entrada, quoting=csv.QUOTE_ALL)
    df = df.drop_duplicates(subset=['link'])

    termos_fortes = ['algoritmo', 'inteligência artificial', 'machine learning', 
                     'aplicativo móvel', 'interface gráfica', 'banco de dados', 
                     'sistema supervisório', 'plataforma digital', 'software de']

    def marcar_ti_real(row):
        titulo = str(row['titulo']).lower()
        descricao = str(row['descricao_final']).lower()
        if titulo.startswith('pc') or any(t in titulo for t in ['software', 'programa']):
            return "SIM"
        if any(t in descricao for t in termos_fortes):
            return "SIM"
        return "NÃO"

    df['Eh_Software_TI'] = df.apply(marcar_ti_real, axis=1)
    df_ti = df[df['Eh_Software_TI'] == "SIM"]
    
    # Salvamento blindado para Excel não separar as linhas
    df.to_csv('BASE_UNICAMP_COMPLETA_CLASSIFICADA.csv', index=False, encoding='utf-8-sig', quoting=csv.QUOTE_ALL)
    df_ti.to_csv('BASE_UNICAMP_SOMENTE_TI.csv', index=False, encoding='utf-8-sig', quoting=csv.QUOTE_ALL)
    
    print(f"🎯 Sucesso! 'BASE_UNICAMP_SOMENTE_TI.csv' gerado com {len(df_ti)} itens.")

if __name__ == "__main__":
    coletor_unicamp_definitivo()
    lapidacao_cirurgica('vitrine_unicamp_FINAL_TOTAL.csv')
