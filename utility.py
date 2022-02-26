from time import time


def add(num1, num2):
    return num1 + num2


def minus(num1, num2):
    try:
        return num1 - num2
    except TypeError as err:
        return err


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took about {t2 - t1}")
        return result

    return wrapper
