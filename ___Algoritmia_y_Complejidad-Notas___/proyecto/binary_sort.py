from math import floor

def binary_search(array, value, start, end): 
    # Base cases.
    if (start == end):
        if (array[start] > value):
            return (start)
        else:
            return (start + 1)
    if (start > end):
        return (start)
    middle = floor((start+end)/2)

    # Recursion conditions.
    if (array[middle] < value):
        return binary_search(array, value, middle+1, end)
    elif (array[middle] > value):
        return binary_search(array, value, start, middle-1)
    else:
        return (middle)
  
def insertion_sort(array): 
    for i in range(1, len(array)): 
        value = array[i]
        j = binary_search(array, value, 0, i-1)
        array = array[:j] + [value] + array[j:i] + array[i + 1:]
    return array 

array = [100, 5, 2, 32, 10005, 69, 88, 1]

print("Result:") 
print (insertion_sort(array))
