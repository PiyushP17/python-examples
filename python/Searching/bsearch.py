def binarySearch (arr, l, r, x): 
    if l<=r: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x)
    return -1

arr = list(map(int,input("Enter elements in increasing order: ").split()))
x = int(input("Enter element to search : "))
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print("Element present at index ",result)
else: 
    print("Element not found")
