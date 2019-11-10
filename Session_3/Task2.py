def generate_squares(num):
    dict_f = {}

    for i in range(1, num + 1):
        dict_f[i] = i*i

    return dict_f


print(generate_squares(5))
