# This is a simple example web app that is meant to illustrate the basics.
from flask import Flask, render_template, redirect, g, request, url_for, jsonify, json
import urllib
import requests  # similar purpose to urllib.request, just more convenience
import os

app = Flask(__name__)

#TODO_API_URL = "http://"+os.environ['TODO_API_IP']+":5001"
TODO_API_URL = "http://127.0.0.1:5001"


@app.route("/")
def login():
    return render_template('login.html', errorInfo=False)


@app.route("/login", methods=['POST'])
def login_check():
    resp = requests.post(TODO_API_URL+"/api/login", json={
                  "NAME": request.form['name'], "PW": request.form['pw']})
    print(resp)
    resp = resp.json()
    print(resp)
    if resp['result']:
        return redirect(url_for('show_list', userid=resp['userid'][0]))
    else:
        return render_template('login.html', errorInfo=True)


@app.route("/show/<userid>")
def show_list(userid):
    userid = urllib.parse.quote(userid)
    user_name = requests.get(TODO_API_URL+"/api/username/"+userid)
    user_name = user_name.json()
    resp = requests.get(TODO_API_URL+"/api/items/"+userid)
    resp = resp.json()
    print(resp)
    return render_template('index.html', username=user_name['name'], uid=userid, todolist=resp,things=len(resp))


@app.route("/add/<userid>", methods=['POST'])
def add_entry(userid):
    userid = urllib.parse.quote(userid)
    requests.post(TODO_API_URL+"/api/items", json={
                  "what_to_do": request.form['what_to_do'], "due_date": request.form['due_date'], 'ID': userid})
    return redirect(url_for('show_list', userid=userid))


@app.route("/delete/<userid>/<item>")
def delete_entry(userid, item):
    userid = urllib.parse.quote(userid)
    item = urllib.parse.quote(item)
    requests.delete(TODO_API_URL+"/api/items/"+userid + '/' + item)
    return redirect(url_for('show_list', userid=userid))


@app.route("/mark/<userid>/<item>")
def mark_as_done(userid, item):
    userid = urllib.parse.quote(userid)
    item = urllib.parse.quote(item)
    requests.put(TODO_API_URL+"/api/items/" + userid + '/' +item)
    return redirect(url_for('show_list', userid=userid))


if __name__ == "__main__":
    app.run("0.0.0.0")
