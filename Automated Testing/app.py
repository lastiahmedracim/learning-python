def read_database():
    return []

def get_username():
    return read_database()

def fetch_data():
    return {"status": "success"}


def fetch_users():
    return ["Hunter", "Alex", "Sarah"]


def count_users():
    users = fetch_users()
    return len(users)