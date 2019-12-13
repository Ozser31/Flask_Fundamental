import flask
import requests
import json

from flask import render_template

API_URL='http://localhost:8000'
app = flask.Flask(__name__)

@app.route('/')
def index() :
    stats = requests.get(f'{API_URL}/api/v1/Stats')
    hasil = 'Data belum berhasil diakses'
    if stats.status_code == 200:
        hasil = json.loads(stats.text)
        hasil = len(hasil)
        data = stats.json()
    return render_template('index.html', jumlah_stats=hasil, stats=data )
