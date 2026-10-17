# from copy import deepcopy
# from main import process_users

# def test_valid_user_is_clean():
#     users = [
#         {
#             "id": 1,
#             "name": "  Hunter  ",
#             "email": "  hunter@example.com  ",
#             "address": {"city": "  Algiers  "}
#         }
#     ]

#     results = process_users(users)

#     assert results == [
#         {
#             "id": 1,
#             "name": "Hunter",
#             "email": "hunter@example.com",
#             "city": "Algiers"
#         }
#     ]

# def test_user_missing_email_is_skipped():
#     users = [
#         {
#             "id": 1,
#             "name": "Hunter",
#             "address": {"city": "Algiers"}
#         }
#     ]

#     results = process_users(users)

#     assert results == []

# def test_invalid_id_is_skipped():
#     users = [
#         {
#             "id": True,
#             "name": "Hunter",
#             "email": "hunter@example.com",
#             "address": {"city": "Algiers"}
#         }
#     ]

#     results = process_users(users)

#     assert results == []

# def test_invalid_and_valid_users():
#     users = [
#         {
#             "id": 1,
#             "name": "Hunter",
#             "email": "hunter@example.com",
#             "address": {"city": "Algiers"}
#         },
#         None,
#         {
#             "id": 2,
#             "name": "Alex",
#             "address": {"city": "Berlin"}
#         }
#     ]

#     results = process_users(users)

#     assert len(results) == 1
#     assert results[0]["name"] == "Hunter"


# def test_empty_list():
#     assert process_users([]) == []


# def test_original_data_is_not_modified():
#     users = [
#         {
#             "id": 1,
#             "name": "  Hunter  ",
#             "email": "hunter@example.com",
#             "address": {"city": "Algiers"}
#         }
#     ]

#     backup = deepcopy(users)
#     results = process_users(users)

#     assert users == backup
#     assert results != users or backup
    