# -*- coding: utf-8 -*-
import os
from flask import Flask, jsonify, request, render_template
from werkzeug.exceptions import NotFound, ServiceUnavailable
import requests
from services.user.user_dao import get_users, create_user


app = Flask(__name__)


@app.route("/index", methods=['GET'])
def hello():
    return jsonify({
        "uri": "/",
        "subresource_uris": {
            "users": "/users",
            "user": "/users/<username>",
            "bookings": "/users/<username>/bookings",
            "suggested": "/users/<username>/suggested"
        }
    })


@app.route("/users", methods=['GET'])
def users_list():
    user_info = get_users()
    if not isinstance(user_info, dict):
        return jsonify({"result": "query db error: %s" % user_info})
    return jsonify(user_info)


@app.route("/users", methods=['POST'])
def add_user():
    user_name = request.values.get("user_name")
    user_pwd = request.values.get("user_pwd")
    user_type = request.values.get("user_type")
    if user_name and user_pwd and user_type:
        res = create_user(user_name, user_pwd, user_type)
        if res == 0:
            return jsonify({"result": "create user success"})
        return jsonify({"result": "create user failed: %s" % res})
    return jsonify({"result": "please check args"})


@app.route("/download", methods=['GET'])
def download():
    file_path = request.values.get("file_path")
    # file_path = "ftp://localhost:2121/ftp_server.py"
    if not file_path:
        file_path = "D:/xiaochen/services/ftp_server"
    if not os.path.exists(file_path):
        return jsonify({"result": "please check path"})
    html = "<html>\n"
    for f in os.listdir(file_path):
        html += '<a href="ftp://localhost:2121/%s">%s</a></br>' % (f, f)
    html += "</html>"
    return html


if __name__ == "__main__":
    app.run(port=5000, debug=True)
