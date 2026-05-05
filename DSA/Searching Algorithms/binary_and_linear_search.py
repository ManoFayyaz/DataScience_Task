class Linear_Search:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target

    def linearSearch(self):
        for i in range(len(self.arr)):
            if self.arr[i]==self.target:
                return f"Found {self.target} at index {i}"
                
        return "Target variable is not in this list"    

x=[1,5,4,3,7,8,9,4]
v=4
l1=Linear_Search(x,v)
print(l1.linearSearch())


class Binary_Search:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def binarySearch(self):
        self.arr.sort()
        left=0
        right=len(self.arr)-1

        while left<=right:
            mid=(left+right)//2

            if self.target==self.arr[mid]:
                return f"Found at index {mid}"
            
            if self.target>self.arr[mid]:
                left=mid+1
            else:
                right=mid-1    
        return "Target was not found!"

x=[4,5,7,2,3,1,9]
target=9

b1=Binary_Search(x,target)
print(b1.binarySearch())