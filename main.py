from flask import Flask, request

import config as cfg
from DB_manger import dbConnector

app = Flask(__name__)


# GET requests will be blocked
@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    if not request_data:
        return "forbidden"

    username = request_data.get('username')
    password = request_data.get('password')

    if not username or not password:
        # TODO: response with error
        return "forbidden"

    # get user and check passwords

    db_connector = dbConnector()
    user_obj = db_connector.get_user_by_username(username=username)
    if user_obj.get("password") == password:
        return "success"

    return "forbidden"


if __name__ == '__main__':
    app.run(host=cfg.server_ip, port=cfg.server_port)
