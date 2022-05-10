from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

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