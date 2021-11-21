class NotLoggedIn(Exception):
    pass


class user:
    def __init__(self, username, password, _id):
        self.id = _id
        self.username = username
        self.password = password
        self.logged = False

    def __str__(self):
        return f"User: {self.username} - logged in: {[self.logged]}"


class login:
    user_id = 1

    def __init__(self):
        self.users = {}

    def add_user(self, username, password):

        if username in [_user.username for _user in self.users.values()]:
            raise KeyError("Username is already taken")

        new_user = user(username, password, login.user_id)
        self.users[new_user.id] = new_user
        login.user_id += 1

    def get_user(self, username, out=False):
        _obj = [_user for _user in self.users.values() if _user.username == username]
        if _obj:
            return _obj[0]
        else:
            return out

    def check_credentials(self, username, password):
        if self.get_user(username).password == password:
            return True
        else:
            return False

    def login(self, username, password):
        self.logout()

        if self.check_credentials(username, password):
            self.get_user(username).logged = True
            print(f"User <{username}> logged succesfully.")
        else:
            print(f"Failed to login User <{username}>.")

    def logout(self, *args):
        if args:
            self.get_user(args[0]).logged = False
        else:
            for _user in self.users.values():
                _user.logged = False

    def show_users(self):

        loggedusers = [_user for _user in self.users.values() if _user.logged is True]
        otherusers = [_user for _user in self.users.values() if _user.logged is False]

        print("Users logged in:")
        for _user in loggedusers:
            print(f"<{_user.username}>")
        print("Users not logged in:")
        for _user in otherusers:
            print(f"<{_user.username}>")

    def login_required(self, username):
        def decorator_login_required(_func):
            def wrapper_login_required(*args, **kwargs):
                if self.get_user(username).logged is True:
                    output = _func(*args, **kwargs)
                    return output
                else:
                    raise NotLoggedIn("Required user is not logged in")

            return wrapper_login_required

        return decorator_login_required


users = [('Ala', "1234"),
         ("Tom", "5678"),
         ("Olaf", "balwanek"),
         ]

log = login()
for elem in users:
    log.add_user(*elem)

if input("Czy chcesz się zalogować? (y/n?)\n>") in {"Y", "y", "Yes", "yes"}:
    data = input("Podaj nazwę użytkownika:\n>"), input("Podaj hasło:\n>")
    log.login(*data)
else:
    print("Zalogowano anonimowo")

# log.show_users()


@log.login_required("Ala")
def func():
    print("Function executed succesfully")
