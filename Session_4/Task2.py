import re


def most_common_words(filepath, number_of_words=3):
    with open(filepath, 'r') as f:
        f_content = re.findall(r'\w+', f.read().lower())

    f_dict = {}
    for item in f_content:
        f_dict[item] = (f_content.count(item))

    sorted_list = sorted(f_dict, key=f_dict.get, reverse=True)
    output = []

    for item in sorted_list[0:number_of_words]:
        output.append(item)

    return output


print(most_common_words('data/lorem_ipsum.txt'))
