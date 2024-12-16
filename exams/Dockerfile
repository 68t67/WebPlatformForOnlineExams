FROM python:3.11.1-slim

WORKDIR /app

# Копирование файла зависимостей в контейнер
COPY requirements.txt /app/

# Установка зависимостей из requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование всех файлов проекта в контейнер
COPY . /app/

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
