arr = [1, 3, 4, 6, 7, 9, 11, 12]
# def bsearch1(arr, key):
#     low, high = 0, len(arr)
#     while high - low > 1:
#         mid = (low + high) // 2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             low = mid
#         else:
#             high = mid
#     return None

def bsearch1(arr, key):
    low, high = 0, len(arr)
    while high - low >= 1: # добавлено >= для учёта случаев когда в интервале low:high лежит в левой части один элемент
        mid = (low + high) // 2
        if len(arr[low:high]) == 1 and arr[0] != key: return None # когда всего один элемент
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid
        else:
            high = mid
            
    return None


# def bsearch2(arr, key, left=0, right=None):
    if right is None:
        right = len(arr)
    if right < left:
        return None
    middle = (left + right) >> 1
    if arr[middle] > key:
        return bsearch2(arr, key, left, middle)
    if arr[middle] < key:
        return bsearch2(arr, key, middle + 1, right)
    return middle


# def bsearch2(arr, key, left=0, right=None): # поменять на len(arr) - 1, допустимый инпут для проверки с одним элементом
#     if right is None: # не работает потому что right указывает на недопустимый индекс
#         right = len(arr) - 1 # для явного указания на элементы
#     if right < left:
#         return None
#     middle = (left + right) >> 1
#     if arr[middle] > key:
#         return bsearch2(arr, key, left, middle - 1) # middle - 1 для явного указания на элементы
        
#     if arr[middle] < key:
#         return bsearch2(arr, key, middle + 1, right)
#     return middle
def bsearch3(arr, key):
    n = len(arr)
    if n < 2:
        return (0 if (n == 1 and arr[0] == key) else None)
    m = int(0.5 * n)
    if arr[m] > key:
        return bsearch3(arr[:m], key)
    result = bsearch3(arr[m:], key)
    return result + (m if result != None else 0)

# def bsearch3(arr, key):
#     n = len(arr)
#     if n < 2:
#         return (0 if (n == 1 and arr[0] == key) else None)
#     m = int(0.5 * n)
#     if arr[m] > key:
#         return bsearch3(arr[:m], key)
#     result = bsearch3(arr[m:], key)
#     return (result + m if result != None else None) # исправить только тут: потому что при тесте на числа 
    # больше максимума в массиве он складывает None в result + какое то число целое m, а иначе возвращает 0
    # инпут на котором зафейлит это любое число больше максимума в массиве
# print(bsearch3(arr, 0))
def verify(arr):
    for i in arr:
        print(bsearch3(arr, i))
    print(bsearch3(arr, 0))
    print(bsearch3(arr, 13))
    print(bsearch3([1], 1))
    print(bsearch3([1], 0))
    print(bsearch3([1], 2))
    return
# verify(arr)
print(1675-229)


