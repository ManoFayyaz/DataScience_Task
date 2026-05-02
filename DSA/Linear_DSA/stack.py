class Stack:
    def __init__(self):
      self.stack=[]
    
    def push(self,element):
        self.stack.append(element)
    
    def pop_element(self):
        self.stack.pop()
    
    def peek(self):
         return self.stack[-1]
    
stack=Stack()        
stack.push(2)
stack.push(3)
stack.push(6)
stack.push(8)
print(stack.stack)
stack.pop_element()
print(stack.stack)
print(stack.peek())

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.size=0
        
    def push(self,value):
        new_Node=Node(value)
        if self.head:
            new_Node.next=self.head
        self.head=new_Node
        self.size+=1

    def pop(self):
        if not(self.isEmpty()):
            pop_node=self.head
            self.head=self.head.next
            self.size-=1

    def isEmpty(self):
        return self.size==0
    
    def traverse(self):
        if not(self.isEmpty()):
            currentNode=self.head
            while currentNode:
                print(currentNode.value,end="->")
                currentNode=currentNode.next
            print()

    def isPeek(self):
        if not(self.isEmpty()):
            return self.head.value
        
    
    
mystack=Stack()
mystack.push(4)
mystack.push(6)
mystack.push(8)
mystack.traverse()
mystack.pop()
mystack.traverse()
print(mystack.isPeek())














