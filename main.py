import datetime

import jwt
from flask import Flask, request, jsonify

import config as cfg
from DB_manger import dbConnector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret_key'


# GET requests will be blocked
@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    if not request_data:
        return jsonify({"status": "forbidden"}), 403

    username = request_data.get('username')
    password = request_data.get('password')

    if not username or not password:
        # TODO: response with error
        return jsonify({"status": "forbidden"}), 403

    # get user and check passwords

    db_connector = dbConnector()
    user_obj = db_connector.get_user_by_username(username=username)

    if user_obj.get("password") == password:
        token = jwt.encode(
            {
                'public_id': user_obj.get("id"),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=cfg.token_expire_mins)
            },
            app.config['SECRET_KEY']
        )
        print("DEBUG  Token: {}".format(token))
        return jsonify({"status": "success", "token": token}), 200

    return jsonify({"status": "forbidden"}), 403


if __name__ == '__main__':
    app.run(host=cfg.server_ip, port=cfg.server_port, debug=True)
