# Projeto stock insights

API em Python com AWS Lambda que retorna o histórico de preços e dados básicos de ações da B3, utilizando `yfinance` e a API pública do Brapi.

---

## 📁 Estrutura do Projeto

```
- requirements.txt
- .gitignore
- README.md
- serverless.yml
- .vscode/
  - launch.json
- functions/
  - stock_analysis.py
```

---

## 🚀 Funcionalidade

A função `fetch_stock_data` exposta via API retorna:
- Preço histórico (últimos 5 anos)
- Informações básicas da ação (via brapi.dev)

---

## ✅ Requisitos

- Python 3.11
- `pip install -r requirements.txt`
- Token de acesso à API Brapi (opcional para alguns dados)

---

## 🛠 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/stock-insights-api.git
cd stock-insights-api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute localmente com o Serverless Framework:
```bash
sls offline
```
