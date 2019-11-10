import string

alphabet = string.ascii_lowercase


def character_in_all_strings(list_of_strings_f):
    chosen_item = set(list_of_strings_f[0])
    for item in list_of_strings_f[1:]:
        chosen_item &= set(item)

    return chosen_item


def character_in_alphabet_order(list_of_string_f):
    output = set()

    for item in list_of_string_f:
        output |= set(item)

    return output


def character_in_two_or_more(list_of_strings_f):
    output = set()
    chosen_item = set(list_of_strings_f[0])

    for item in list_of_strings_f[1:]:
        chosen_item &= set(item)
        output |= chosen_item
        chosen_item = set(list_of_strings_f[0])

    return output


def character_not_in_list(list_of_strings_f):
    output = set(alphabet) - set(list_of_strings_f)

    return output


list_of_strings = ["hello", "world", "python"]

print(character_in_all_strings(list_of_strings))
print(character_in_alphabet_order(list_of_strings))
print(character_in_two_or_more(list_of_strings))
print(character_not_in_list(list_of_strings))
