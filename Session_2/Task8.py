def get_pairs(list_f):
    output = []

    for i in range(0, len(list_f) - 1):
        tuple_f = (list_f[i], list_f[i + 1])
        output.append(tuple_f)

    return output


my_list = (1, 2, 3, 4, 5)
print(get_pairs(my_list))
