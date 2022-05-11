from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient('mongodb+srv://test:sparta@cluster0.lovi7.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fork')
def fork():
    return render_template('fork.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)