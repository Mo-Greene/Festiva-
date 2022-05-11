from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.sijdl.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

from datetime import datetime

# 저장
@app.route('/review', methods=['POST'])
def comment_post():
    place_receive = request.form['place_give']
    comment_receive = request.form['comment_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        "place": place_receive,
        "comment": comment_receive,
        "file": f'{filename}.{extension}'
        }

    db.festivareview.insert_one(doc)

    return jsonify({'result': 'success', 'msg': f'"{place_receive}" 저장!'})

@app.route("/review", methods=["GET"])
def comment_get():
    comment_list = list(db.festivareview.find({}, {'_id': False}))
    return render_template("review.html", rows=comment_list)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)