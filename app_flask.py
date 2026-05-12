from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import sqlite3
from datetime import datetime

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

cut_order     = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_order   = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
clarity_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

# Veritabanını oluştur
def init_db():
    conn = sqlite3.connect('tahminler.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tahminler (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            tarih     TEXT,
            carat     REAL,
            cut       TEXT,
            color     TEXT,
            clarity   TEXT,
            depth     REAL,
            table_    REAL,
            fiyat     REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    carat   = data['carat']
    cut     = cut_order.index(data['cut'])
    color   = color_order.index(data['color'])
    clarity = clarity_order.index(data['clarity'])
    depth   = data['depth']
    table   = data['table']

    features = np.array([[carat, cut, color, clarity, depth, table]])
    tahmin   = model.predict(features)[0]
    tahmin   = round(float(tahmin), 2)

    # Veritabanına kaydet
    conn = sqlite3.connect('tahminler.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tahminler (tarih, carat, cut, color, clarity, depth, table_, fiyat)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        data['carat'], data['cut'], data['color'],
        data['clarity'], data['depth'], data['table'], tahmin
    ))
    conn.commit()
    conn.close()

    return jsonify({'tahmin': tahmin})

@app.route('/gecmis')
def gecmis():
    return render_template('gecmis.html')

@app.route('/api/gecmis')
def gecmis_api():
    conn = sqlite3.connect('tahminler.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tahminler ORDER BY id DESC LIMIT 20')
    kayitlar = cursor.fetchall()
    conn.close()
    return jsonify(kayitlar)

if __name__ == '__main__':
    app.run(debug=True)
