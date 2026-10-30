import pytest
import app
import requests
from unittest.mock import patch,call,Mock
from copy import deepcopy

# @pytest.fixture
# def users():
#     return [
#     {"id": 1, "name": "Hunter", "active": True},
#     {"id": 2, "name": "Alex", "active": False},
#     {"id": 3, "name": "Sarah", "active": True}
# ]

# def test_total_users(users):
#     assert len(users) == 3

# def test_active_users(users):
#     result = sum(1 for user in users if user["active"] is True)
#     assert result == 2







# def is_adult(age):
#     return age >= 18


# @pytest.mark.parametrize("age, result", [
#     (18, True),
#     (25, True),
#     (17, False),
#     (0, False),
#     (-1, False)
# ])

# def test_age(age, result):
#     assert is_adult(age) == result







# def validate_username(username):
#     if not username:
#         raise ValueError("Username cannot be empty")

#     return True

# @pytest.mark.parametrize("username",[""])
# def test_username_error(username):
#     with pytest.raises(ValueError, match="Username cannot be empty"):
#         validate_username(username)








# def validate_username(username):
#     if not username:
#         raise ValueError("Username cannot be empty")

#     return True

# @pytest.mark.parametrize("username", [
#     "Hunter",
#     "Alex"
# ])
# def test_valid_username(username):
#     assert validate_username(username) is True

# @pytest.mark.parametrize("username", [
#     "",
#     None,
#     0
# ])
# def test_invalid_username(username):
#     with pytest.raises(ValueError, match="Username cannot be empty"):
#         validate_username(username)







# def calculate_shipping(weight):
#     if weight <= 0:
#         raise ValueError("Weight must be positive")

#     if weight <= 5:
#         return 5

#     return 10

# @pytest.mark.parametrize("weight", [
#     0,
#     -1
# ])
# def test_invalid_weight(weight):
#     with pytest.raises(ValueError, match="Weight must be positive"):
#         calculate_shipping(weight)

# @pytest.mark.parametrize("weight, expected", [
#     (0.1, 5),
#     (5, 5),
#     (5.1, 10)
# ])
# def test_valid_weight(weight, expected):
#     assert calculate_shipping(weight) == expected







# def clean_names(names):
#     return [name.strip() for name in names]


# def test_clean_names_does_not_modify_input():
#     names = [" Hunter ", " Alex "]
#     backup = deepcopy(names)

#     results = clean_names(names)

#     assert results == ["Hunter", "Alex"]
#     assert names == backup








# def test_notify_user():
#     with patch("app.send_email") as mock_send:
#         app.notify_user("alex@example.com")

#         mock_send.assert_called_once_with(
#             "alex@example.com",
#             "Your account was created"
#         )









# def test_register_user_logs_events_in_order():
#     with patch("app.log_event") as mock_log:
#         app.register_user()

#         assert mock_log.call_args_list == [
#             call("User validation started"),
#             call("User created"),
#             call("Welcome email scheduled")
#         ]








# def test_fetch_user():
#     with patch("app.requests.get") as mock_get:
#         mock_response = mock_get.return_value

#         mock_response.json.return_value = {
#             "id": 7,
#             "name": "Alex"
#         }

#         result = app.fetch_data()

#         assert result == {
#             "id": 7,
#             "name": "Alex"
#         }

#         mock_get.assert_called_once_with(
#             "www.example.com/users/1",
#             timeout = 5
#         )

#         mock_response.raise_for_status.assert_called_once()








# def test_fetch_user_http_error():
#     with patch("app.requests.get") as mock_get:
#         mock_response = mock_get.return_value
#         mock_response.raise_for_status.side_effect = (
#             requests.HTTPError("error 404")
#         )

#         with pytest.raises(requests.HTTPError, match="error 404"):
#             app.fetch_data()

#         mock_response.raise_for_status.assert_called_once()







# def test_fetch_user_timeout():
#     with patch("app.requests.get") as mock_get:
#         mock_get.side_effect = requests.Timeout("request timed out")

#         with pytest.raises(requests.Timeout, match="request timed out"):
#             app.fetch_data()

#         mock_get.assert_called_once_with(
#             "www.example.com/users/1",
#             timeout = 5
#         )





# def test_fetch_user_connection_error_returns_none():
#     with patch("app.requests.get") as mock_get:
#         mock_get.side_effect = requests.ConnectionError("connection failed")

#         result = app.fetch_user()
#         assert result == None
#         mock_get.assert_called_once()





# def test_fetch_user_invalid_format():
#     with patch("app.requests.get") as mock_get:
#         response = mock_get.return_value

#         response.json.return_value = ["Hunter", "Alex"]
#         result = app.fetch_user()

#         assert result == None
#         response.raise_for_status.assert_called_once()




# def test_fetch_user_success():
#     with patch("app.requests.get") as mock_get:
#         mock_response = mock_get.return_value

#         mock_response.json.return_value = {"id": 1, "name": "Hunter"}
#         result = app.fetch_user()

#         assert result == {"id": 1, "name": "Hunter"}
#         mock_response.raise_for_status.assert_called_once()





# def test_fetch_user_request():
#     with patch("app.requests.get") as mock_get:
#         mock_response = mock_get.return_value

#         mock_response.json.return_value = {"id": 1, "name": "Hunter"}
#         result = app.fetch_user()

#         mock_get.assert_called_once_with(
#             "https://example.com/users/1",
#             timeout= 5
#         )

#         assert result == {"id": 1, "name": "Hunter"}







# def test_fetch_user_headers():
#     with patch("app.requests.get") as mock_get:
#         mock_response = mock_get.return_value

#         mock_response.json.return_value = {"id": 1, "name": "Hunter"}
#         result = app.fetch_user()

#         assert result == {"id": 1, "name": "Hunter"}
#         assert mock_get.call_count == 1
#         mock_get.assert_called_once()

#         mock_get.assert_called_once_with(
#             "https://example.com/users/1",
#             headers= {
#                 "Accept": "application/json"
#             },
#             timeout= 5
#         )







# def test_get_user_name():
#     with patch("app.fetch_user") as mock_fetch_user:
#         mock_fetch_user.return_value = {"id": 1, "name": "Hunter"}

#         result = app.get_user_name()
#         assert result == "Hunter"

#         mock_fetch_user.assert_called_once()







# def test_get_user_name_missing():
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.return_value = None

#         result = app.get_user_name()

#         assert result == None
#         mock_fetch.assert_called_once()






# def test_get_user_name_missing_field():
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.return_value = {"id": 1}

#         result = app.get_user_name()

#         assert result == None
#         mock_fetch.assert_called_once()





# def test_get_user_name_multiple_calls():
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.side_effect = [
#             {"id": 1, "name": "Hunter"},
#             None
#         ]

#         first_result = app.get_user_name()
#         second_result = app.get_user_name()

#         assert first_result == "Hunter"
#         assert second_result == None

#         assert mock_fetch.call_count == 2





# def test_get_user_name_exception():
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.side_effect = ValueError("somthing went wrong")

#         with pytest.raises(ValueError, match="somthing went wrong"):
#             app.get_user_name()

#         mock_fetch.assert_called_once()






# def test_get_user_name_handles_exception():
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.side_effect = ValueError("somthing went wrong")

#         result = app.get_user_name()

#         assert result == None
#         mock_fetch.assert_called_once()







# def test_get_user_name_unexpected_exception():
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.side_effect = TypeError("unexpected error")

#         with pytest.raises(TypeError, match="unexpected error"):
#             app.get_user_name()

#         mock_fetch.assert_called_once()







# @pytest.fixture
# def sample_user():
#     return {"id": 1, "name": "Hunter"}

# def test_get_user_name_with_fixture(sample_user):
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.return_value = sample_user

#         result = app.get_user_name()

#         assert result == "Hunter"
#         mock_fetch.assert_called_once()









# @pytest.fixture
# def user_without_name():
#     return {"id": 1}


# def test_get_user_name_missing_name_with_fixture(user_without_name):
#     with patch("app.fetch_app") as mock_fetch:
#         mock_fetch.return_value = user_without_name

#         result = app.get_user_name()

#         assert result == None
#         mock_fetch.assert_called_once()





# @pytest.fixture
# def sample_user():
#     return {"id": 1, "name": "Hunter"}

# def test_sample_user_name(sample_user):
#     assert sample_user["name"] == "Hunter"

# def test_sample_user_id(sample_user):
#     assert sample_user["id"] == 1




# @pytest.fixture
# def sample_user():
#     name = {"id": 1, "name": "Hunter"}
#     yield name
#     name["name"] = "cleaned"

# def test_sample_user(sample_user):
#     assert sample_user["name"] == "Hunter"



# @pytest.fixture
# def sample_user():
#     user = {"id": 1, "name": "Hunter"}

#     yield user

#     user["name"] = "Cleaned"

# def test_sample_user_id():
#     assert sample_user["id"] == 1





# @pytest.fixture
# def sample_user():
#     return []

# def test_sample_list_add(sample_user):
#     sample_user.append("Hunter")
#     assert sample_user == ["Hunter"]

# def test_sample_list_is_empty(sample_user):
#     assert sample_user == []





# @pytest.fixture
# def sample_user():
#     return []

# def test_sample_list_is_fresh(sample_user):
#     sample_user.append("Alex")
#     assert sample_user == ["Alex"]




# @pytest.fixture(scope="module")
# def shared_list():
#     return []

# def test_shared_list_add(shared_list):
#     shared_list.append("Hunter")
#     assert shared_list == ["Hunter"]

# def test_shared_list_persists(shared_list):
#     assert shared_list == ["Hunter"]






# @pytest.mark.parametrize("name", ["Hunter", "Alex", "Sam"])
# def test_get_user_name_parametrized(name):
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.return_value = {"id":1, "name":name}

#         result = app.get_user_name()

#         assert result == name

#         mock_fetch.assert_called_once()







# @pytest.mark.parametrize(
#     "user , expected",
#     [
#     ({"id": 1, "name": "Hunter"}, "Hunter"),
#     ({"id": 2, "name": "Alex"}, "Alex")
# ])

# def test_get_user_name_multiple_users(user, expected):
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.return_value = user

#         result = app.get_user_name()

#         assert result == expected
#         mock_fetch.assert_called_once()




# @pytest.mark.parametrize("username",[None, {"id":1}])
# def test_get_user_name_missing_values(username):
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.return_value = username

#         result = app.get_user_name()

#         assert result == None
#         mock_fetch.assert_called_once()



# @pytest.mark.parametrize(
#     "username",
#     [None, {"id": 1}],
#     ids=["no-user", "missing-name"]
# )
# def test_get_user_name_missing_values(username):
#     with patch("app.fetch_user") as mock_fetch:
#         mock_fetch.return_value = username

#         result = app.get_user_name()

#         assert result == None
#         mock_fetch.assert_called_once()



# @pytest.mark.parametrize(
#     "username",
#     ["", None],
#     ids=["empty-string", "none"]
# )
# def test_validate_username_invalid(username):
#         with pytest.raises(ValueError, match="Username is required"):
#             app.validate_username(username)




# @pytest.mark.parametrize(
#     "name",
#     ["Hunter", "Alex", "Sam"],
#     ids=["hunter", "alex", "sam"]
# )
# def test_validate_username_valid(name):
#     result = app.validate_username(name)

#     assert result == name




# @pytest.mark.parametrize(
#     "character",
#     ["A", "AB"],
#     ids=["one-character", "two-characters"]
# )
# def test_validate_username_too_short(character):
#     with pytest.raises(ValueError, match="Username must contain at least 3 characters"):
#         app.validate_username(character)





# @pytest.mark.parametrize(
#     "name",
#     ["ABC", "Hunter"],
#     ids=["min-length", "longer-name"]
# )
# def test_validate_username_too_short(name):
#     result = app.validate_username(name)

#     assert result == name







# @pytest.mark.parametrize(
#     "username",
#     ["AB", "ABC", "ABCD", ""],
#     ids=["too-short", "minimum-valid", "above-minimum", "empty"]
# )
# def test_validate_username_boundary(username):
#     if len(username) < 3:
#         with pytest.raises(
#             ValueError,
#             match="Username must contain at least 3 characters"
#         ):
#             app.validate_username(username)
#     else:
#         result = app.validate_username(username)
#         assert result == username





# @pytest.mark.parametrize(
#     "name, is_valid",
#     [("A", False),
#      ("ABC", True),
#      ("Hunter", True),
#      ("", False)
#     ],
#     ids=[
#     "one-character",
#     "minimum-valid",
#     "longer-valid",
#     "empty"
#     ]
# )
# def test_validate_username_expected_results(name, is_valid):
#     if is_valid:
#         assert app.validate_username(name) == name
#     else:
#         with pytest.raises(ValueError):
#             app.validate_username(name)








# @pytest.mark.parametrize(
#     "username",
#     [
#         pytest.param("ABC", id="valid-minimum"),
#         pytest.param("Hunter", id="valid-longer"),
#         pytest.param("AB", id="invalid-short"),
#     ]
# )
# def test_validate_username_with_case_ids(username):
#     if username == "AB":
#         with pytest.raises(ValueError):
#             app.validate_username(username)
#     else:
#         assert app.validate_username(username) == username



# @pytest.mark.xfail(reason= "Known bug: uppercase conversion is not implemented")
# def test_normalize_username_uppercase_bug():
#     result = app.normalize_username(" HUNTER ")
#     assert result == "hunter123"



# @pytest.mark.xfail(reason="Known bug", strict=True)
# def test_normalize_username_strict_xfail():
#     result = app.normalize_username(" HUNTER ")

#     assert result == "hunter123"


# @pytest.mark.skip(reason="Feature is not ready")
# def test_normalize_username_skipped():
#     result = app.normalize_username(" HUNTER ")

#     assert result == "hunter"


# def test_add():
#     assert app.add(2, 3) == 5


# def test_subtract():
#     assert app.subtract(5, 3) == 2


# def test_multiply():
#     assert app.multiply(2, 3) == 6


# def test_divide():
#     assert app.divide(6, 2) == 3

# def test_divivde_by_zero():
#     with pytest.raises(ValueError):
#         app.divide(0, 10)








# @pytest.mark.parametrize("num, expectation",
#     [
#         (2, True),
#         (7, False),
#         (0, True),
#         (-4, True),
#         (-3, False),
#     ]
# )
# def test_even_number(num, expectation):
#     assert app.is_even(num) == expectation






# def test_add_tag():
#     original = {
#         "name": "anyone",
#         "tags": ["python"]
#     }
#     user = {
#         "name": "anyone",
#         "tags": ["python"]
#     }

#     result = app.add_tag(user, "testing")

#     assert result == {
#         "name": "anyone",
#         "tags": ["python", "testing"]
#     }

#     assert user == original





# def test_register_user():
#     with patch("app.save_user") as mock_save_user:
#         result = app.register_user("Hunter@gmail.com")

#         assert result == {
#             "email": "Hunter@gmail.com",
#             "saved": True
#         }
#         mock_save_user.assert_called_once_with("Hunter@gmail.com")




# def test_read_report(tmp_path):
#     report_path = tmp_path / "report.text"
#     report_path.write_text("testing", encoding="utf-8")


#     result = app.read_report(report_path)
#     assert result == "testing"



# def test_missing_report(tmp_path):
#     report_path = tmp_path / "missing_report.text"
#     with pytest.raises(FileNotFoundError):
#         app.read_report(report_path)



# def test_fetch_product():
#     fake_fetch = Mock()
#     fake_fetch.json.return_value = {
#         "id": 3,
#         "product": "keyboard"
#     }

#     with patch("app.requests.get", return_value=fake_fetch) as mock_get:
#         result = app.fetch_product(3)

#     assert result == {
#         "id": 3,
#         "product": "keyboard"
#     }
#     mock_get.assert_called_once_with(
#         "https://api.example.com/products/3",
#         timeout= 5
#     )



# def test_fetch_product_http_error():
#     fake_response = Mock()
#     fake_response.raise_for_status.side_effect = requests.HTTPError("error 404")

#     with patch("app.requests.get", return_value=fake_response):
#         with pytest.raises(requests.HTTPError):
#             app.fetch_product(3)



# def test_fetch_with_retry():
#     fake_response = Mock()
#     fake_response.json.return_value = {"status": "ok"}

#     with patch("app.requests.get") as mock_get:
#         mock_get.side_effect = [
#             requests.ConnectionError("temporary failure"),
#             fake_response
#         ]
#         result = app.fetch_with_retry("https://api.example.com/status")

#     assert result == {"status": "ok"}
#     assert mock_get.call_count == 2


# def test_get_cached_data():
#     app.cache_data = {"users": ["olduser"]}
#     app.cache_time = 100

#     fake_response = Mock()
#     fake_response.json.return_value = {"users": ["newuser"]}

#     with patch("app.time.monotonic", return_value=170):
#         with patch("app.requests.get", return_value=fake_response) as mock_get:
#             result = app.get_cached_data()

#     assert result == {"users": ["newuser"]}
#     mock_get.assert_called_once_with(
#         "https://api.example.com/users",
#         timeout=5
#     )
#     fake_response.raise_for_status.assert_called_once()



# def test_get_cached_data():
#     app.cache_data = {"users": ["olduser"]}
#     app.cache_time = 100

#     fake_response = Mock()
#     fake_response.raise_for_status.side_effect = requests.HTTPError("tomporary failure")

#     with patch("app.time.monotonic", return_value=170):
#         with patch("app.requests.get", return_value=fake_response) as moke_get:
#             with pytest.raises(requests.HTTPError):
#                 app.get_cached_data()

#     assert app.cache_data == {"users": ["olduser"]}
#     assert app.cache_time == 100




# def test_porcess_response():
#     response = Mock()
#     response.json.return_value = {"users": ["firstuser"]}

#     result = app.process_response(response)

#     assert result == {"users": ["firstuser"]}
#     assert response.mock_calls == [
#         call.raise_for_status(),
#         call.json()
#     ]




# def test_get_api_url_costum(monkeypatch):
#     monkeypatch.setenv(
#         "API_URL",
#         "https://test.example.com"
#     )

#     assert app.get_api_url() == "https://test.example.com"

# def test_get_api_url_default(monkeypatch):
#     monkeypatch.delenv("API_URL", raising=False)

#     assert app.get_api_url() == "https://api.example.com"




# def test_save_user_data(tmp_path):
#     file_path = tmp_path / "user.text"

#     app.save_user_data(file_path, "username=Hunter")

#     assert file_path.exists()
#     assert file_path.read_text(encoding="utf-8") == "username=Hunter"





# @pytest.mark.parametrize("age", [
#     0,
#     1,
#     25,
#     120
# ])
# def test_valid_age(age):
#     assert app.validate_age(age) == True

# @pytest.mark.parametrize("age", [
#     -1,
#     121
# ])
# def test_invalid_age(age):
#     with pytest.raises(ValueError, match="age must be between 0 and 120"):
#         app.validate_age(age)

# @pytest.mark.parametrize("age", [
#     25.5,
#     "25",
#     None,
#     True
# ])
# def test_invalid_type_age(age):
#     with pytest.raises(TypeError, match="age must be integer"):
#         app.validate_age(age)






# @pytest.mark.parametrize(
#     "numbers, expected",
#     [
#         ([10, 20, 30], 20),
#         ([-10, 0, 10], 0),
#         ([42], 42),
#     ],
# )
# def test_calculate_average_valid(numbers, expected):
#     assert app.calculate_average(numbers) == expected


# def test_calculate_average_empty_list():
#     with pytest.raises(
#         ValueError,
#         match="^Numbers cannot be empty$",
#     ):
#         app.calculate_average([])


# def test_calculate_average_not_a_list():
#     with pytest.raises(
#         TypeError,
#         match="^Numbers must be a list$",
#     ):
#         app.calculate_average("10,20,30")


# @pytest.mark.parametrize(
#     "numbers",
#     [
#         [10, "20", 30],
#         [10, True, 30],
#     ],
# )
# def test_calculate_average_invalid_values(numbers):
#     with pytest.raises(
#         TypeError,
#         match="^All values must be numbers$",
#     ):
#         app.calculate_average(numbers)









# def test_not_dict():
#     with pytest.raises(TypeError, match="^User must be a dictionary$"):
#         app.get_user_name("hi")


# def test_profile_missing():
#     with pytest.raises(ValueError, match="^Profile is missing$"):
#         app.get_user_name({"id": 1})


# def test_profile_not_dict():
#     with pytest.raises(TypeError, match="^Profile must be a dictionary$"):
#         app.get_user_name({"id": 1, "profile": []})


# def test_name_missing():
#     with pytest.raises(ValueError, match="^Name is missing$"):
#         app.get_user_name({"id": 1, "profile": {"last_name": "unknown"}})


# @pytest.mark.parametrize("name", ["", "   ", True, None, 123])
# def test_invalid_name(name):
#     with pytest.raises(
#         ValueError,
#         match="^Name must be a non-empty string$",
#     ):
#         app.get_user_name({"id": 1, "profile": {"name": name}})


# def test_valid_name():
#     user = {"id": 1, "profile": {"name": "  Hunter  "}}

#     assert app.get_user_name(user) == "Hunter"






# def test_removed_password():
#     user = {"name": "Hunter", "password": "secret123"}
#     result = app.remove_password(user)

#     assert result == {"name": "Hunter"}
#     assert "password" not in result


# def test_orginal_unchanged():
#     user = {"name": "Hunter", "password": "secret123"}
#     original = deepcopy(user)

#     app.remove_password(user)

#     assert user == original


# def test_nested_data_unchanged():
#     user = {
#         "name": "Hunter",
#         "password": "secret123",
#         "profile": {"skills": ["Python", "SQL"]}
#     }
#     orginal = deepcopy(user)

#     result = app.remove_password(user)

#     assert result == {
#         "name": "Hunter",
#         "profile": {"skills": ["Python", "SQL"]}
#     }
#     assert user == orginal


# def test_nested_data_is_independent():
#     user = {
#         "name": "Hunter",
#         "password": "secret123",
#         "profile": {"skills": ["Python"]}
#     }

#     result = app.remove_password(user)
#     result["profile"]["skills"].append("SQL")


# def test_missing_password():
#     user = {"name": "Hunter"}

#     result = app.remove_password(user)

#     assert result == user
#     assert result is not user









# @pytest.mark.parametrize(
#     "scores, expected",
#     [
#         ([30, 10, 20], [10, 20, 30]),
#         ([10, 20, 30], [10, 20, 30]),
#         ([], []),
#         ([42], [42]),
#         ([-10, 0, 10], [-10, 0, 10]),
#         ([5, 2, 5], [2, 5, 5]),
#     ],
# )
# def test_valid_scores(scores, expected):
#     original = scores.copy()

#     result = app.sort_scores(scores)

#     assert result == expected
#     assert scores == original
#     assert result is not scores


# @pytest.mark.parametrize(
#     "scores, message",
#     [
#         ("hb", "^Scores must be a list$"),
#         (["hi", "by"], "^All scores must be numbers$"),
#         ([True, 10], "^All scores must be numbers$"),
#     ],
# )
# def test_invalid_scores(scores, message):
#     with pytest.raises(TypeError, match=message):
#         app.sort_scores(scores)






# @pytest.mark.parametrize("items, page, page_size, expected", [
#     (["A", "B", "C", "D", "E"], 2, 2, ["C", "D"]),
#     (["A", "B", "C", "D", "E"], 3, 2, ["E"]),
#     (["A", "B", "C", "D", "E"], 4, 2, []),
#     ([], 2, 2, [])
# ])
# def test_valide_list(items, page, page_size, expected):
#     backup = deepcopy(items)

#     result = app.get_page(backup, page, page_size)

#     assert result == expected
#     assert backup == items


# @pytest.mark.parametrize("items, page, page_size, expected", [
#     (["A", "B", "C", "D", "E"], 0, 2, "page must be a positive integer"),
#     (["A", "B", "C", "D", "E"], -1, 2, "page must be a positive integer"),
#     (["A", "B", "C", "D", "E"], True, 2, "page must be a positive integer"),
#     (["A", "B", "C", "D", "E"], 1.5, 2, "page must be a positive integer"),
# ])
# def test_invalide_page(items, page, page_size, expected):
#     with pytest.raises(ValueError, match=expected):
#         app.get_page(items, page, page_size)

# @pytest.mark.parametrize("items, page, page_size, expected", [
#     (["A", "B", "C", "D", "E"], 2, 0, "page size must be a positive integer"),
#     (["A", "B", "C", "D", "E"], 2, -1, "page size must be a positive integer"),
#     (["A", "B", "C", "D", "E"], 2, False, "page size must be a positive integer"),
#     (["A", "B", "C", "D", "E"], 2, 2.5, "page size must be a positive integer"),
# ])
# def test_invalide_page_size(items, page, page_size, expected):
#     with pytest.raises(ValueError, match=expected):
#         app.get_page(items, page, page_size)


# @pytest.mark.parametrize("items, page, page_size, expected", [
#     ("hi", 2, 2, "items must be a list"),
#     (True, 2, 2, "items must be a list")
# ])
# def test_non_list_input(items, page, page_size, expected):
#     with pytest.raises(TypeError, match=expected):
#         app.get_page(items, page, page_size)







# from datetime import datetime, timedelta, time

# now = datetime.now()
# one_minute_before = now - timedelta(minutes=1)


# @pytest.mark.parametrize("expiry_time, now, expected", [
#     (now, one_minute_before, False),
#     (now, now, True),
# ])
# def test_expiration(expiry_time, now, expected):
#     result = app.is_expired(expiry_time, now)

#     assert result == expected


# @pytest.mark.parametrize("expiry_time, now", [
#     ("hello", now),
#     (now, None)
# ])
# def test_invalid_expiry_time(expiry_time, now):
#     with pytest.raises(TypeError, match="both value must be datetime objects"):
#         app.is_expired(expiry_time, now)








# VALID_DATA = {
#     "id": 12,
#     "title": "keyboard",
#     "price": 49.99
# }

# @patch("app.requests.get")
# def test_get_product_success(mock_get):
#     response = Mock()
#     response.json.return_value = VALID_DATA
#     mock_get.return_value = response

#     result = app.get_product(12)

#     assert result == VALID_DATA
#     mock_get.assert_called_once_with(
#         "https://api.example.com/products/12",
#         timeout=5
#     )
#     response.raise_for_status.assert_called_once_with()

# @patch("app.requests.get")
# def test_strip_title(mock_get):
#     response = Mock()
#     response.json.return_value = {
#         "id": 12,
#         "title": "  keyboard  ",
#         "price": 49.99
#     }
#     mock_get.return_value = response

#     result = app.get_product(12)

#     assert result["title"] == "keyboard"


# @pytest.mark.parametrize("invalid_data", [
#     {"title": "Keyboard", "price": 49.99},
#     {"id": 0, "title": "Keyboard", "price": 49.99},
#     {"id": True, "title": "Keyboard", "price": 49.99},
#     {"id": 12, "title": "", "price": 49.99},
#     {"id": 12, "title": "   ", "price": 49.99},
#     {"id": 12, "title": 123, "price": 49.99},
#     {"id": 12, "title": "Keyboard", "price": -1},
#     {"id": 12, "title": "Keyboard", "price": False},
#     {"id": 12, "title": "Keyboard"},
#     ["not", "a", "dictionary"],
#     ids=[
#         "missing-id",
#         "zero-id",
#         "boolean-id",
#         "empty-title",
#         "whitespace-title",
#         "non-string-title",
#         "negative-price",
#         "boolean-price",
#         "missing-price",
#         "non-dictionary",
#     ],
# ])
# @patch("app.request.get")
# def test_invalid_product(mock_get ,invalid_data):
#     response = Mock()
#     response.json.return_value = invalid_data
#     mock_get.return_value = response

#     with pytest.raises(ValueError, match="Invalid product data"):
#         app.get_product(12)


# @patch("app.requests.get")
# def test_http_error(mock_get):
#     response = Mock()
#     response.raise_for_status.side_effect = requests.HTTPError("server error")
#     mock_get.return_value = response

#     with pytest.raises(requests.HTTPError, match="Server error"):
#         app.get_product(12)

#     response.json.assert_not_called()









import sqlite3

# @pytest.fixture
# def connection():
#     conn = sqlite3.connect(":memory:")
#     app.create_user_table(conn)

#     yield conn

#     conn.close


# def test_create_users_table(connection):
#     result = connection.execute(
#         "SELECT name FROM sqlite_master "
#         "WHERE type = 'table' AND name = 'users'"
#     ).fetchone()

#     assert result == ("users",)











# @pytest.fixture
# def connection():
#     conn = sqlite3.connect(":memory:")
#     app.create_accounts_table(conn)

#     conn.executemany(
#         "INSERT INTO accounts (id, balance) VALUES (?, ?)",
#         [(1, 500.0), (2, 100.0)],
#     )
#     conn.commit()

#     yield conn

#     conn.close()


# def get_balance(connection, account_id):
#     return connection.execute(
#         "SELECT balance FROM accounts WHERE id = ?",
#         (account_id,),
#     ).fetchone()[0]


# def test_valid_transaction(connection):
#     result = app.transfer_money(connection, 1, 2, 200)

#     assert get_balance(connection, 1) == 300.0
#     assert get_balance(connection, 2) == 300.0
#     assert result == 300.0


# def test_missing_sender_rolls_back(connection):
#     with pytest.raises(ValueError, match="^Account not found$"):
#         app.transfer_money(connection, 99, 2, 200)

#     assert get_balance(connection, 2) == 100.0


# def test_missing_receiver_rolls_back(connection):
#     with pytest.raises(ValueError, match="^Account not found$"):
#         app.transfer_money(connection, 1, 99, 200)

#     assert get_balance(connection, 1) == 500.0


# def test_insufficient_balance(connection):
#     with pytest.raises(ValueError, match="^Insufficient balance$"):
#         app.transfer_money(connection, 1, 2, 600)

#     assert get_balance(connection, 1) == 500.0
#     assert get_balance(connection, 2) == 100.0


# def test_unexpected_database_error_rolls_back(connection):
#     connection.execute("BEGIN")

#     original_execute = connection.execute
#     calls = 0

#     def failing_execute(sql, parameters=()):
#         nonlocal calls
#         if sql.startswith("UPDATE") and "balance + ?" in sql:
#             raise sqlite3.OperationalError("Simulated database failure")
#         return original_execute(sql, parameters)

#     connection.execute = failing_execute

#     with pytest.raises(
#         sqlite3.OperationalError,
#         match="Simulated database failure",
#     ):
#         app.transfer_money(connection, 1, 2, 200)

#     connection.execute = original_execute

#     assert get_balance(connection, 1) == 500.0
#     assert get_balance(connection, 2) == 100.0











@pytest.fixture
def connection():
    conn = sqlite3.connect(":memory:")
    app.create_products_table(conn)

    yield conn

    conn.close()


def test_add_valid_product(connection):
    product_id = app.add_product(
        connection,
        "Keyboard",
        49.99,
    )

    result = connection.execute(
        "SELECT id, name, price FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    assert result == (product_id, "Keyboard", 49.99)


def test_add_two_different_products(connection):
    first_id = app.add_product(connection, "Keyboard", 49.99)
    second_id = app.add_product(connection, "Mouse", 19.99)

    assert first_id != second_id

    result = connection.execute(
        "SELECT COUNT(*) FROM products"
    ).fetchone()

    assert result[0] == 2


def test_duplicate_product_name(connection):
    app.add_product(connection, "Keyboard", 49.99)

    with pytest.raises(sqlite3.IntegrityError):
        app.add_product(connection, "Keyboard", 59.99)

    result = connection.execute(
        "SELECT COUNT(*) FROM products"
    ).fetchone()

    assert result[0] == 1


@pytest.mark.parametrize("price", [0, -10, -0.01])
def test_invalid_price(connection, price):
    with pytest.raises(sqlite3.IntegrityError):
        app.add_product(connection, "Keyboard", price)

    result = connection.execute(
        "SELECT COUNT(*) FROM products"
    ).fetchone()

    assert result[0] == 0


def test_missing_name(connection):
    with pytest.raises(sqlite3.IntegrityError):
        app.add_product(connection, None, 49.99)

    result = connection.execute(
        "SELECT COUNT(*) FROM products"
    ).fetchone()

    assert result[0] == 0


def test_failed_insertion_preserves_existing_product(connection):
    app.add_product(connection, "Keyboard", 49.99)

    with pytest.raises(sqlite3.IntegrityError):
        app.add_product(connection, "Keyboard", 100)

    result = connection.execute(
        "SELECT name, price FROM products"
    ).fetchall()

    assert result == [("Keyboard", 49.99)]
