class Linkedlist:
        def __init__(self,data):
            self.data=data
            self.next=None

        def Traverse(self,head):
            self.current_node=head
            while self.current_node:
                print(self.current_node.data,end=" -> ")
                self.current_node=self.current_node.next
            print("\n")
 

        def Min(self,head):
            if head == None:
                print("Linked list is empty")
                return None

            curent_head = head
            min=curent_head.data
            current_head = head.next

            while current_head:
                if current_head.data  < min:
                     min=current_head.data
                current_head=current_head.next 

            print("\n","Minimum value in the linked list is:", min)

        def Max(self,head):
            if head == None:
                print("Linked list is empty")
                return None

            curent_head = head
            max=curent_head.data
            current_head = head.next

            while current_head:
                if current_head.data > max:
                     max=current_head.data
                current_head=current_head.next 

            print("\n","Maximum value in the linked list is:", max)   


        def Delete_Node(self,head,nodetodelete):
            if head==nodetodelete:
                head=head.next
                return head 
            
            current_node=head
            while current_node.next and current_node.next!=nodetodelete:
                current_node=current_node.next

            if current_node.next is None:
                return head

            # If we reach here, then current_node.next is the node to be deleted
            current_node.next=current_node.next.next
            return head

        @staticmethod
        def Insert_Node(head,new_node,position):
            if position == 1:
                new_node.next = head
                return new_node

            current_node=head

            for _ in range(position - 2):
                if current_node is None:
                    break
                current_node = current_node.next

            if current_node is None:
                print("Position out of range")
                return head

            # Inserting the node
            new_node.next = current_node.next
            current_node.next = new_node
            return head


node1=Linkedlist(10) 
node2=Linkedlist(20)   
node3=Linkedlist(30)
node4=Linkedlist(40)
node5=Linkedlist(5)

node1.next=node2
node2.next=node3
node3.next=node4     
node4.next=node5
node5.next=None

node1.Traverse(node1)
node1.Min(node1)
node1.Max(node1)
node1.Delete_Node(node1,node3)
node1.Traverse(node1)

new_node=Linkedlist(35)
node1.Insert_Node(node1,new_node,3)
node1.Traverse(node1)