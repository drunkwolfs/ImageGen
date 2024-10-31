# Используем базовый образ с Python и wkhtmltopdf
FROM mkubenka/python-wkhtmltopdf

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
