import requests

# import time

# cached_users = None
# cache_time = 0
# cache_source = "None"

# CACHE_DURATION = 60

# def fetch_users():
#     url = "https://jsonplaceholder.typicode.com/users"
#     headers = {
#         "accept": "application/json"
#     }
#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#         users = response.json()

#         if not isinstance(users, list):
#             print("invalid api response format")
#             return None
        
#         return users
    
#     except requests.RequestException as e:
#         print("api request faild ",e)
#         return None

# def get_cached_users():
#     global cache_source, cache_time, cached_users

#     current_time = time.monotonic()

#     if (
#         cached_users is not None
#         and current_time - cache_time < CACHE_DURATION
#     ):
#         cache_source = "cache"
#         return cached_users

#     fresh_users = fetch_users()

#     if fresh_users is not None:
#         cached_users = fresh_users
#         cache_time = time.monotonic()
#         cache_source = "api"
#         return cached_users

#     if cached_users is not None:
#         cache_source = "stale cache"
#         return cached_users

#     cache_source = "None"
#     return []

# def process_users(users):
#     processed_users = []

#     for user in users:
#         if not isinstance(user, dict):
#             continue

#         user_id = user.get("id")
#         name = user.get("name")
#         email = user.get("email")
#         address = user.get("address")

#         if not isinstance(user_id, int) or isinstance(user_id, bool):
#             continue

#         if not isinstance(name, str) or not name.strip():
#             continue

#         if not isinstance(email, str) or not email.strip():
#             continue

#         if not isinstance(address, dict):
#             continue

#         city = address.get("city")

#         if not isinstance(city, str) or not city.strip():
#             continue

#         processed_users.append({
#             "id": user_id,
#             "name": name.strip(),
#             "email": email.strip(),
#             "city": city.strip()
#         })

#     return processed_users

# def main():
#     for call_number in range(1, 4):
#         print(f"\n========== CALL {call_number} ==========")

#         users = get_cached_users()
#         processed_users = process_users(users)

#         print("data_source: ", cache_source)
#         print("total valid users: ", len(processed_users))

#         for user in processed_users:
#             print(
#                 f"{user['id']}. {user['name']} | "
#                 f"{user['email']} | {user['city']}"
#             )

# if __name__ == "__main__":
#     main()





def fetch_users():
    url = ""
    headers = {
        "accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        users = response.json()

        if not isinstance(users, list):
            print("api request format faild")
            return None

        return users
    except requests.RequestException as e:
        print("api request faild ", e)
        return None

    