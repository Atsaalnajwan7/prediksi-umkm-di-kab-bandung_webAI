from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

# --- DATA DUMMY ---
X = np.array([[2020], [2021], [2022], [2023], [2024]])
y = np.array([1000, 1100, 1250, 1320, 1450])

# --- TRAIN MODEL ---
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    if request.method == 'POST':
        tahun_input = request.form.get('tahun')
        if tahun_input:
            try:
                tahun = float(tahun_input)
                prediksi = model.predict([[tahun]])
                hasil = round(float(prediksi[0]), 2)
            except Exception as e:
                hasil = f"Error: {str(e)}"
    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    # PAKSA menggunakan host 0.0.0.0 dan PORT dari Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)