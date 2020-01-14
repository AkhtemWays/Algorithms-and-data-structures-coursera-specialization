# python3

def third_scan(str1, str2, count):
    count = max(0, count)
    for i,digit1 in enumerate(str1):
        if digit1 in str2:
            for j, digit2 in enumerate(str2):
                if digit1 == digit2:
                    count += 1
                    if len(str1[i+1:]) != 0 and len(str2[j+1:]) != 0:
                        third_scan(str1[i + 1:], str2[j + 1:], count)
                    else:
                        return count

        else:
            return count


def maximum_length(int1, int2):
    count_array = []
    str1 = str(int1)
    index = 0
    while index != len(str1):
        str2 = str(int2)
        count = 0
        count_array.append(third_scan(str1[index:], str2, count))
    return max(count_array)

print(maximum_length(72931594, 2813970))