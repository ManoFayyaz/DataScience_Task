class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]            
    def traverse(self):
        print(self.queue)    
     


q=Queue()
q.enqueue(8)
q.enqueue(4)
q.enqueue(3)
q.enqueue(6)
q.enqueue(7)
q.traverse()
print(q.dequeue())
q.traverse()
print(q.peek())
print("--------------------------------------")

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def enqueue(self,value):
        newNode=Node(value)
        if self.front is None:
            self.front=self.rear=newNode
            self.size+=1 

        self.rear.next=newNode
        self.rear=newNode 
        self.size+=1

    def deqeue(self):
        if self.front is None:
            self.rear=None
            return "Empty Queue"
        
        self.front=self.front.next
        self.size-=1
    
    def peek(self):
        if self.front is None:
            return "Empty"
        print(self.front.value)    
                    
    def traverse(self):
        currentNode=self.front
        while currentNode:
            print(currentNode.value)
            currentNode=currentNode.next                

q=Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(8)
q.traverse()
print("After dequeue")
q.deqeue()
q.traverse()