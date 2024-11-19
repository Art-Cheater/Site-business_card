from flask import Flask, jsonify
from flask_cors import CORS  # Импортируем CORS
import sqlite3

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


if __name__ == '__main__':
    app.run(debug=True)
