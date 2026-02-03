my_str = "TAAAAAAGGAABBBCCCCDABB"
print(my_str)


def compress_string(s):
    compressed = []
    new_item = ""
    count = 1
    chars_list = list(s)

    for index in range(0, len(chars_list) - 1):

        if chars_list[index] == chars_list[index + 1]:
            new_item = chars_list[index]
            count += 1
            if index == len(chars_list) - 2:
                compressed.append((new_item, count))
            continue
        else:
            if count > 1:
                compressed.append((new_item, count))
            else:
                compressed.append((chars_list[index], count))

        count = 1
    return compressed


print(compress_string(my_str))
