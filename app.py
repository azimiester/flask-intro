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
        r = review(db, None, pid, rating, uid, comment)
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

@app.route('/review/reviews/<int:pid>/<string:date_from>/<string:date_to>', methods=["GET"])
@auth.login_required
def product_reviews(pid, date_to, date_from):
    try:
        db = db_con()
        if not pid or not date_to or not date_from:
            raise Exception(notifs.errors['invalid_arguments'])
        rs = reviews(db)
        return jsonify({'success': True, 'data': rs.get_product_reviews(pid, date_from, date_to)})
        db.close_conn()

    except Exception as e:
        return jsonify({'success': False, 'data': str(e)})
        db.close_conn()

@app.route('/review/summary/<int:pid>/<string:date_from>/<string:date_to>', methods=["GET"])
@auth.login_required
def product_summary(pid, date_to, date_from):
    try:
        db = db_con()
        if not pid or not date_to or not date_from:
            raise Exception(notifs.errors['invalid_arguments'])
        rs = reviews(db)
        return jsonify({'success': True, 'data': rs.get_product_summary(pid, date_from, date_to)})
        db.close_conn()

    except Exception as e:
        return jsonify({'success': False, 'data': str(e)})
        db.close_conn()

@app.route('/review/<int:id>', methods=["DELETE"])
@auth.login_required
def delete_review(id):
    try:
        db = db_con()
        if not id:
            raise Exception(notifs.errors['invalid_arguments'])
        r = review(db, id)
        return jsonify({'success': True, 'data': r.delete_review(id)})
        db.close_conn()

    except Exception as e:
        return jsonify({'success': False, 'data': str(e)})
        db.close_conn()


if __name__ == '__main__':
    app.run(debug=True)
