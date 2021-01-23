from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL
# mysqlclient, flask-mysqldb, simplejson 설치 필요함
# apt-get install libmysqlclient-dev
# pip install simplejson flask-mysqldb
# simplejson은 설치만 해두면 jsonify에서 사용함

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql1234'
app.config['MYSQL_DB'] = 'gunpladb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_SORT_KEYS'] = False
db = MySQL(app)


@app.route("/")
def index():
    return render_template('list.html')


@app.route("/mechanic", methods=["GET"])
def mechanic():
    query = 'select * from mechanic'
    cur = db.connection.cursor()
    cur.execute(query)
    return jsonify(cur.fetchall())

# @app.route("/mechanic", methods=["GET"])
# def mechanic():
#     query = 'select * from mechanic'
#     cur = db.connection.cursor()
#     cur.execute(query)
#     r = Response(response=json.dumps(cur.fetchall()))
#     r.headers["Content-Type"] = "application/json; charset=utf-8"
#     return r


@app.route("/gunpla", methods=["GET"])
def gunpla():
    query = 'select * from gunpla'
    cur = db.connection.cursor()
    cur.execute(query)
    return jsonify(cur.fetchall())


@app.route("/image", methods=["GET"])
def image():
    query = 'select * from image'
    cur = db.connection.cursor()
    cur.execute(query)
    return jsonify(cur.fetchall())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
