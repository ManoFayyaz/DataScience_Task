class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def preorder_traversal(node):
    if node is None:
        return
    print(node.data,end=",")
    preorder_traversal(node.left)
    preorder_traversal(node.right)    

def inorder_traversal(node):
    if node is None:
        return
    preorder_traversal(node.left)
    print(node.data,end=",")
    preorder_traversal(node.right)    

def postorder_traversal(node):
    if node is None:
        return
    preorder_traversal(node.left)
    preorder_traversal(node.right)    
    print(node.data,end=",")


root=BinaryTree('R')  
nodeA=BinaryTree('A')
nodeB=BinaryTree('B')
nodeC=BinaryTree('C')
nodeD=BinaryTree('D')
nodeE=BinaryTree('E')
nodeF=BinaryTree('F')
nodeG=BinaryTree('G')

root.left=nodeA
root.right=nodeB
nodeA.left=nodeC
nodeA.right=nodeD
nodeB.left=nodeE
nodeB.right=nodeF
nodeE.left=nodeG

print("PreOrder")
preorder_traversal(root)
print("\nInOrder")
inorder_traversal(root)
print("\nPostOrder")
postorder_traversal(root)
