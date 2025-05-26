# 💜 Amora_Imovel 🏡💻

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Sobre o Projeto

**Amora_Imovel** é uma aplicação web voltada para simulação de financiamento imobiliário.  
Com base no valor do imóvel, percentual de entrada e tempo de contrato, o sistema calcula automaticamente:

- 💰 Valor da entrada  
- 🏦 Valor financiado  
- 📊 Total a guardar  
- 📆 Parcela mensal ideal

Backend robusto com **FastAPI** e frontend leve e moderno com **React**.

---

## 🛠️ Tecnologias Utilizadas

### 🔙 Backend
- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **Uvicorn**

### 🔜 Frontend
- **React**
- **Vite**
- **JavaScript/TypeScript**

---

## 🚀 Como Rodar o Projeto

### ⚙️ Backend

```bash
# 1. Acesse a pasta do backend
cd backend

# 2. Crie e ative o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode o servidor
python main.py

A API estará disponível em: http://localhost:8000

```
```bash
# 1. Acesse a pasta do frontend
cd frontend

# 2. Instale as dependências
npm install

# 3. Inicie o servidor de desenvolvimento
npm run dev
A interface estará acessível em: http://localhost:5173
```
