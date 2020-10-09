import re


def is_palindrome(word):
    # forward = "".join(word[:].lower())
    forward = "".join(re.findall(r'[a-z]+', word.lower()))
    reverse = forward[::-1]

    print("Forward: {}\nReverse: {}".format(forward, reverse))

    return forward == reverse


# print(is_palindrome("Go hang a salami - I'm a lasagna hog"))


def my_is_palindrome(words):
    print("Input: {}".format(words))

    # remove all spaces/comma/punctuations
    forward = "".join(re.findall(r"\w", words.lower()))
    print("Forward: {}".format(forward))

    backward = forward[::-1]
    print("Forward: {}".format(backward))

    return forward==backward


print(my_is_palindrome("RACe Car"))
