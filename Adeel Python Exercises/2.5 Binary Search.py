def binary_search(array, v):
    sort_array = sorted(array)
    start, end = 0, len(array)+1
    
    while start <= end:
        mid = (start+end) // 2
        if sort_array[mid] == v:
            return mid
        elif sort_array[mid] < v:
            start = mid + 1
        elif sort_array[mid] > v:
            end = mid -1
        
    return -1


list = ['c','a','v','z','t']
value = 'a'
result = binary_search(list, value)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Can't find the target!")