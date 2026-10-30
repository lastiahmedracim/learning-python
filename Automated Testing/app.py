import requests
from copy import deepcopy
import os

# def read_database():
#     return []


# def get_username():
#     return read_database()


# def fetch_data():
#     return {"status": "success"}


# def fetch_users():
#     return ["Hunter", "Alex", "Sarah"]


# def count_users():
#     users = fetch_users()
#     return len(users)


# def send_email(email, message):
#     print(f"Sending email to {email}: {message}")


# def notify_user(email):
#     send_email(email, "Your account was created")


# def log_event(message):
#     print(message)


# def register_user():
#     log_event("User validation started")
#     log_event("User created")
#     log_event("Welcome email scheduled")


# def fetch_data():
#     response = requests.get("www.example.com/users/1", timeout=5)
#     response.raise_for_status()
#     return response.json()


# def fetch_user():
#     try:
#         response = requests.get(
#             "https://example.com/users/1",
#             timeout=5
#         )
#         response.raise_for_status()
#         return response.json()

#     except requests.RequestException:
#         return None





def fetch_user():
    try:
        response = requests.get(
            "https://example.com/users/1",
            headers= {
                "Accept": "application/json"
            },
            timeout=5
        )
        response.raise_for_status()

        user = response.json()

        if not isinstance(user, dict):
            return None

        return user

    except requests.RequestException:
        return None



def get_user_name():
    try:
        user = fetch_user()
    except ValueError:
        return None

    if user is None:
        return None

    return user.get("name")



# def validate_username(username):
#     if not username:
#         raise ValueError("Username is required")
#     return username


def validate_username(username):
    if len(username) < 3:
        raise ValueError("Username must contain at least 3 characters")

    return username


def normalize_username(username):
    return username.strip().lower()


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot devide by zero")
    return a / b

def is_even(number):
    return number % 2 == 0



def add_tag(user, tag):
    new_user = deepcopy(user)
    new_user["tags"].append(tag)
    return new_user


def save_user(email):
    print(f"Saving {email}")

def register_user(email):
    save_user(email)
    return {"email": email, "saved": True}


def read_report(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def fetch_product(product_id):
    response = requests.get(f"https://api.example.com/products/{product_id}", timeout=5)
    response.raise_for_status()
    return response.json()


def fetch_with_retry(url):
    for attemp in range(2):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            if attemp == 1:
                raise

import time

CACHE_DURATION = 60
cache_data = None
cache_time = 0

def get_cached_data():
    global cache_data, cache_time

    now = time.monotonic()

    if cache_data is not None and now - cache_time < CACHE_DURATION:
        return cache_data

    response = requests.get("https://api.example.com/users", timeout=5)
    response.raise_for_status()
    cache_data = response.json()
    cache_time = now

    return cache_data


def process_response(response):
    response.raise_for_status()
    return response.json()


def get_api_url():
    return os.getenv(
        "API_URL",
        "https://api.example.com"
    )


def save_user_data(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def validate_age(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("age must be integer")

    if age > 120 or age < 0:
        raise ValueError("age must be between 0 and 120")

    return True




def calculate_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Numbers must be a list")

    if not numbers:
        raise ValueError("Numbers cannot be empty")

    if any(
        not isinstance(value, (int, float)) or isinstance(value, bool)
        for value in numbers
    ):
        raise TypeError("All values must be numbers")

    return sum(numbers) / len(numbers)




def get_user_name(user):
    if not isinstance(user, dict):
        raise TypeError("User must be a dictionary")

    if "profile" not in user:
        raise ValueError("Profile is missing")

    profile = user["profile"]

    if not isinstance(profile, dict):
        raise TypeError("Profile must be a dictionary")

    if "name" not in profile:
        raise ValueError("Name is missing")

    name = profile["name"]

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")

    return name.strip()



def remove_password(user):
    result = deepcopy(user)
    result.pop("password")
    return result





def sort_scores(scores):
    if not isinstance(scores, list):
        raise TypeError("Scores must be a list")

    if any(
        not isinstance(score, (int, float)) or isinstance(score, bool)
        for score in scores
    ):
        raise TypeError("All scores must be numbers")

    return sorted(scores)





def get_page(items, page, page_size):
    if not isinstance(items, list):
        raise TypeError("items must be a list")

    if not isinstance(page, int) or isinstance(page, bool) or page <= 0:
        raise ValueError("page must be a positive integer")

    if not isinstance(page_size, int) or isinstance(page_size, bool) or page_size <= 0:
            raise ValueError("page size must be a positive integer")
    
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]


from datetime import datetime

def is_expired(expiry_time, now):
    if not isinstance(expiry_time, datetime) or not isinstance(now, datetime):
        raise TypeError("both value must be datetime objects")

    return now >= expiry_time


def get_product(product_id):
    response = requests.get(f"https://api.example.com/products/{product_id}", timeout=5)
    response.raise_for_status()
    user = response.json()

    if not isinstance(user, dict):
        raise ValueError("invalid product data")

    id = user.get("id")
    title = user.get("title")
    price = user.get("price")

    if (
        not isinstance(id, int)
        or isinstance(id, bool)
        or id <= 0
    ):
        raise ValueError("Invalid product data")

    if not isinstance(title, str) or not title.strip():
        raise ValueError("Invalid product data")

    if (
        not isinstance(price, (int, float))
        or isinstance(price, bool)
        or price < 0
    ):
        raise ValueError("Invalid product data")

    return {
        "id": id,
        "title": title.strip(),
        "price": price,
    }





def create_user_table(connection):
    connection.execute("""
        create table if not exsists users (
            id integer primary key autoincreament,
            name text not null,
            email text not null
        )
    """)
    connection.commit()


def add_user(connection, name, email):
    cursor = connection.execute(
        "insert into users (name, email) values (?, ?)",
        (name, email)
    )
    connection.commit()
    return cursor.lastrowid










def create_accounts_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            balance REAL NOT NULL CHECK (balance >= 0)
        )
    """)
    connection.commit()

def get_balance(connection, id):
    return connection.execute(
        "select balance from accounts where id = ?"(id,)
    ).fetchone()

def transfer_money(connection, sender_id, receiver_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    try:
        sender = connection.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (sender_id,),
        ).fetchone()

        receiver = connection.execute(
            "SELECT balance FROM accounts WHERE id = ?",
            (receiver_id,),
        ).fetchone()

        if sender is None or receiver is None:
            raise ValueError("Account not found")

        if sender[0] < amount:
            raise ValueError("Insufficient balance")

        connection.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, sender_id),
        )

        connection.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, receiver_id),
        )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    return connection.execute(
        "SELECT balance FROM accounts WHERE id = ?",
        (receiver_id,),
    ).fetchone()[0]




def create_products_table(connection):
    connection.execute("""
        create table if not exists products (
            id integer primary key autoincrement,
            name text unique not null check (name <> ''),
            price integer not null check (price > 0)

        )
    """)
    connection.commit()

def add_product(connection, name, price):
    cursor = connection.execute(
        "insert into products (name, price) values (?, ?)", (name, price)
    )
    connection.commit()
    return cursor.lastrowid