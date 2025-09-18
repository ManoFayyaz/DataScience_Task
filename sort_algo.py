def BubbleSort(arr,n):
    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr

list=[45,67,33,23,89,56]
n=len(list)

res=BubbleSort(list,n)
print("Sorted list is:", res)


def SelectionSort(arr,n):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
                arr[i],arr[min]= arr[min],arr[i]
    return arr

list1 = [45,67,22,13,45,12]
n=len(list1)
res1 = SelectionSort(list1,n)
print("Sorted list is:", res1)