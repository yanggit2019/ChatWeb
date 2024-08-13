from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password


# 假设用户信息存储在一个字典中
users = {"1": User("1", "user1", "password1"), "2": User("2", "user2", "password2")}


def get_user(user_id):
    return users.get(user_id)
