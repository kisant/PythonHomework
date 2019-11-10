def get_digits(num_f):
    output = []
    tuple_f = ()

    while num_f > 0:
        output.append(num_f % 10)
        num_f //= 10

    output.reverse()
    return tuple(output)


print(get_digits(1234567890))
