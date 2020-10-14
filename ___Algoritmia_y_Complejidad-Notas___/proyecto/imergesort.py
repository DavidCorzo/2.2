import pdb

def mergeSort(array):
    curr_s = 1 # Current size.
    while (curr_s < len(array) - 1):
        left = 0
        while ( left < (len(array) - 1) ):
            middle = min((left + curr_s - 1),(len(array)-1))
            if (2 * curr_s  + left - 1 > len(array)-1): right = len(array) - 1
            else: right = 2 * curr_s + left - 1
            merge(array, left, middle, right)
            left = left + curr_s * 2
        curr_s = 2 * curr_s  

def merge(array, left:int, middle:int, right:int):
    n_1 = middle - left + 1
    n_2 = right - middle
    L = [0] * n_1
    R = [0] * n_2
    print("inside for loop n_1")
    for i in range(0, n_1):
        pdb.set_trace()
        L[i] = array[left + i]
    print("out.")
    print("inside for loop n_2")
    for i in range(0, n_2):
        pdb.set_trace()
        R[i] = array[middle + i + 1]
    print("out.")
    i = j = 0
    k = left
    print("inside while i < n_1 and j < n_2")
    while ( (i < n_1) and (j < n_2) ):
        if ( L[i] > R[j] ):
            array[k] = R[j]
            j += 1
        else:
            array[k] = L[i]
            i += 1
        k += 1
        pdb.set_trace()
    print("Out")
    # First array.
    while ( i < n_1 ):
        array[k] = L[i]
        i += 1
        k += 1
    # Second array.
    while ( j < n_2 ):
        array[k] = R[j]
        j += 1
        k += 1
  

array = [12, 11, 13, 5, 6, 7]
mergeSort(array)
print(f"Result: \n{array}")
