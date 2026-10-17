import requests

# url = "https://jsonplaceholder.typicode.com/users/1"

# response = requests.get(url)

# print("status code:",response.status_code)

# data = response.json()

# print(f"Name: {data['name']}")
# print(f"Username: {data['username']}")
# print(f"Email: {data['email']}")
# print(f"City: {data['address']['city']}")


# def get_user(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         return data

#     except requests.RequestException as error:
#         print("api request faild", error)
#         return None

# user = get_user(1)

# if user:
#     print("Name:", user["name"])
#     print("Email:", user["email"])

# user = get_user(999)

# # 200 → Success
# # 201 → Created
# # 400 → Bad request
# # 401 → Unauthorized
# # 403 → Forbidden
# # 404 → Not found
# # 500 → Server error


# def search_users(username):

#     url = "https://jsonplaceholder.typicode.com/users"

#     params = {
#         "username": username
#     }

#     try:
#         response = requests.get(url, timeout=5, params=params)
#         response.raise_for_status()
#         return response.json()
    
#     except requests.RequestException as error:
#         print("api reqests faild", error)
#         return []

# def main():

#     users = search_users("Bret")
#     if users:
#         for user in users:
#                 print("Name:", user["name"])
#                 print("Email:", user["email"])
#                 print("City:", user["address"]["city"])
#     else:
#         print("No users found.")


# if __name__ == "__main__":
#     main()




# def create_user(name, username, email):
#     url = "https://jsonplaceholder.typicode.com/users"

#     user = {
#         "name": name,
#         "username": username,
#         "email": email
#     }

#     try:
#         response = requests.post(
#             url,
#             json=user,
#             timeout=5
#         )

#         response.raise_for_status()

#         return response.json()

#     except requests.RequestException as error:
#         print("API request failed:", error)
#         return None


# def main():
#     user = create_user(
#         "Hunter",
#         "Hunter51197",
#         "hunter@example.com"
#     )

#     if user:
#         print("ID:", user["id"])
#         print("Name:", user["name"])
#         print("Username:", user["username"])
#         print("Email:", user["email"])
#     else:
#         print("User creation failed.")


# if __name__ == "__main__":
#     main()


# def get_users():
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#             "Accept": "application/json"
#     }
#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         data = response.json()
#         return data
    
#     except requests.RequestException as e:
#         print("api request faild", e)
#         return []

# def main():
#     users = get_users()
#     if users:
#         for user in users:
#             print("id: ", user["id"])
#             print("name: ", user["name"])
#             print("username: ", user["username"])
#             print("email: ", user["email"])
#     else:
#         print("no users found")


# if __name__ == "__main__":
#     main()


# def create_user(name, username, email):
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json"
#     }
#     user = {
#         "name": name,
#         "username": username,
#         "email": email
#     }
#     try:
#         response = requests.post(url, json=user, headers=headers, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         return data
    
#     except requests.RequestException as e:
#         print("api request faild", e)
#         return []

# def main():
#     user = create_user(
#         "Hunter",
#         "hunter",
#         "hunter@gmail.com"
#     )

#     if user:
#         print("id:", user["id"])
#         print("name:", user["name"])
#         print("username:", user["username"])
#         print("email:", user["email"])
#     else:
#         print("no user found")

# if __name__ == "__main__":
#     main()




# def get_processed_users():
#     url = "https://jsonplaceholder.typicode.com/users"

#     headers = {
#         "Accept": "application/json"
#     }

#     try:
#         response = requests.get(
#             url,
#             headers=headers,
#             timeout=5
#         )

#         response.raise_for_status()

#         users = response.json()

#         processed_users = []

#         for user in users:
#             email = user["email"]
#             email_domain = email.split("@")[1]

#             new_user = {
#                 "id": user["id"],
#                 "name": user["name"],
#                 "username": user["username"],
#                 "email": email,
#                 "city": user["address"]["city"],
#                 "email_domain": email_domain,
#                 "source": "JSONPlaceholder"
#             }

#             processed_users.append(new_user)

#         return processed_users

#     except requests.RequestException as e:
#         print("API request failed:", e)
#         return []


# def main():
#     users = get_processed_users()

#     for user in users:
#         print("ID:", user["id"])
#         print("Name:", user["name"])
#         print("Username:", user["username"])
#         print("Email:", user["email"])
#         print("City:", user["city"])
#         print("Email domain:", user["email_domain"])
#         print("Source:", user["source"])
#         print("--------------------")


# if __name__ == "__main__":
#     main()




# def get_users_by_city(city):
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#         "Action": "application/json"
#     }
#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#         users = response.json()
#         filtere_users = []

#         for user in users:
#             if user["address"]["city"] == city:
#                 email = user["email"]
#                 email_domain = email.split("@")[1]
#                 new_user = {
#                     "id": user["id"],
#                     "name": user["name"],
#                     "username": user["username"],
#                     "email": email,
#                     "city": user["address"]["city"],
#                     "email_domain": email_domain,
#                     "source": "JSONPlaceholder"
#                 }

#                 filtere_users.append(new_user)

#         return filtere_users

#     except requests.RequestException as e:
#         print("api request faild", e)
#         return []

# def main():
#     users = get_users_by_city("Gwenborough")

#     for user in users:
#         print("ID:", user["id"])
#         print("Name:", user["name"])
#         print("Username:", user["username"])
#         print("Email:", user["email"])
#         print("City:", user["city"])
#         print("Email domain:", user["email_domain"])
#         print("Source:", user["source"])
#         print("--------------------")

# if __name__ == "__main__":
#     main()




# def fetch_users():
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#     "Accept": "application/json"
#     }

#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#         return response.json()

#     except requests.RequestException as e:
#         print("api faild request", e)
#         return []
    
# def process_users(users):
#     processed_users = []

#     for user in users:
#         email = user["email"]
#         email_domain = email.split("@")[1]

#         new_user = {
#             "id": user["id"],
#             "name": user["name"],
#             "username": user["username"],
#             "email": user["email"],
#             "city": user["address"]["city"],
#             "email_domain": email_domain,
#             "source": "JSONPlaceholder"
#         }

#         processed_users.append(new_user)

#     return processed_users


# def main():
#     users = fetch_users()
#     p_users = process_users(users)

#     for user in p_users:
#         print("ID:", user["id"])
#         print("Name:", user["name"])
#         print("Username:", user["username"])
#         print("Email:", user["email"])
#         print("City:", user["city"])
#         print("Email domain:", user["email_domain"])
#         print("Source:", user["source"])
#         print("--------------------")

# if __name__ == "__main__":
#     main()




# def fetch_users():
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#     "Accept": "application/json"
#     }

#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#         return response.json()

#     except requests.RequestException as e:
#         print("api faild request", e)
#         return []

# def validate_user(user):
#     required_field = [
#         "id",
#         "name",
#         "username",
#         "email",
#         "address"
#     ]

#     for field in required_field:
#         if field not in user:
#             return False
#     return True

# def process_users(users):
    
#     processed_user = []

#     for user in users:
#         if validate_user(user):
#             email = user["email"]
#             email_domain = email.split("@")[1]

#             new_user = {
#                 "id": user["id"],
#                 "name": user["name"],
#                 "username": user["username"],
#                 "email": user["email"],
#                 "city": user["address"]["city"],
#                 "email_domain": email_domain,
#                 "source": "JSONPlaceholder"
#             }

#             processed_user.append(new_user)

#     return processed_user


# def main():
#     users = fetch_users()
#     p_user = process_users(users)

#     for user in p_user:
#         print("ID:", user["id"])
#         print("Name:", user["name"])
#         print("Username:", user["username"])
#         print("Email:", user["email"])
#         print("City:", user["city"])
#         print("Email domain:", user["email_domain"])
#         print("Source:", user["source"])
#         print("--------------------")

# if __name__ == "__main__":
#     main()



# def fetch_users():
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#         "Accept": "application/json"
#     }

#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#         return response.json()
    
#     except requests.RequestException as e:
#         print("api faild request", e)
#         return []

# def validate_user(user):
#     required_field = [
#         "id",
#         "name",
#         "username",
#         "email",
#         "address"
#     ]

#     for field in required_field:
#         if field not in user:
#             return False
#     if "city" not in user["address"]:
#         return False
        
#     return True

# def search_users(users, city):
#     processed_user = []
#     for user in users:
#         if validate_user(user):
#             if user["address"]["city"] == city:
#                 email = user["email"]
#                 email_domain = email.split("@")[1]

#                 new_user = {
#                     "id": user["id"],
#                     "name": user["name"],
#                     "username": user["username"],
#                     "email": email,
#                     "city": user["address"]["city"],
#                     "email_domain": email_domain,
#                     "somthing": "dosen't exist"
#                 }

#                 processed_user.append(new_user)

#     processed_user = sorted(processed_user, key=lambda user: user["name"])
#     return processed_user

# def main():
#     users = fetch_users()
#     city = "Gwenborough"
#     p_users = search_users(users, city)

#     for user in p_users:
#         print("id:", user["id"])
#         print("name:", user["name"])
#         print("username:", user["username"])
#         print("email:", user["email"])
#         print("email_domain:", user["email_domain"])
#         print("city:", user["city"])
#         print("somthing:", user["somthing"])

# if __name__ == "__main__":
#     main()





# def fetch_users():
#     url = "https://jsonplaceholder.typicode.com/users"

#     headers = {
#         "Accept": "application/json"
#     }

#     try:
#         response = requests.get(
#             url,
#             headers=headers,
#             timeout=5
#         )

#         response.raise_for_status()
#         return response.json()

#     except requests.RequestException as e:
#         print("API request failed:", e)
#         return []


# def validate_user(user):
#     required_fields = [
#         "id",
#         "name",
#         "username",
#         "email",
#         "address"
#     ]

#     for field in required_fields:
#         if field not in user:
#             return False

#     return True


# def process_users(users):
#     processed_users = []

#     for user in users:
#         if not validate_user(user):
#             continue

#         email = user["email"]

#         new_user = {
#             "id": user["id"],
#             "name": user["name"],
#             "username": user["username"],
#             "email": email,
#             "city": user["address"]["city"],
#             "email_domain": email.split("@")[1]
#         }

#         processed_users.append(new_user)

#     return processed_users


# def paginate_users(users, page, per_page):
#     if page < 1 or per_page < 1:
#         return []

#     start = (page - 1) * per_page
#     end = start + per_page

#     return users[start:end]


# def main():
#     users = fetch_users()
#     processed_users = process_users(users)

#     try:
#         page = int(input("Page number: "))
#         per_page = int(input("Users per page: "))
#     except ValueError:
#         print("Please enter valid numbers.")
#         return

#     page_users = paginate_users(
#         processed_users,
#         page,
#         per_page
#     )

#     if not page_users:
#         print("No users found on this page.")
#         return

#     print(f"\n--- Page {page} ---\n")

#     for user in page_users:
#         print("ID:", user["id"])
#         print("Name:", user["name"])
#         print("Username:", user["username"])
#         print("Email:", user["email"])
#         print("City:", user["city"])
#         print("Email domain:", user["email_domain"])
#         print("--------------------")


# if __name__ == "__main__":
#     main()




# def fetch_request():
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#         "accept": "application/json"
#     }

#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#         return response.json()

#     except requests.RequestException as e:
#         print("api request faild ",e)
#         return []


# def validate_user(user):
#     if not isinstance(user, dict):
#         return False

#     user_id = user.get("id")
#     if not isinstance(user_id, int) or isinstance(user_id, bool):
#         return False

#     name = user.get("name")
#     if not isinstance(name, str) or not name.strip():
#         return False

#     username = user.get("username")
#     if not isinstance(username, str) or not username.strip():
#         return False

#     email = user.get("email")
#     if not isinstance(email, str) or not email.strip():
#         return False

#     address = user.get("address")
#     if not isinstance(address, dict):
#         return False

#     city = address.get("city")
#     if not isinstance(city, str) or not city.strip():
#         return False

#     return True


# def process_users(users):
#     processed_users = []
#     for user in users:
#         if not validate_user(user):
#             continue
#         email = user["email"]
#         email_domain = email.strip().split("@")[1]

#         new_user = {
#             "id": user["id"],
#             "name": user["name"],
#             "username": user["username"],
#             "email": email,
#             "email_domain": email_domain,
#             "city": user["address"]["city"]
#         }

#         processed_users.append(new_user)

#     return processed_users


# def main():
#     users = fetch_request()
#     processed_users = process_users(users)


#     if not processed_users:
#         print("no user found")
#         return
    
#     for user in processed_users:
#         print("ID:", user["id"])
#         print("Name:", user["name"])
#         print("Username:", user["username"])
#         print("Email:", user["email"])
#         print("Email domain:", user["email_domain"])
#         print("City:", user["city"])
#         print("--------------------")

#     valid_user = {
#     "id": 1,
#     "name": "Hunter",
#     "username": "hunter",
#     "email": "hunter@example.com",
#     "address": {"city": "Algiers"}
#     }

#     invalid_user = {
#         "id": 2,
#         "name": "   ",
#         "username": "player2",
#         "email": "player2@example.com",
#         "address": {"city": "Algiers"}
#     }

#     invalid_id_user = {
#         "id": True,
#         "name": "Player3",
#         "username": "player3",
#         "email": "player3@example.com",
#         "address": {"city": "Algiers"}
#     }

#     print(validate_user(valid_user))
#     print(validate_user(invalid_user))
#     print(validate_user(invalid_id_user))


# if __name__ == "__main__":
#     main()






# from collections import Counter

# def fetch_users():
#     url = "https://jsonplaceholder.typicode.com/users"

#     headers = {
#         "Accept": "application/json"
#     }

#     try:
#         response = requests.get(
#             url,
#             headers=headers,
#             timeout=5
#         )

#         response.raise_for_status()
#         return response.json()

#     except requests.RequestException as e:
#         print("API request failed:", e)
#         return []


# def validate_user(user):
#     if not isinstance(user, dict):
#         return False

#     user_id = user.get("id")

#     if not isinstance(user_id, int) or isinstance(user_id, bool):
#         return False

#     for field in ("name", "username", "email"):
#         value = user.get(field)

#         if not isinstance(value, str) or not value.strip():
#             return False

#     address = user.get("address")

#     if not isinstance(address, dict):
#         return False

#     city = address.get("city")

#     if not isinstance(city, str) or not city.strip():
#         return False

#     return True


# def process_users(users):
#     processed_users = []

#     for user in users:
#         if not validate_user(user):
#             continue

#         email = user["email"].strip()

#         if email.count("@") != 1:
#             continue

#         email_name, email_domain = email.split("@")

#         if not email_name or not email_domain:
#             continue

#         new_user = {
#             "id": user["id"],
#             "name": user["name"].strip(),
#             "username": user["username"].strip(),
#             "email": email,
#             "city": user["address"]["city"].strip(),
#             "email_domain": email_domain.split(".")[-1].lower()
#         }

#         processed_users.append(new_user)

#     return processed_users


# def calculate_statistics(users):
#     city_counts = Counter(
#         user["city"] for user in users
#     )

#     email_domain_counts = Counter(
#         user["email_domain"] for user in users
#     )

#     most_common = city_counts.most_common(1)

#     if most_common:
#         most_common_city = most_common[0][0]
#     else:
#         most_common_city = None

#     return {
#         "total_users": len(users),
#         "city_counts": dict(city_counts),
#         "email_domain_counts": dict(email_domain_counts),
#         "most_common_city": most_common_city
#     }


# def main():
#     raw_users = fetch_users()
#     processed_users = process_users(raw_users)

#     statistics = calculate_statistics(processed_users)

#     print("Total users:", statistics["total_users"])

#     print("\nUsers per city:")
#     for city, count in statistics["city_counts"].items():
#         print(f"{city}: {count}")

#     print("\nUsers per email domain:")
#     for domain, count in statistics["email_domain_counts"].items():
#         print(f"{domain}: {count}")

#     print("\nMost common city:", statistics["most_common_city"])


# if __name__ == "__main__":
#     main()






# from collections import Counter

# def fetch_users():
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {"Accept": "application/json"}

#     try:
#         response = requests.get(
#             url,
#             headers=headers,
#             timeout=5
#         )
#         response.raise_for_status()

#         data = response.json()

#         if not isinstance(data, list):
#             print("Unexpected API response format.")
#             return []

#         return data

#     except requests.RequestException as error:
#         print("API request failed:", error)
#         return []


# def validate_user(user):
#     if not isinstance(user, dict):
#         return False

#     user_id = user.get("id")

#     if not isinstance(user_id, int) or isinstance(user_id, bool):
#         return False

#     for field in ("name", "username", "email"):
#         value = user.get(field)

#         if not isinstance(value, str) or not value.strip():
#             return False

#     address = user.get("address")

#     if not isinstance(address, dict):
#         return False

#     city = address.get("city")

#     if not isinstance(city, str) or not city.strip():
#         return False

#     return True


# def process_users(users):
#     processed_users = []

#     for user in users:
#         if not validate_user(user):
#             continue

#         email = user["email"].strip()

#         if email.count("@") != 1:
#             continue

#         email_name, email_domain = email.split("@")

#         if not email_name or not email_domain:
#             continue

#         if "." not in email_domain:
#             continue

#         if email_domain.startswith(".") or email_domain.endswith("."):
#             continue

#         processed_user = {
#             "id": user["id"],
#             "name": user["name"].strip(),
#             "username": user["username"].strip(),
#             "email": email,
#             "city": user["address"]["city"].strip(),
#             "email_domain": email_domain.lower()
#         }

#         processed_users.append(processed_user)

#     return processed_users


# def filter_users(users, city=None, email_domain=None):
#     filtered_users = []

#     for user in users:
#         if city is not None:
#             if user["city"].casefold() != city.strip().casefold():
#                 continue

#         if email_domain is not None:
#             if user["email_domain"].casefold() != email_domain.strip().casefold():
#                 continue

#         filtered_users.append(user)

#     return filtered_users


# def generate_report(users):
#     city_counts = Counter(
#         user["city"] for user in users
#     )

#     domain_counts = Counter(
#         user["email_domain"] for user in users
#     )

#     most_common = city_counts.most_common(1)

#     if most_common:
#         most_common_city = most_common[0][0]
#     else:
#         most_common_city = None

#     return {
#         "total_users": len(users),
#         "users_per_city": dict(city_counts),
#         "users_per_email_domain": dict(domain_counts),
#         "most_common_city": most_common_city,
#         "unique_email_domains": len(domain_counts)
#     }


# def main():
#     raw_users = fetch_users()
#     processed_users = process_users(raw_users)

#     city_input = input("City (leave empty for all cities): ").strip()
#     domain_input = input(
#         "Email domain (leave empty for all domains): "
#     ).strip()

#     city = city_input if city_input else None
#     email_domain = domain_input if domain_input else None

#     matching_users = filter_users(
#         processed_users,
#         city=city,
#         email_domain=email_domain
#     )

#     report = generate_report(matching_users)

#     print("\n========== USER REPORT ==========")
#     print("Total users:", report["total_users"])
#     print("Users per city:", report["users_per_city"])
#     print("Users per email domain:", report["users_per_email_domain"])
#     print("Most common city:", report["most_common_city"])
#     print("Unique email domains:", report["unique_email_domains"])

#     print("\n========== MATCHING USERS ==========")

#     if not matching_users:
#         print("No matching users found.")
#         return

#     for user in matching_users:
#         print(f"Name: {user['name']}")
#         print(f"Email: {user['email']}")
#         print(f"City: {user['city']}")
#         print(f"Domain: {user['email_domain']}")
#         print("-" * 30)


# if __name__ == "__main__":
#     main()






import time

cached_users = None
cache_time = 0
cache_source = "none"

CACHE_DURATION = 60


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )
        response.raise_for_status()

        users = response.json()

        if not isinstance(users, list):
            print("Invalid API response format.")
            return None

        return users

    except requests.RequestException as error:
        print("API request failed:", error)
        return None


def get_cached_users():
    global cached_users, cache_time, cache_source

    current_time = time.monotonic()

    # Check whether the cache exists and is still valid.
    if (
        cached_users is not None
        and current_time - cache_time < CACHE_DURATION
    ):
        cache_source = "cache"
        return cached_users

    # Cache is missing or expired, so fetch fresh data.
    fresh_users = fetch_users()

    if fresh_users is not None:
        cached_users = fresh_users
        cache_time = time.monotonic()
        cache_source = "API"
        return cached_users

    # If refreshing fails, use older cached data if available.
    if cached_users is not None:
        cache_source = "stale cache (API refresh failed)"
        return cached_users

    cache_source = "none"
    return []


def process_users(users):
    processed_users = []

    for user in users:
        if not isinstance(user, dict):
            continue

        user_id = user.get("id")
        name = user.get("name")
        email = user.get("email")
        address = user.get("address")

        if not isinstance(user_id, int) or isinstance(user_id, bool):
            continue

        if not isinstance(name, str) or not name.strip():
            continue

        if not isinstance(email, str) or not email.strip():
            continue

        if not isinstance(address, dict):
            continue

        city = address.get("city")

        if not isinstance(city, str) or not city.strip():
            continue

        processed_users.append({
            "id": user_id,
            "name": name.strip(),
            "email": email.strip(),
            "city": city.strip()
        })

    return processed_users


def main():
    for call_number in range(1, 4):
        print(f"\n========== CALL {call_number} ==========")

        users = get_cached_users()
        processed_users = process_users(users)

        print("Data source:", cache_source)
        print("Total valid users:", len(processed_users))

        for user in processed_users:
            print(
                f"{user['id']}. {user['name']} | "
                f"{user['email']} | {user['city']}"
            )


if __name__ == "__main__":
    main()
