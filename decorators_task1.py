def log_before_after(func):

    def wrapper():
        print('Before the function:', func.__name__)
        func()
        print('After the function:', func.__name__)
    return wrapper


@log_before_after
def print_hello():
    print('Hello, world!.')

print_hello()
