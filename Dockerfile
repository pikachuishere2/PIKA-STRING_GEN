FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    libopencv-dev \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Verify Python and pip versions
RUN python3 --version && pip3 --version

# Check network connectivity
RUN ping -c 4 pypi.org
RUN curl -sSL https://github.com

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt --verbose

COPY . .
CMD ["python3", "bash" ,"start"]
