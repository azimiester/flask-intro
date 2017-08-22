#!flask-intro/bin/python
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask import request
from flask import jsonify
from config.notifs import *
from config.connection import *
from models.review import *
from models.reviews import *

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    "username": "password",
}
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/review/', methods=["POST"])
def add_review():
    try:
        db = db_con()
        if not request.form or not 'pid' in request.form or not 'rating' in request.form:
            raise Exception(notifs.errors['invalid_arguments'])
        pid = int(request.form['pid'])
        uid = int(request.form['uid']) if 'uid' in request.form else None
        rating = int(request.form['rating'])
        comment = request.form['comment'] if 'comment' in request.form else None
        r = review(db, None, pid, uid, rating, comment)
        r.set_review()
        #should have used finally for closing connection, doesn't work for some reason.
        db.close_conn()
        return jsonify({'success': True, 'data': r.get_object()})
    except Exception as e:
        db.close_conn()
        return jsonify({'success': False, 'data': str(e)})

@app.route('/review/<int:id>', methods=["GET"])
def get_review(id):
    try:
        db = db_con()
        if not id:
            raise Exception(notifs.errors['invalid_arguments'])
        r = review(db, id)
        db.close_conn()
        return jsonify({'success': True, 'data': r.get_object()})
    except Exception as e:
        db.close_conn()
        return jsonify({'success': False, 'data': str(e)})

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

if __name__ == '__main__':
    app.run(debug=True)
