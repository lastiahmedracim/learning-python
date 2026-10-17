import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("application started")
# logging.error("application error")
# logging.warning("application warning")
# logging.critical("application critical")
# logging.debug("application debug")

# def login(username:str, password:str) -> bool:
#     if username == "admin" and password == "1234":
#         logging.info("the user logged in successfully")
#         return True
#     else:
#         logging.warning("invalid login was attempted")
#         return False

# login("admin", "1234")
# login("hunter", "wrong")

# logging.basicConfig(
#     level= logging.INFO,
#     format= "%(levelname)s:%(name)s:%(message)s"
# )

# logger = logging.getLogger(__name__)

# def create_user(username: str) -> bool:
#     if username == "":
#         logger.error("error")
#         return False
#     elif username != "":
#         logger.info("info")
#         return True

# create_user("Hunter")
# create_user("")

# logging.basicConfig(
#     level= logging.INFO,
#     format= "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
#     filename= "activity.log"
# )

# logger = logging.getLogger(__name__)

# def login(username: str) -> bool:
#     if username == "":
#         logger.error("error")
#         return False
#     elif username != "":
#         logger.info("info")
#         return True

# login("Hunter")
# login("Alice")
# login("")

# logger = logging.getLogger("backend")
# logger.setLevel(logging.INFO)

# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler("server.log")

# formatter = logging.Formatter(
#     "%(asctime)s - %(levelname)s - %(message)s"
# )

# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# def start_server():
#     logger.info("server started")

# def login(username: str) -> bool:
#     if username == "":
#         logger.error("login faild")
#         return False
#     elif username != "":
#         logger.info(f"user {username} logged in")
#         return True

# start_server()

# login("Hunter")
# login("")

# logger = logging.getLogger("api")
# logger.setLevel(logging.INFO)

# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler("api.log")

# formatter = logging.Formatter(
#     "%(asctime)s %(levelname)s %(message)s"
# )

# console_handler.setLevel(level= logging.WARNING)
# file_handler.setLevel(level= logging.INFO)

# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# def process_request(username: str) -> bool:
#     if not username:
#         logger.error("Request rejected: missing username")
#     elif username == "admin":
#         logger.warning("Admin request received")
#     else:
#         logger.info("Request processed for USERNAME")

# process_request("Hunter")
# process_request("admin")
# process_request("")


# logger = logging.getLogger("user_service")
# logger.setLevel(logging.INFO)

# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler("users.log")

# console_handler.setLevel(logging.WARNING)
# file_handler.setFormatter(logging.INFO)

# formatter = logging.Formatter(
#     "%(asctime)s %(levelname)s %(message)s"
# )

# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# def register_user(username: str, age: int) -> bool:

#     try:
#         if not username:
#             logger.error("Registration failed: username is empty")
#             return False
        
#         if age < 18:
#             logger.warning("Registration rejected: user is under 18")
#             return False

#         logger.info(f"User {username} registered successfully")
#         return True
    
#     except Exception:
#         logger.exception("somthing went wrong")


# register_user("Hunter", 25)
# register_user("Alice", 16)
# register_user("", 25)
# register_user("Bob", "abc")

