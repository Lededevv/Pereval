FROM python:3.13-alpine
RUN addgroup -S groupdjang && adduser -S -G groupdjang userdj
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /app/www/pereval
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
USER userdj