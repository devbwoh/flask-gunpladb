from flask import Flask, jsonify
from flask_mysqldb import MySQL
# pip install simplejson 해줘야 함

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
    return "성공!"


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
