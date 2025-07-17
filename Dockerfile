FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN python3 --version
RUN pip3 --version
RUN ping -c 4 pypi.org
RUN pip3 install --no-cache-dir -U -r requirements.txt
