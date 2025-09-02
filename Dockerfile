# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p data uploads temp

# Set environment variables
ENV PYTHONPATH=/app

# Expose port (Railway will set PORT env variable)
EXPOSE $PORT

# Streamlit configuration
RUN mkdir -p ~/.streamlit
RUN echo "[server]" > ~/.streamlit/config.toml && \
    echo "headless = true" >> ~/.streamlit/config.toml && \
    echo "port = \$PORT" >> ~/.streamlit/config.toml && \
    echo "address = \"0.0.0.0\"" >> ~/.streamlit/config.toml

# Run the Streamlit application
CMD streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
