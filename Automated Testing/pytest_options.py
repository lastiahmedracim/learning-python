import pytest

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




