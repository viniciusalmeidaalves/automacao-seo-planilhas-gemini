# Importa as bibliotecas necessárias
import pandas as pd
import google.generativeai as genai
import time

# --- CONFIGURAÇÃO ---
# Coloque a sua Chave de API do Google aqui
GOOGLE_API_KEY = 'AIzaSyAyR3sIlE0mQaiMfVZqhH-XBRsXE7uuWvA'

# Nomes dos arquivos
ARQUIVO_EXCEL_ENTRADA = 'SEO (Search Engine Optimization) RJE Iluminacao.xlsx'
ARQUIVO_EXCEL_SAIDA = 'SEO (Search Engine Optimization) Resultados_preenchidos.xlsx'

# Nomes das colunas na sua planilha
COLUNA_PRODUTO = 'Nome produto'
COLUNA_DESCRICAO_HTML = 'Descrição grande'
COLUNA_SEO_TITULO = 'SEO Título'
COLUNA_SEO_DESC_SIMPLES = 'SEO descrição simplificada'
COLUNA_SEO_PALAVRA_CHAVE = 'SEO palavra chave'

# --- FIM DA CONFIGURAÇÃO ---


# Configura o modelo do Gemini com sua chave
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-pro')

def gerar_seo_com_gemini(nome_produto, descricao_html):
    """
    Envia o prompt para a API do Gemini e extrai os resultados.
    """
    # Este prompt instrui a IA a retornar os dados em um formato fácil de processar
    prompt = f"""
    A partir do nome do produto e da descrição em HTML abaixo, gere o seguinte conteúdo de SEO:

    1.  **SEO Título**: Um título otimizado para buscadores.
    2.  **SEO Descrição Simplificada**: Uma descrição curta e comercial.
    3.  **SEO Palavras-Chave**: Uma lista de palavras-chave relevantes, separadas por vírgula.

    Responda APENAS com o conteúdo solicitado, usando o seguinte formato de separadores:
    <TITULO>CONTEÚDO DO TÍTULO</TITULO>
    <DESC>CONTEÚDO DA DESCRIÇÃO</DESC>
    <CHAVES>CONTEÚDO DAS PALAVRAS-CHAVE</CHAVES>

    **Produto:** [{nome_produto}]
    **Descrição:** [{descricao_html}]
    """
    
    try:
        print(f"Processando produto: {nome_produto}...")
        response = model.generate_content(prompt)
        
        # Extrai o conteúdo usando os separadores definidos
        texto_resposta = response.text
        titulo = texto_resposta.split('<TITULO>')[1].split('</TITULO>')[0].strip()
        descricao = texto_resposta.split('<DESC>')[1].split('</DESC>')[0].strip()
        palavras_chave = texto_resposta.split('<CHAVES>')[1].split('</CHAVES>')[0].strip()
        
        print(" -> Sucesso!")
        return titulo, descricao, palavras_chave

    except Exception as e:
        print(f" -> ERRO ao processar '{nome_produto}': {e}")
        return "ERRO", "ERRO", "ERRO"


# Carrega a planilha do Excel
df = pd.read_excel(ARQUIVO_EXCEL_ENTRADA, sheet_name='SEO_Otimizado')

# Itera sobre cada linha da planilha
for index, row in df.iterrows():
    # Verifica se a coluna "SEO Título" já está preenchida
    # Se estiver (e não for um erro), pula para a próxima linha
    if pd.notna(row[COLUNA_SEO_TITULO]) and row[COLUNA_SEO_TITULO] != "ERRO":
        print(f"Já preenchido para: {row[COLUNA_PRODUTO]}. Pulando.")
        continue

    # Pega os dados das colunas B e C
    produto = row[COLUNA_PRODUTO]
    descricao_html = row[COLUNA_DESCRICAO_HTML]

    # Gera o conteúdo de SEO usando a função do Gemini
    seo_titulo, seo_desc_simples, seo_palavras_chave = gerar_seo_com_gemini(produto, descricao_html)

    # Coloca os resultados de volta na planilha (no DataFrame)
    df.loc[index, COLUNA_SEO_TITULO] = seo_titulo
    df.loc[index, COLUNA_SEO_DESC_SIMPLES] = seo_desc_simples
    df.loc[index, COLUNA_SEO_PALAVRA_CHAVE] = seo_palavras_chave

    # Pausa de 3 segundos para não sobrecarregar a API
    time.sleep(3)

# Salva o DataFrame modificado em um novo arquivo Excel
df.to_excel(ARQUIVO_EXCEL_SAIDA, index=False)

print(f"\n✅ Processo concluído! Os resultados foram salvos em '{ARQUIVO_EXCEL_SAIDA}'")