import json

# json_data = '''
# {
#     "username": "Hunter",
#     "age": 25,
#     "email": "hunter@example.com",
#     "is_active": true
# }
# '''

# python_data = json.loads(json_data)

# print(python_data["username"])
# print(python_data["email"])
# print(python_data["age"])
# if python_data["is_active"]:
#     print(f"{python_data["username"]} is active")
# python_data["age"] = 26
# json_data1 = json.dumps(python_data)
# print(json_data1)



# users = [
#     {
#         "username": "Hunter",
#         "age": 25,
#         "active": True
#     },
#     {
#         "username": "Alice",
#         "age": 22,
#         "active": True
#     },
#     {
#         "username": "Bob",
#         "age": 17,
#         "active": False
#     }
# ]

# with open("users.json", "w") as file:
#     json.dump(users, file, indent=4)

# with open("users.json", "r") as file:
#     updated_users = json.load(file)

# for user in updated_users:
#     print(user["username"])

# for user in updated_users:
#     if user["active"]:
#         print(user["username"])

# for user in updated_users:
#     if user["username"] == "Hunter":
#         user["age"] = 26

# with open("users.json", "w") as file:
#     json.dump(updated_users, file, indent=4)



# def save_users(users):
#     with open("users.json", "w") as file:
#         json.dump(users, file, indent=4)

# def load_users():
#     try:
#         with open("users.json", "r") as file:
#             return json.load(file)

#     except FileNotFoundError:
#         print("file not founded")
#         return []

#     except json.JSONDecodeError:
#         print("invaild json")
#         return []

# def add_user(users, username, age):
#     user = {
#         "username" : username,
#         "age": age,
#         "active": True
#     }

#     users.append(user)


# users = load_users()

# add_user(users, "Hunter", 25)
# add_user(users, "Alice", 22)

# save_users(users)

# users = load_users()

# for user in users:
#     print(user["username"])



# import logging

# # =========================
# # LOGGING
# # =========================

# logger = logging.getLogger("user_manager")
# logger.setLevel(logging.INFO)

# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler("user_manager.log")

# console_handler.setLevel(logging.WARNING)
# file_handler.setLevel(logging.INFO)

# formatter = logging.Formatter(
#     "%(asctime)s - %(levelname)s - %(message)s"
# )

# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)


# # =========================
# # LOAD USERS
# # =========================

# def load_users():
#     try:
#         with open("users.json", "r") as file:
#             return json.load(file)

#     except FileNotFoundError:
#         logger.warning("users.json not found")
#         return []

#     except json.JSONDecodeError:
#         logger.error("users.json contains invalid JSON")
#         return []


# # =========================
# # SAVE USERS
# # =========================

# def save_users(users):
#     try:
#         with open("users.json", "w") as file:
#             json.dump(users, file, indent=4)

#         logger.info("Users saved successfully")

#     except OSError:
#         logger.exception("Failed to save users")


# # =========================
# # ADD USER
# # =========================

# def add_user(users, username, age, email):

#     if not username:
#         logger.warning("User registration failed: empty username")
#         return False

#     if age < 18:
#         logger.warning(
#             f"User registration failed: {username} is under 18"
#         )
#         return False

#     if not email:
#         logger.warning(
#             f"User registration failed: {username} has no email"
#         )
#         return False

#     # Generate ID
#     if users:
#         new_id = max(user["id"] for user in users) + 1
#     else:
#         new_id = 1

#     user = {
#         "id": new_id,
#         "username": username,
#         "age": age,
#         "email": email,
#         "active": True
#     }

#     users.append(user)

#     logger.info(f"User {username} registered successfully")

#     return True


# # =========================
# # FIND USER
# # =========================

# def find_user(users, username):

#     for user in users:
#         if user["username"] == username:
#             return user

#     logger.warning(f"User {username} not found")

#     return None


# # =========================
# # DEACTIVATE USER
# # =========================

# def deactivate_user(users, username):

#     user = find_user(users, username)

#     if user is None:
#         return False

#     user["active"] = False

#     logger.info(f"User {username} deactivated")

#     return True


# # =========================
# # LIST ACTIVE USERS
# # =========================

# def list_active_users(users):

#     print("\nActive users:")

#     for user in users:
#         if user["active"]:
#             print(
#                 f"{user['username']} - {user['email']}"
#             )


# # =========================
# # MAIN
# # =========================

# def main():

#     users = load_users()

#     add_user(
#         users,
#         "Hunter",
#         25,
#         "hunter@example.com"
#     )

#     add_user(
#         users,
#         "Alice",
#         22,
#         "alice@example.com"
#     )

#     add_user(
#         users,
#         "Bob",
#         16,
#         "bob@example.com"
#     )

#     add_user(
#         users,
#         "",
#         25,
#         "empty@example.com"
#     )

#     hunter = find_user(users, "Hunter")

#     if hunter:
#         print("\nFound user:")
#         print(hunter)

#     find_user(users, "Charlie")

#     deactivate_user(users, "Alice")

#     list_active_users(users)

#     save_users(users)

#     # Load again to verify the file
#     users = load_users()

#     print("\nAfter loading from file:")

#     list_active_users(users)


# if __name__ == "__main__":
#     main()


