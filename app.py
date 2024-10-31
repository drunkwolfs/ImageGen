from flask import Flask, render_template, send_file
import json
import imgkit
import os
from io import BytesIO

app = Flask(__name__)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    data = load_data()  # Чтение данных из JSON-файла
    return render_template('table_template.html', data=data)

@app.route('/render-image')
def render_image():
    data = load_data()  # Чтение данных из JSON-файла
    html_output = render_template('table_template.html', data=data)
    
    # Создаем изображение в памяти
    img = imgkit.from_string(html_output, False)  # Используем False для возврата изображения в виде байтов
    
    return send_file(BytesIO(img), mimetype='image/png', as_attachment=True, download_name='output_image.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
