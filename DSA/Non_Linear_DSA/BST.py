class Binary_Search_Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def preorder_traversel(node):
    if node is None:
        return 
    print(node.data,end=">")
    preorder_traversel(node.left)
    preorder_traversel(node.right)

def insert(root,value):
    if root is None:
       return Binary_Search_Tree(value)
    if value < root.data:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)        

    return root

def find_min(node):
    while node.left:
        node=node.left
    return node    

def delete_node(root,value):
    if root is None:
        return root
    
    if value<root.data:
        root.left=delete_node(root.left,value)
    elif value>root.data:
        root.right=delete_node(root.right,value)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp=find_min(root.right)
        root.data=temp.data
        root.right=delete_node(root.right, temp.data)

    return root


root=None
root=insert(root,14)
root=insert(root,6)
root=insert(root,7)
root=insert(root,15)
root=insert(root,24)

preorder_traversel(root)        

print("\n")
delete_node(root,6)
preorder_traversel(root)        