# Используем базовый образ с Python
FROM python:3.9-slim

# Устанавливаем необходимые зависимости для wkhtmltoimage
RUN apt-get update && \
    apt-get install -y wkhtmltopdf && \
    apt-get clean && \
    pip install --upgrade pip

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
