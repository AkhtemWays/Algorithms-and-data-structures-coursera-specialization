# python3

from random import randint


from random import randint

def partition3(array, left, right):
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    pivot = array[left]
    j = left
    for i in range(left+1, right+1):
        if array[i] <= pivot:
            j = j + 1
            array[j], array[i] = array[i], array[j]
    array[left], array[j] = array[j], array[left]
    return j


def randomized_quick_sort(array, left, right):
    if left >= right:
        return array
    else:
        mid = partition3(array, left, right)
        randomized_quick_sort(array, left, mid-1)
        randomized_quick_sort(array, mid+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(" ".join(map(str, elements)))
