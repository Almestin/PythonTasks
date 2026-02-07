data = [(3, 2), (3, 4), (2, 1), (7, 8), (4, 3), (3, 5), (5, 6), (9, 9), (8, 7), (9, 9), (1, 2), (0, 5)]
print(data)


def mirror_pairs(pairs):
    index_list = []
    for index in range(len(pairs) - 2):
        if pairs[index][0] > pairs[index][1]:
            pairs[index] = (pairs[index][1], pairs[index][0])

    for index in range(0, len(pairs) - 2):
        for t in range(len(pairs) - index - 1, 1, -1):
            if pairs[index] == pairs[index + t]:
                index_list.append(index)

    for index in range(len(index_list) - 1, -1, -1):
        pairs.pop(index_list[index])

    return pairs


print(mirror_pairs(data))

