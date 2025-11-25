# Use Python 3.11 (this forces the version)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Streamlit + PyArrow + GRPC
RUN apt-get update && apt-get install -y \
    gcc g++ build-essential cmake \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port for Streamlit
EXPOSE 10000

# Start Streamlit
CMD ["streamlit", "run", "streamlit-app.py", "--server.port=10000", "--server.address=0.0.0.0"]
