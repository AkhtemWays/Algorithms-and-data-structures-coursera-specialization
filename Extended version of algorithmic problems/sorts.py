# def merge_sort(arr):
#     partition(arr, 0, len(arr) - 1)

# def partition(arr, left, right):
#     if left < right:
#         middle = (left + right) // 2               
#         partition(arr, left, middle)
#         partition(arr, middle+1, right)
#         merge(arr, left, middle, right)
# def merge(arr, left, middle, right):

#     left_part = arr[left:middle + 1]
#     right_part = arr[middle + 1:right + 1]
#     i, j = 0, 0
#     left_part.append(float('inf'))
#     right_part.append(float('inf'))
#     for k in range(left, right+1):
#         if left_part[i] <= right_part[j]:
#             arr[k] = left_part[i]
#             i += 1
#         else:
#             arr[k] = right_part[j]
#             j += 1
    
   
# arr = [i for i in range(2000000, 0, -1)]
# merge_sort(arr)
# print(arr)

# quick sort

def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi


        
def Quick_sort(arr):
    Quick_sort2(arr, 0, len(arr) - 1)
def Quick_sort2(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        Quick_sort2(arr, low, p - 1)
        Quick_sort2(arr, p + 1, high)

def partition(arr, low, high):
   
    pvt_idx = get_pivot(arr, low, high)
    pivot = arr[pvt_idx]
    arr[pvt_idx], arr[low] = arr[low], arr[pvt_idx]
    border = low
    
    shift_idx = border + 1
    while shift_idx <= high:
        if arr[shift_idx] < pivot:
            border += 1
            arr[shift_idx], arr[border] = arr[border], arr[shift_idx]
        shift_idx += 1
    arr[low], arr[border] = arr[border], arr[low]
    return border
    


    

arr = [i for i in range(20, 1, -1)]
Quick_sort(arr)
print(arr)



# Divide and conquer algorithms

def binary_search(a, x):
    left, right = 0, len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return a[mid]
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search([2, 3, 5, 7, 8, 10, 12], 5))