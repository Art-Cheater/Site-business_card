from flask import Flask, jsonify
from flask_cors import CORS  # Импортируем CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

# Маршрут для получения всех отзывов
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()

    # Извлекаем все отзывы из базы
    cursor.execute("SELECT id, text FROM reviews")
    rows = cursor.fetchall()
    conn.close()

    # Преобразуем данные в JSON-формат
    reviews = [{"id": row[0], "text": row[1]} for row in rows]
    print(reviews)
    return jsonify(reviews)
@app.route('/')
def home():
    return "API is running. Access the reviews endpoint at /api/reviews"



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Получаем порт из переменных окружения
    app.run(host="0.0.0.0", port=port, debug=True)
