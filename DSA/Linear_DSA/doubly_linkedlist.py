class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        
def traverse(head,lastNode):
    currentNode=head
    while currentNode:
        print(currentNode.value)
        currentNode=currentNode.next
    print()    
    
    currentNode=lastNode
    while currentNode:
            print(currentNode.value)
            currentNode=currentNode.prev
    print()   
        
def insertNode(head,newNode,position):
    if position==1:
        newNode.next=head
        return head
        
    currentNode=head
    for _ in range(position-2):
        if currentNode.next is None:
            break
        currentNode=currentNode.next
    
    newNode.next = currentNode.next
    newNode.prev = currentNode
    
    if currentNode.next:
        currentNode.next.prev = newNode
    
    currentNode.next = newNode
    return head
    
def deleteNode(head,nodetoDelete):
    if head==nodetoDelete:
        return head.next
    
    currentNode=head
    while currentNode.next and currentNode.next!=nodetoDelete:
        currentNode=currentNode.next
   # node not found
    if currentNode.next is None:
        return head
    
    nodeToDelete = currentNode.next

    currentNode.next = nodeToDelete.next
    
    if nodeToDelete.next:
        nodeToDelete.next.prev = currentNode
    
    return head
        
        
node1=Node(7)
node2=Node(9)
node3=Node(4)
node4=Node(5)

node1.next=node2

node2.next=node3
node2.prev=node1

node3.next=node4
node3.prev=node2

node4.prev=node3

traverse(node1,node4)

print("After Insertion")
newNode=Node(2)
insertNode(node1,newNode,2)
traverse(node1,node4)

print("After Deletion")
deleteNode(node1,node3)
traverse(node1,node4)



