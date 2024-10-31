from flask import Flask, render_template, send_file
import json
import imgkit
import os
import sys
from io import BytesIO

app = Flask(__name__)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    return '444'

@app.route('/imgbox-cdn/lol/<string:filename>')
def render_image(filename):
    data = load_data()  # Чтение данных из JSON-файла
    
    print(json.dumps(data, ensure_ascii=False, indent=4), file=sys.stderr)
    template_path = os.path.join('templates', 'page_template.html')  # Путь к шаблону в папке templates
    # Проверка существования файла шаблона
    if os.path.exists(template_path):
        print(f"Шаблон найден: {template_path}", file=sys.stderr)
    else:
        print(f"Шаблон не найден: {template_path}", file=sys.stderr)
        
    html_output = render_template('page_template.html', data=data)
    
    # Создаем изображение в памяти
    img = imgkit.from_string(html_output, False, 
        options={
            'format': 'png',      # Убедитесь, что формат установлен на png
            'quality': '100',     # Максимальное качество
            'no-stop-slow-scripts': '',  # Отключение остановки медленных скриптов
            'disable-smart-width': '',     # Отключение "умной ширины"
            'width': '700',    # Установите верхний отступ в 0
            'margin-right': '0',  # Установите правый отступ в 0
            'margin-bottom': '0', # Установите нижний отступ в 0
            'margin-left': '0'    # Установите левый отступ в 0
        })  # Используем False для возврата изображения в виде байтов
    
    return send_file(BytesIO(img), mimetype='image/png', as_attachment=True, download_name='output_image.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
