def remember_result(f):
    last_res = None

    def wrapper(*args):
        nonlocal last_res
        print(f"Last result = '{last_res}'")
        last_res = f(*args)
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


print(sum_list(1, 2))
print(sum_list("c", "d"))
