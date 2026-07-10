# Automação de SEO para Planilhas com Google Gemini

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blueviolet)
![Excel](https://img.shields.io/badge/Excel-XLSX-green)
![SEO](https://img.shields.io/badge/SEO-Automation-orange)

Este projeto contém um script Python desenvolvido para automatizar a criação de conteúdo de SEO (Título, Descrição e Palavras-Chave) para uma lista de produtos contida em uma planilha Excel, utilizando a poderosa API do Google Gemini.

## Visão Geral

O objetivo deste script é eliminar o trabalho manual e repetitivo de otimização de SEO para catálogos de produtos, garantindo consistência e qualidade através da inteligência artificial. O script é robusto, projetado para lidar com grandes volumes de dados e continuar o trabalho de onde parou em caso de interrupção.

## Funcionalidades

* **Leitura de Planilha Excel:** Carrega produtos a partir de um arquivo `.xlsx`.
* **Integração com a API Gemini:** Conecta-se à API do Google para gerar conteúdo de SEO de alta qualidade.
* **Inteligência de Continuação:** Se o script for interrompido, ele continuará de onde parou na próxima execução, sem reprocessar itens já concluídos.
* **Coluna de Status:** Adiciona uma coluna "Status" na planilha de saída para um acompanhamento claro do que foi processado com sucesso, o que já existia e o que falhou.
* **Lógica de Retentativa Automática:** Em caso de falhas temporárias na API (como limites de taxa), o script espera e tenta novamente antes de marcar um item como erro.
* **Salvamento Automático:** O progresso é salvo na planilha de saída a cada item processado, evitando perda de dados.

## Como Usar

Siga os passos abaixo para configurar e executar a automação.

### Pré-requisitos

* Python 3.10 ou 3.11 instalado.
* Uma Chave de API do Google Gemini (pode ser obtida no [Google AI Studio](https://aistudio.google.com/app/apikey)).
* Uma conta do Google Cloud com o faturamento habilitado para remover os limites da API.

### Instalação

1.  **Clone ou baixe este repositório:**
    ```bash
    # git clone [https://viniciusalmeidaalves/automacao-seo-planilhas-gemin.git](https://viniciusalmeidaalves/automacao-seo-planilhas-gemin.git)
    # cd (https://viniciusalmeidaalves/automacao-seo-planilhas-gemin)
    ```

2.  **Crie e ative um ambiente virtual:**
    ```powershell
    # Criar o ambiente
    py -3.10 -m venv .venv

    # Ativar o ambiente (Windows PowerShell)
    .\.venv\Scripts\Activate.ps1
    ```

3.  **Instale as dependências:**
    ```powershell
    pip install -r requirements.txt
    ```

### Configuração

1.  **Prepare a Planilha de Entrada:**
    * Coloque seu arquivo Excel na pasta do projeto. O nome padrão esperado é `SEO (Search Engine Optimization) RJE Iluminacao.xlsx`.
    * A planilha deve conter no mínimo as colunas: `Nome produto` e `Descrição grande`.

2.  **Configure o Script:**
    * Abra o arquivo `automacao_seo.py` em um editor de texto.
    * Na seção `--- CONFIGURAÇÃO ---`, insira sua Chave de API na variável `GOOGLE_API_KEY`.
    * Se necessário, ajuste os nomes dos arquivos de entrada e saída e os nomes das colunas.

### Execução

Com o ambiente virtual ativado, execute o script a partir do terminal:
```powershell
python automacao_seo.py
```
O script começará a processar os itens e salvará os resultados no arquivo `SEO (Search Engine Optimization) Resultados_preenchidos.xlsx`.

Execultandos script no visual studio code
```powershell
# Importa as bibliotecas necessárias
import pandas as pd
import google.generativeai as genai
import time

# --- CONFIGURAÇÃO ---
# Coloque a sua Chave de API do Google aqui
GOOGLE_API_KEY = 'CODIGO_DA_API_GOOGLE'

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


print(f"\n Processo concluído! Os resultados foram salvos em '{ARQUIVO_EXCEL_SAIDA}'")
```
Planilha com realização de SEO em 827 produtos

[![Excel](https://img.shields.io/badge/Excel-Planilha%20SEO-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://github.com/user-attachments/files/29897603/SEO.Search.Engine.Optimization.Nome.da.Loja.xlsx)


<img width="1280" height="985" alt="image" src="https://github.com/user-attachments/assets/528e3925-fca8-412a-8481-e958a97b43b6" />

## Tecnologias
- Linguagem de Programação: Python

- Principal Biblioteca de IA: Google Generative AI (google-generativeai)

- Manipulação de Dados: Pandas

- Interação com Excel: OpenPyXL

- Ambiente Virtual: venv

- API Externa: Google Gemini API

