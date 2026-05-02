#Singly Linked List
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def traverse(head):
    currentNode=head
    while currentNode:
        print(currentNode.value)
        currentNode=currentNode.next
    print()       


def min_traverse(head):
    min_val=head.value
    currentNode=head.next
    while currentNode:
        if currentNode.value<min_val:
            min_val=currentNode.value    
        currentNode=currentNode.next
    return min_val    

def DeleteNode(head,node):
    if head==node:
        return head.next
    
    currentNode=head
    while currentNode.next and currentNode.next!=node:
        currentNode=currentNode.next 

    if currentNode.next is None:
        return head

    currentNode.next=currentNode.next.next

    return head

def insertNode(head,newNode,position):
    if position==1:
        newNode.next=head
        return newNode
    
    currentNode=head
    for _ in range(position-2):
        if currentNode.next is None:
            break
        currentNode=currentNode.next

    newNode.next=currentNode.next
    currentNode.next=newNode
    return head

node1=Node(4)
node2=Node(6)
node3=Node(7)        
node4=Node(8)

node1.next=node2
node2.next=node3
node3.next=node4

traverse(node1)
print(min_traverse(node1))
print("----------")
DeleteNode(node1,node3)
traverse(node1)

newNode=Node(67)
insertNode(node1,newNode,3)
traverse(node1)