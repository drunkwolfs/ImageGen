from flask import Flask, request, jsonify
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/get_image', methods=['GET'])
def get_image():
    # Получаем параметр image из GET-запроса
    image_base64 = request.args.get('image')
    
    if not image_base64:
        return jsonify({"error": "Parameter 'image' is required"}), 400
    
    try:
        # Декодируем base64 строку и открываем изображение
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        
        # Конвертируем изображение обратно в base64 для HTML
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        # Создаём data URI для использования в HTML <img src="...">
        img_data_uri = f"data:image/png;base64,{img_base64}"
        
        # Возвращаем data URI в ответе JSON
        return jsonify({"image_data_uri": img_data_uri})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
