def split_by_index(string_f, indexes_f):
    output = []
    my_index = 0

    for item in indexes_f:
        if item < len(string_f):
            output.append(string_f[my_index:item])
            my_index = item

    return output


indexes = [6, 8]
print(split_by_index("pythoniscool", indexes))
