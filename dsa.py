list1=[3,5,6,8,3,2,0]

min=list1[0]

for i in list1:
    if i < min:
        min=i

print("Minimum value in the list is:", min)        

list2=[4,66,78,22,45,31]

max=list2[0]

for i in list2:
    if i > max:
        max=i

print("Maximum value in the list is:", max)       

#Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            self.stack.pop()
            print(self.stack)

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print(self.stack[-1])

    def length(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print(len(self.stack))


stack1 = Stack()


stack1.push(10)
stack1.push(20) 
stack1.push(30)
stack1.peek()
stack1.length()
stack1.pop()
stack1.peek()
stack1.length()


stack=[34,55,6]
print(stack[-1])
print(stack[-2])


class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.append(element)
        print(self.queue)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            self.queue.pop(0)
            print(self.queue)

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.queue[0])

    def length(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(len(self.queue))  

print("Queue Implementation")

queue1=Queue()

queue1.enqueue(10)
queue1.enqueue(20)  
queue1.enqueue(30)
queue1.peek()
queue1.length()
queue1.dequeue()
queue1.peek()
queue1.length()      
            
