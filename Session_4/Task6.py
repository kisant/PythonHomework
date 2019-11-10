def call_once(f):
    call_check = False

    def wrapper(*args):
        nonlocal call_check
        if not call_check:
            call_check = True
            return f(*args)
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
