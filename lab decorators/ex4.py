class user:
    users = {}
    logged = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        user.users[username] = password

    @staticmethod
    def check_credentials(username, password):
        if user.users[username] == password:
            return True
        else:
            return False

    @staticmethod
    def login(username, password):
        if user.check_credentials(username, password):
            user.logged[username] = True
            print(f"User <{username}> logged succesfully.")
        else:
            print(f"Failed to login User <{username}>.")

    @staticmethod
    def logout(username):
        user.logged[username] = False

    def __str__(self):
        return f"User: {self.username} - logged in: {user.logged[self.username]}"

    @staticmethod
    def show_users():
        users = [(useritem, user.logged.get(useritem[0], False)) for useritem in user.users.items()]
        loggedusers = [usertuple[0] for usertuple in users if usertuple[1] is True]
        otherusers = [usertuple[0] for usertuple in users if usertuple[1] is False]

        print("Logged users:")
        for usertuple in loggedusers:
            print(f"<{usertuple[0]}>")
        print("Users not logged in:")
        for usertuple in otherusers:
            print(f"<{usertuple[0]}>")

    @staticmethod
    def login_required(func):
        def wrapper_login_required(*args, **kwargs):
            if any([userlogged for userlogged in user.logged.values()]):
                value = func(*args, **kwargs)
                return value
            else:
                raise ValueError

        return wrapper_login_required

users = [('Ala', "1234"),
         ("Tom", "5678"),
         ("Olaf", "balwanek"),
         ]

for usercredentials in users:
    newuser = user(*usercredentials)

user.login("Ala", "1234")


# user.show_users()

def program():
    print("Uruchomiono program")
