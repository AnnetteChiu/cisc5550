# RESTful API
from flask import Flask, render_template, redirect, g, request, url_for, jsonify, Response
import sqlite3
import urllib
import json

DATABASE = 'todolist.db'


app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/api/items/<userid>")  # default method is GET
def get_items(userid):
    userid = urllib.parse.unquote(userid)
    db = get_db()
    cur = db.execute('SELECT what_to_do, due_date, status FROM entries where ID="'+userid+'"')
    entries = cur.fetchall()
    tdlist = [dict(what_to_do=row[0], due_date=row[1], status=row[2])
              for row in entries]
    response = Response(json.dumps(tdlist),  mimetype='application/json')
    return response

@app.route("/api/username/<userid>")
def get_username(userid):
    userid = urllib.parse.unquote(userid)
    db = get_db()
    res = db.execute('SELECT NAME FROM users where ID="'+userid+'"')
    res = list(res)
    print(res)
    return jsonify({"name": res[0][0]})


@app.route("/api/login", methods=['POST'])
def login():
    db = get_db()
    name = request.json['NAME']
    pw = request.json['PW']
    sql_str = 'select ID from users where NAME="' + name + '";'
    res = db.execute(sql_str)
    res = list(res)
    if len(res) == 0:
        db.execute("insert into users (NAME, PW) values ('" + name + "','"+pw+"')")
    sql_str = 'select ID from users where NAME="' + name + '" and PW="' + pw + '";'
    # print(sql_str)
    res = db.execute(sql_str)
    res = list(res)
    # print(res)
    db.commit()
    if len(res) == 0:
        return jsonify({"result": False})
    else:
        return jsonify({"result": True, "userid":res[0]})


@app.route("/api/items", methods=['POST'])
def add_item():
    db = get_db()
    db.execute('insert into entries (ID, what_to_do, due_date, status) values (?, ?, ?, ?)',
               [request.json['ID'], request.json['what_to_do'], request.json['due_date'], 'processing'])
    db.commit()
    return jsonify({"result": True})


@app.route("/api/items/<userid>/<item>", methods=['DELETE'])
def delete_item(userid, item):
    userid = urllib.parse.unquote(userid)
    item = urllib.parse.unquote(item)
    db = get_db()
    db.execute("DELETE FROM entries WHERE what_to_do='"+item+"' and ID='" + userid + "'")
    db.commit()
    return jsonify({"result": True})


@app.route("/api/items/<userid>/<item>", methods=['PUT'])
def update_item(userid, item):
    # we do not need the body so just ignore it
    userid = urllib.parse.unquote(userid)
    item = urllib.parse.unquote(item)
    db = get_db()
    db.execute("UPDATE entries SET status='done' WHERE what_to_do='"+item+"' and ID='" + userid + "'")
    db.commit()
    return jsonify({"result": True})


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001)
