# Linear Search Algorithm Implementation
def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr=[3,4,6,7,9]
x=7
result=LinearSearch(arr,x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")

# Binary Search Algorithm Implementation
def BinarySearch(arr, target):
    left=0
    right=len(arr)-1

    while left <= right:
        mid= (left+right)//2   #integer division

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left=mid+1
           
        else:
            right=mid-1
    return -1  # Element not found

   

arr=[1,2,3,4,5,6,7,8,9]
x=8
result=BinarySearch(arr,x)
if result != -1:
    print(f"Element found at index {result+1}")
else:
    print("Element not found in the array")

