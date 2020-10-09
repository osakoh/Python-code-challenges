def my_find_index(the_list, find):
    first_list = []
    second_list = []

    for idx, value in enumerate(the_list):
        if value == find:
            first_list.append(idx)
        elif isinstance(value, list):
            for inx in my_find_index(value, find):
                second_list.append(inx)
    tl = first_list + second_list
    return tl


index = [[2, 8, 6, 2], [6, 9, 0], [7, 6], [2, 0, 6, 2]] #, [6, 9, 0], [7, 6], [2, 0, 6]]
print(my_find_index(index, 2))

print("\n")

index1 = [[2, 5, 2, 4, 2, 9], [2, 3], [0, 5, 2]]
for i, v in enumerate(index1):
    if v == 2:
        pass
    elif isinstance(v, list):
        for ind, val in enumerate(v):
            if val == 2:
                print(i + ind)
        print("true")