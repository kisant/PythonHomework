def combine_dicts(*dicts):
    output = {}

    for dict_f in dicts:
        for key, value in dict_f.items():
            if key not in output:
                output[key] = value
            else:
                output[key] += value

    return output


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2, dict_3))
