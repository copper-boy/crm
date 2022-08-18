FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt

COPY . .

