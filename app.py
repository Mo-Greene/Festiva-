from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.diiam.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/festival')
def home():
 r = requests.get("http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api?serviceKey=2%2FK1CdSKKycm%2FIyr1z09L2cFGNZIOO0uBgTNREIj3m8CbuZg5jcGqGzQV%2FhKIbphrEEOOeoxzwyj4vgco6M1bg%3D%3D&pageNo=0&numOfRows=100&type=json")
 response = r.json()
 items = response['response']['body']['items']
 return render_template('index.html', items=items)


if __name__ == '__main__':
 app.run('0.0.0.0', port=5000, debug=True)