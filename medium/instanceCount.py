class User:
    count = 0
    def __init__(self, user):
        self.user = user
        User.count = User.count + 1


u1 = User("johnsmith10")
u2 = User("johnsmith20")

print(User.count)
