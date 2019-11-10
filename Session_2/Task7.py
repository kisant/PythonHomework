def foo(list_f):
    output = []
    item = 1

    for i in range(len(list_f)):
        for j in range(len(list_f)):
            if j != i:
                item *= list_f[j]

        output.append(item)
        item = 1

    return output


my_list = [1, 2, 3, 4, 5]
print(foo(my_list))
