from copy import deepcopy

# player = {
#     "name": "hunter",
#     "level": 10
# }

# backup = deepcopy(player)
# player["level"] = 20

# assert player["level"] == 20
# assert backup["level"] == 10

# print("all test passed")

# player = {
#     "name": "Hunter",
#     "stats": {
#         "level": 10
#     }
# }

# backup = deepcopy(player)
# player["stats"]["level"] = 20

# assert player["stats"]["level"] == 20
# assert backup["stats"]["level"] == 10

# print("all test pass")




# def get_player_name(player):
#     return player["name"].strip().lower()

# player = {"name": "  Hunter  "}
# backup = deepcopy(player)

# name = get_player_name(player)

# assert name == "hunter"
# # assert backup["name"] == "hunter"

# print("all test pass")



# def level_up(player):
#     player["level"] += 1
#     return player

# player = {"name": "Hunter", "level": 10}
# backup = deepcopy(player)


# level_up(player)
# assert player["level"] == 11
# # assert backup == player

# print("all test pass")



# def cleaned_user(user):
#     return {
#         "name": user["name"].strip(),
#         "email": user["email"].strip()
#     }

# user = {
#     "name": "  Hunter  ",
#     "email": " hunter@example.com "
# }
# backup = deepcopy(user)

# clean_user = cleaned_user(user)

# assert clean_user["name"] == "Hunter"
# assert clean_user["email"] == "hunter@example.com"
# # assert user == backup

# print("all test passed")






# def add_xp(player):
#     updated_player = deepcopy(player)
#     updated_player["xp"] += 100
#     return updated_player


# player = {
#     "name": "Hunter",
#     "xp": 500
# }

# backup = deepcopy(player)

# updated_player = add_xp(player)

# assert updated_player["xp"] == 600
# assert player["xp"] == 500
# assert player == backup
# assert updated_player is not player

# print("All tests passed!")





# def level_up(player):
#     player_copy = deepcopy(player)
#     player_copy["stats"]["level"] += 1
#     player_copy["stats"]["xp"] += 100
#     return player_copy

# player = {
#     "name": "Hunter",
#     "stats": {
#         "level": 10,
#         "xp": 500
#     }
# }

# update_player = level_up(player)

# assert update_player["stats"]["level"] == 11
# assert update_player["stats"]["xp"] == 600
# assert player["stats"]["level"] == 10
# assert player["stats"]["xp"] == 500

# print("all tests passed")




# def level_up(player):
#     player_copy = deepcopy(player)
#     player_copy["stats"]["level"] += 1
#     return player_copy


# players = [
#     {"name": "Hunter", "stats": {"level": 10}},
#     {"name": "Alex", "stats": {"level": 5}}
# ]

# updated_player = level_up(players[0])

# assert updated_player["stats"]["level"] == 11
# assert players[0]["stats"]["level"] == 10
# assert players[1]["stats"]["level"] == 5
# assert updated_player is not players[0]

# print("all tests passed")





# def add_items(inventory, item):
#     inventory_copy = deepcopy(inventory)
#     inventory_copy.append(item)
#     return inventory_copy


# inventory = ["rifle", "armor", "ammo"]

# updated_inventory = add_items(inventory, "medkit")

# assert "medkit" in updated_inventory
# assert "medkit" not in inventory
# assert inventory == ["rifle", "armor", "ammo"]
# assert updated_inventory != inventory

# print("all tests passed")





# def remove_item(inventory, item):
#     inventory_copy = deepcopy(inventory)
#     inventory_copy.remove(item)
#     return inventory_copy

# inventory = ["rifle", "armor", "ammo", "medkit"]

# backup = deepcopy(inventory)

# updated_inventory = remove_item(inventory, "armor")

# assert "armor" not in updated_inventory
# assert "armor" in inventory
# assert inventory == backup
# assert updated_inventory != inventory

# print("all tests pass")




# def remove_item(inventory, item):
#     inventory_copy = deepcopy(inventory)
#     if item in inventory_copy:
#         inventory_copy.remove(item)
#     return inventory_copy

# inventory = ["rifle", "armor", "ammo"]
# backup = deepcopy(inventory)

# updated_inventory1 = remove_item(inventory, "armor")
# assert updated_inventory1 == ["rifle", "ammo"]
# assert inventory == backup

# updated_inventory2 = remove_item(inventory, "medkit")
# assert updated_inventory2 == ["rifle", "armor", "ammo"]
# assert inventory == backup


# print("all tests passed")




# def clean_username(username):
#     return username.strip().lower()

# username1 = "  HUNTER  "
# username2 = "  Alex123 "

# clean_user1 = clean_username(username1)
# clean_user2 = clean_username(username2)

# assert clean_user1 == "hunter"
# assert clean_user2 == "alex123"

# assert username1 == "  HUNTER  "
# assert username2 == "  Alex123 "

# print("all tests passed")

# here we don't need deepcopy becouse only dict and list or nested dict or list are mutable.



# def is_valid_email(email):
#     email = email.strip()
#     if "@" not in email:
#         return False
#     username, domain = email.split("@", 1)
#     if not username or "." not in domain:
#         return False
    
#     return True


# email1 = " hunter@example.com "
# email2 = "alex.example.com"
# email3 = "alex@"
# email4 = "  hello@site.org  "

# assert is_valid_email(email1)
# # assert is_valid_email(email2)
# # assert is_valid_email(email3)
# assert is_valid_email(email4)


# assert email1 == " hunter@example.com "
# assert email2 == "alex.example.com"
# assert email3 == "alex@"
# assert email4 == "  hello@site.org  "

# print("All tests passed!")






# def get_adult_users(users):
#     original_copy = deepcopy(users)

#     adults = [
#         user for user in users
#         if user["age"] >= 18
#     ]

#     assert users == original_copy

#     return adults


# users = [
#     {"name": "Hunter", "age": 25},
#     {"name": "Alex", "age": 16},
#     {"name": "Sam", "age": 18},
#     {"name": "Max", "age": 12}
# ]

# backup = deepcopy(users)

# result = get_adult_users(users)

# assert result == [
#     {"name": "Hunter", "age": 25},
#     {"name": "Sam", "age": 18}
# ]

# assert len(result) == 2
# assert users == backup
# assert result is not users

# print("All tests passed!")






# def get_adult_users(users):
#     adults = deepcopy([
#         user for user in users
#         if user["age"] >= 18
#     ])

#     for user in adults:
#         user["name"] = user["name"].lower()

#     return adults

# users = [
#     {"name": "HUNTER", "age": 25},
#     {"name": "Alex", "age": 16},
#     {"name": "SAM", "age": 18}
# ]

# backup = deepcopy(users)

# adult_users = get_adult_users(users)

# assert adult_users == [
#     {"name": "hunter", "age": 25},
#     {"name": "sam", "age": 18}
# ]
# assert len(adult_users) == 2
# assert backup == users
# assert users[0]["name"] == "HUNTER"
# assert users[2]["name"] == "SAM"

# print("all tests passed :)")




# def get_sorted_adults(users):
#     adults = deepcopy([
#         user for user in users
#         if user["age"] >= 18
#     ])
#     adults.sort(key=lambda user: user["age"])
#     return adults

# users = [
#     {"name": "Hunter", "age": 25},
#     {"name": "Alex", "age": 16},
#     {"name": "Sam", "age": 18},
#     {"name": "Max", "age": 30}
# ]

# backup = deepcopy(users)
# sorted_adults = get_sorted_adults(users)

# assert sorted_adults == [
#     {"name": "Sam", "age": 18},
#     {"name": "Hunter", "age": 25},
#     {"name": "Max", "age": 30}
# ]
# assert [user["age"] for user in sorted_adults] == [18, 25, 30]
# sorted_adults[0]["name"] = "Changed"
# assert users[2]["name"] == "Sam"

# print("all tests passed")





# def get_user_stats(users):
#     total = len(users)
#     average_age = sum(user["age"] for user in users) / total
#     oldest_user = max(users, key=lambda user: user["age"])["name"]

#     return {
#         "total": total,
#         "average_age": average_age,
#         "oldest_user": oldest_user
#     }

# users = [
#     {"name": "Hunter", "age": 25},
#     {"name": "Alex", "age": 16},
#     {"name": "Sam", "age": 19}
# ]

# backup = deepcopy(users)
# resault = get_user_stats(users)

# assert resault["total"] == 3
# assert resault["average_age"] == 20
# assert resault["oldest_user"] == "Hunter"
# assert users == backup

# print("all tests passed")





# def get_user_stats(users):
#     if not users:
#         return None
#     total = len(users)
#     average_age = sum(user["age"] for user in users) / total
#     oldest_user = max(users, key=lambda user: user["age"])["name"]

#     return {
#         "total": total,
#         "average_age": average_age,
#         "oldest_user": oldest_user
#     }

# users = [
#     {"name": "Hunter", "age": 25},
#     {"name": "Alex", "age": 16},
#     {"name": "Sam", "age": 19}
# ]

# backup = deepcopy(users)
# resault = get_user_stats(users)

# assert resault["total"] == 3
# assert resault["average_age"] == 20
# assert resault["oldest_user"] == "Hunter"
# assert users == backup
# assert get_user_stats([]) is None

# print("all tests passed")








# def count_age_groups(users):
#     minors = sum(1 for user in users if user["age"] < 18)
#     adults = sum(1 for user in users if user["age"] >= 18)

#     return {
#         "minors": minors,
#         "adults": adults
#     }


# users = [
#     {"name": "Hunter", "age": 25},
#     {"name": "Alex", "age": 16},
#     {"name": "Sam", "age": 19},
#     {"name": "Max", "age": 12},
#     {"name": "Lina", "age": 35}
# ]

# backup = deepcopy(users)

# results = count_age_groups(users)

# assert results == {"minors": 2, "adults": 3}
# assert count_age_groups([]) == {"minors": 0, "adults": 0}
# assert users == backup

# print("all tests passed")







# from collections import Counter

# def count_by_country(users):
#     countries = Counter(user["country"] for user in users)
#     return dict(countries)


# users = [
#     {"name": "Hunter", "country": "Algeria"},
#     {"name": "Alex", "country": "Germany"},
#     {"name": "Sam", "country": "Algeria"},
#     {"name": "Lina", "country": "France"},
#     {"name": "Max", "country": "Germany"}
# ]

# backup = deepcopy(users)
# countries = count_by_country(users)

# assert countries == {
#     "Algeria": 2,
#     "Germany": 2,
#     "France": 1
# }

# assert count_by_country([]) == {}
# assert users == backup

# print("All tests passed!")






# from collections import Counter

# def get_most_popular_country(users):
#     if not users:
#         return None
#     most_visited = Counter(user["country"] for user in users)
#     most_common_visited = most_visited.most_common(1)[0][0]
#     return most_common_visited
    
# users = [
#     {"name": "Hunter", "country": "Algeria"},
#     {"name": "Alex", "country": "Germany"},
#     {"name": "Sam", "country": "Algeria"},
#     {"name": "Lina", "country": "France"},
#     {"name": "Max", "country": "Germany"},
#     {"name": "Sara", "country": "Algeria"}
# ]

# backup = deepcopy(users)

# result = get_most_popular_country(users)
# print(result)
# assert result == "Algeria"
# assert get_most_popular_country([]) is None
# assert users == backup

# print("all tests passed")






# from collections import Counter

# def analyze_users(users):
#     if not users:
#       return None
#     total = len(users)
#     adult_count = sum(1 for user in users if user["age"] >= 18)
#     average_age = sum(user["age"] for user in users) / total
#     country_count = dict(
#        Counter(
#           user["country"] for user in users
#        )
#     )
#     return {
#         "total_user": total,
#         "adult_count": adult_count,
#         "average_age": average_age,
#         "country_count": country_count
#     }

# users = [
#     {"name": "Hunter", "age": 25, "country": "Algeria"},
#     {"name": "Alex", "age": 16, "country": "Germany"},
#     {"name": "Sam", "age": 19, "country": "Algeria"},
#     {"name": "Lina", "age": 35, "country": "France"},
#     {"name": "Max", "age": 12, "country": "Germany"}
# ]

# backup = deepcopy(users)

# result = analyze_users(users)

# assert result["total_user"] == 5
# assert result["adult_count"] == 3
# assert result["average_age"] == 21.4
# assert result["country_count"] == {
#     "Algeria": 2,
#     "Germany": 2,
#     "France": 1
# }
# assert analyze_users([]) is None
# assert users == backup

# print("all tests passed")



