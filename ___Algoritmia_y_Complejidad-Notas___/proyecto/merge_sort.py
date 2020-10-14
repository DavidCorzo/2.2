def mergeSort(arr):
    size = len(arr)
    if (size > 1):
        middle = (size // 2)
        l_arr = arr[:middle] # The left array pushed to the call-stack.
        r_arr = arr[middle:] # The right array pushed to the call-stack.
        # Recursive calls.
        mergeSort(l_arr)
        mergeSort(r_arr)

        prev,curr,nextt = 0,0,0
        
        l_size = len(l_arr)
        r_size = len(r_arr)
        while ( (prev < l_size) and (curr < r_size) ):
            if (l_arr[prev] < r_arr[curr]):
              arr[nextt] = l_arr[prev]
              prev += 1
            else:
                arr[nextt] = r_arr[curr]
                curr += 1
             
            nextt += 1
            
        while prev < l_size:
            arr[nextt] = l_arr[prev]
            prev += 1
            nextt += 1
 
        while curr < r_size:
            arr[nextt] = r_arr[curr]
            curr += 1
            nextt += 1

array = [100, 5, 2, 32, 10005, 69, 88, 1]

mergeSort(array)
print("\nResult:")
print(array)
