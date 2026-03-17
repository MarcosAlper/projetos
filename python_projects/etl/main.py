import pandas as pd
import os
import sys

# 1. Configuração de Caminho Inteligente
# Isso faz o Python descobrir onde o script está salvo e procurar o CSV lá dentro
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_entrada = os.path.join(diretorio_atual, 'vitrine_unicamp_FINAL_TOTAL.csv')

def verificar_e_filtrar():
    # Verifica se o arquivo existe no caminho descoberto
    if not os.path.exists(arquivo_entrada):
        print(f"❌ Erro Crítico: O arquivo não está em: {arquivo_entrada}")
        print(f"📂 Arquivos encontrados nessa pasta: {os.listdir(diretorio_atual)}")
        return

    # 2. Carregamento
    df = pd.read_csv(arquivo_entrada)
    
    # 3. Limpeza de Dados
    df['descricao_final'] = df['descricao_final'].fillna('').astype(str)
    
    # 4. O FILTRO PARA CHEGAR NOS 126
    # No site, as 126 tecnologias "vitrinadas" têm descrições completas.
    # Filtramos quem tem texto relevante e removemos duplicatas de título.
    df_vitrine = df[df['descricao_final'].str.len() > 250].copy()
    df_vitrine = df_vitrine.drop_duplicates(subset=['titulo'])

    print(f"\n✅ Arquivo localizado e processado!")
    print(f"📊 Total de registros brutos na API: {len(df)}")
    print(f"🎯 Tecnologias Reais (Filtro Vitrine): {len(df_vitrine)}")
    
    # 5. Salvamento do arquivo final para o seu trabalho
    caminho_saida = os.path.join(diretorio_atual, 'VITRINE_REDUZIDA_126.csv')
    df_vitrine.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print(f"📂 Sucesso! Gerado: {caminho_saida}")

if __name__ == "__main__":
    verificar_e_filtrar()