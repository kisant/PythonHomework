def is_polindrome(string_f):
    test_string = string_f[::-1]
    if test_string == string_f:
        return True
    else:
        return False


print(is_polindrome("qweewq"))
