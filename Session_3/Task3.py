def count_letters(string):
    output = {}

    for char in string:
        output[char] = string.count(char)

    return output


print(count_letters("simplestring"))
