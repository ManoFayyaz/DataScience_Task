class BubbleSort:
    def __init__(self,arr):
        self.arr=arr
    def bubbleSort(self):
        n=len(self.arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]

        print("Sorted Array: ",self.arr)

arr=[67,43,23,78,90]
b1=BubbleSort(arr)                    
b1.bubbleSort()


class SelectionSort:
    def __init__(self,arr):
        self.arr=arr
    def selectionSort(self):
        n=len(arr)
        for i in range(n-1):
            min_index=i
            # print("min index before",min_index)
            # print("j--------")

            for j in range(i+1,n):
                # print(j)
                if self.arr[j]<self.arr[min_index]:
                    min_index=j
            # print("Min index this time: ",min_index)        
            self.arr[i],self.arr[min_index]=self.arr[min_index],self.arr[i]
        print("Sorted Array", self.arr)

arr=[4,6,7,3,2,9]
s1=SelectionSort(arr)
s1.selectionSort()

class InsertionSort:
    def __init__(self,arr):
        self.arr=arr
    def insertionSort(self):
        n=len(self.arr)
        for i in range(1,n):
            insert_index=i
            current_value=self.arr[i]
            for j in range(i-1,-1,-1):
                if self.arr[j]>current_value:
                    self.arr[j+1]=self.arr[j]
                    insert_index=j
                else:
                    break
            self.arr[insert_index]=current_value    
        print("Sorted array:",self.arr)                        

arr=[9,6,7,4,3]
i1=InsertionSort(arr)
i1.insertionSort()