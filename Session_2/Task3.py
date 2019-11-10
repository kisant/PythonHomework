def make_split(string_f):
    output = []
    help_string = ""

    for item in string_f:
        if item != " ":
            help_string += item
        else:
            output.append(help_string)
            help_string = ""

    if help_string:
        output.append(help_string)

    return output


print(make_split("qwe qwe qwe"))
