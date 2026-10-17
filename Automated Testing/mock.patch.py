from unittest.mock import patch
# from app import get_username

# @patch("app.read_database")
# def test_get_username(mock_database):
#     mock_database.return_value = "Hunter"
#     result = get_username()

#     assert result == "Hunter"



# import app

# def test_get_username():
#     with patch("app.read_database") as mock_database:
#         mock_database.return_value = "Alex"

#     result = app.get_username()
#     assert result == "Alex"
#     mock_database.assert_called_once()




# import pytest
# import app

# def test_database_error():
#     with patch("app.read_database") as mock_database:
#         mock_database.side_effect = RuntimeError("database unavailable")

#         with pytest.raises(RuntimeError, match="database unavailabele"):
#             app.get_username()

#         assert mock_database.assert_called_once()







# import app
# import pytest

# def test_fetch_data():
#     with patch("app.fetch_data") as mock_fetch:
#         mock_fetch.side_effect = [
#             ConnectionError("connection faild"),
#             {"status": "success"}
#         ]

#         with pytest.raises(ConnectionError, match="connection faild"):
#             app.fetch_data()

#         result = app.fetch_data()
#         assert result == {"status": "success"}
#         assert mock_fetch.call_count == 2





# import app

# def test_count_user():
#     with patch("app.fetch_users") as mock_fetch_users:
#         mock_fetch_users.return_value = ["Hunter", "Alex", "Sarah"]

#         result = app.count_users()

#         assert result == 3
#         mock_fetch_users.assert_called_once()





# import app

# def test_count_users_one_user():
#     with patch("app.fetch_users") as mock_fetch_users:
#         mock_fetch_users.return_value = ["Hunter"]

#         result = app.count_users()

#         assert result == 1
#         mock_fetch_users.assert_called_once()