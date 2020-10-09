def sort_words(input_string):
    words = input_string.split()  # returns a list of all the words in the string
    print("Before sort (split): {}".format(words))
    words = [(w.lower() + w) for w in words]

    print("Before sort(lower) {}".format(words))

    words.sort()
    words = [w[len(w) // 2:] for w in words]
    print("After sort & lower {}".format(words))

    return " ".join(words)  # returns a string in which the elements of sequence have been joined by str separator.


# print(sort_words("banana ORANGE apple Orange orange"))


def sort_string(string):
    return ' '.join(sorted(string.split(), key=lambda x: x.lower()))


# print(sort_string("banana ORANGE apple Orange orange"))


def my_sort_words(input_word):
    print("Input: {}".format(input_word))
    split_word = input_word.split()
    word_list = []
    for word in split_word:
        word_list.append(word.lower() + word)

    word_list.sort()

    new_list = []

    for word in word_list:
        new_list.append(word[(len(word)//2):])

    new_list = ", ".join(map(str, new_list))

    return "Output: {}".format(new_list)


print(my_sort_words("MANGO apple Banana ORANGE pawpaw"))