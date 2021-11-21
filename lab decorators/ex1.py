def hello(func):
    def hello_wrapper(*args, **kwargs):
        print("Hello!")
        return func(*args, **kwargs)

    return hello_wrapper


@hello
def ala(n):
    return n ** 2


print(ala(3))
