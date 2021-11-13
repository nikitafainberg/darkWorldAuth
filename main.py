from flask import Flask, request, Response
import sys

import config as cfg
from DB_manger import dbConnector

app = Flask(__name__)


# GET requests will be blocked
@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    if not request_data:
        return Response("forbidden", status=407)

    username = request_data.get('username')
    password = request_data.get('password')

    if not username or not password:
        # TODO: response with error
        return Response("forbidden", status=405)

    # get user and check passwords

    db_connector = dbConnector()
    user_obj = db_connector.get_user_by_username(username=username)
    if user_obj.get("password") == password:
        return Response("success", status=200)

    return Response("forbidden", status=403)


if __name__ == '__main__':
    app.run(host=cfg.server_ip, port=cfg.server_port, debug=True)
