from unittest.mock import Mock

# get_age = Mock()

# get_age.return_value = 25

# result = get_age()

# assert result == 25







# send_email = Mock()

# send_email("hunter@example.com")

# send_email.assert_called()
# send_email.assert_called_once()
# send_email.assert_called_with("hunter@example.com")

# print("all tests passed")




# get_user = Mock()

# get_user.return_value = {"id": 1, "name": "Hunter"}

# user = get_user(1)

# print(user)






# get_user = Mock()

# get_user.return_value = {
#     "id": 7,
#     "name": "Alex",
#     "age": 22
# }

# user = get_user(7)

# assert user == {
#     "id": 7,
#     "name": "Alex",
#     "age": 22
# }

# assert user["age"] == 22

# get_user.assert_called_once_with(7)

# print("All tests passed!")




# import pytest

# get_user = Mock()

# get_user.side_effect = ValueError("invalid data")

# with pytest.raises(ValueError):
#     get_user()




# get_user = Mock()

# get_user.side_effect = ["loading", "success"]

# v1 = get_user()
# v2 = get_user()

# assert v1 == "loading"
# assert v2 == "success"

# # get_user.assert_called_once()

# assert get_user.call_count == 2

# print("all tests passed")