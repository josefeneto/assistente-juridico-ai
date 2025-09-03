FROM python:3.13-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro para aproveitar cache do Docker
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY streamlit_app.py .
COPY utils/ utils/

# Criar diretórios necessários
RUN mkdir -p uploads temp

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Expor porta
EXPOSE 8501

# Comando que evita completamente o problema do config.toml
streamlit run streamlit_app.py
#CMD streamlit run streamlit_app.py --server.port=${PORT:-8501} --server.address=0.0.0.0 --server.headless=true --browser.gatherUsageStats=false