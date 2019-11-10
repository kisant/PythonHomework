def replace(string_f):
    translate = {
        "\'": "\"",
        "\"": "\'"
    }
    output = ""
    for item in string_f:
        output += translate.get(item, item)
    return output


string = "hello it\'s me \" \" \'"
print(replace(string))
