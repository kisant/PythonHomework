f_content = ""

with open("data/unsorted_names.txt", "r") as f:
    f_content = sorted(f.read().split())

with open("data/sorted_names.txt", "w") as f:
    f.write("\n".join(f_content))
