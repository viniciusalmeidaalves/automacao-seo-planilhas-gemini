# Automação de SEO para Planilhas com Google Gemini

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
<img width="1365" height="727" alt="image" src="https://github.com/user-attachments/assets/34c8fff9-403c-4dba-b4ed-8a607c215b85" />

Planilha para realização de SEO em 827 produtos
<img width="1280" height="985" alt="image" src="https://github.com/user-attachments/assets/528e3925-fca8-412a-8481-e958a97b43b6" />

## Tecnologias
- Linguagem de Programação: Python

- Principal Biblioteca de IA: Google Generative AI (google-generativeai)

- Manipulação de Dados: Pandas

- Interação com Excel: OpenPyXL

- Ambiente Virtual: venv

- API Externa: Google Gemini API

