def merge_sort(arr):
    partition(arr, 0, len(arr) - 1)

def partition(arr, left, right):
    if left < right:
        middle = (left + right) // 2               
        partition(arr, left, middle)
        partition(arr, middle+1, right)
        merge(arr, left, middle, right)
def merge(arr, left, middle, right):

    left_part = arr[left:middle + 1]
    right_part = arr[middle + 1:right + 1]
    i, j = 0, 0
    left_part.append(float('inf'))
    right_part.append(float('inf'))
    for k in range(left, right+1):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
    
   
arr = [i for i in range(2000000, 0, -1)]
merge_sort(arr)
print(arr)