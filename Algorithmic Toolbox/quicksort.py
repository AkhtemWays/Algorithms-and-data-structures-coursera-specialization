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