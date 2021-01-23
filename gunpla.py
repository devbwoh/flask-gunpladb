from flask import Flask, jsonify, render_template, request, redirect
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
    query = 'select * from mechanic'
    cur = db.connection.cursor()
    cur.execute(query)
    return render_template('list.html', list = cur.fetchall())


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

@app.route("/insert", methods=[ "GET", "POST" ])
def insert():
    if request.method == 'GET':
        return render_template('insert.html')
    elif request.method == 'POST':
        query = 'insert into mechanic values (null, %s, %s, %s, %s, %s, %s)'
        # print(request.form)
        params = (
            request.form['name'],
            request.form['model'],
            request.form['manufacturer'],
            request.form['armor'],
            float(request.form['height']),
            float(request.form['weight'])
        )
        cur = db.connection.cursor()
        cur.execute(query, params)
        db.connection.commit()
        return index()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
