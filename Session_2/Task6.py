def get_longest_word(string_f):
    list_f = string_f.split()

    max_num = 0
    max_item = ""
    for item in list_f:
        if len(item) > max_num:
            max_num = len(item)
            max_item = item

    #return max(list_f)
    return max_item


print(get_longest_word("a     ,afksfl][+*-kldk      ab abb abbb a bbb"))