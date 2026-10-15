# Automação de SEO para produtos com Google Gemini

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-8E44AD?logo=google&logoColor=white)](https://ai.google.dev/)
[![Excel](https://img.shields.io/badge/Excel-XLSX-217346?logo=microsoftexcel&logoColor=white)](https://support.microsoft.com/office/excel-file-formats-2647e5e5-3f59-4d33-9b5d-5a8f1fbb7c02)
[![SEO](https://img.shields.io/badge/SEO-Automation-F0783C)](#visão-geral)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/compose/)

## Visão geral

Esta aplicação automatiza a preparação de produtos para publicação no site da
**Tudo Natal**. A partir de uma planilha Excel, ela gera:

- descrição completa do produto em HTML;
- título e descrição para mecanismos de busca;
- palavras-chave;
- endereço (URL) do produto.

![Automação de SEO](screenshots/Search%20Engine%20Optimization.png)

O objetivo é reduzir o trabalho manual, padronizar os textos e acelerar o
cadastro dos produtos.

## Fluxo

1. A planilha de produtos é colocada na pasta de entrada.
2. A aplicação identifica os produtos que ainda não têm HTML preenchido.
3. Os textos e dados de SEO são gerados com a API Gemini.
4. Uma nova planilha é salva na pasta de saída.
5. O arquivo gerado é revisado antes da publicação.

## Requisitos

- Docker e Docker Compose;
- acesso à API Gemini;
- chave da API configurada no arquivo `.env`;
- planilha de produtos.

> A chave da API é confidencial. Não a compartilhe nem a adicione à planilha.

## Resultado

Planilha com realização de SEO em 827 produtos:

[SEO.Search.Engine.Optimization.RJE.Iluminacao.xlsx](https://github.com/user-attachments/files/30371966/SEO.Search.Engine.Optimization.RJE.Iluminacao.xlsx)

## Estrutura

```text
.
├── dados/
│   ├── entrada/       # Planilhas originais
│   └── saida/         # Planilhas processadas
├── src/               # Código da automação
├── tests/             # Testes automatizados
├── .env               # Configurações locais e chave da API
├── docker-compose.yml
└── dockerfile
```

## Boas práticas

- Faça uma cópia da planilha original antes de processá-la.
- Revise os textos gerados antes da publicação.
- Não compartilhe a chave `GEMINI_API_KEY`.
