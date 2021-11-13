# TODO: rename to DB_host etc
import os

ENV = os.getenv("stage")

if ENV == "dev":
    host = "127.0.0.1"
    user = "admin"
    password = "admin"
    database = "DarkWorldAuth"
    server_ip = "127.0.0.1"
    server_port = "24390"
else:
    host = "192.168.31.180"
    user = "admin"
    password = "Qwe_123!_123456789"
    database = "DarkWorldAuth"
    server_ip = "192.168.31.82"
    server_port = "24390"

token_expire_mins = 60
