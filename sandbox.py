from DB_manger import dbConnector

if __name__ == '__main__':
    db_connector = dbConnector()

    users = db_connector.get_user_by_username("nick")[0]
    print(users)
