class User:
    user_count = 0
    def __init__(self, username):
        self.username = username
        User.user_count = User.user_count + 1


u1 = User("johnsmith10")
u2 = User("smithjohn20")

print(User.user_count)
