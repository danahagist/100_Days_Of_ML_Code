# Task:
# Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) 
#  and inserts it at the tail of the linked list referenced by the head parameter. 
#   Once the new node is added, return the reference to the head node.

# ---------------------------- HackerRank creates Node and Solution classes ----------------------------------------

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
            
 # ------------------------------------------ Solution -------------------------------------------------------------
 
     def insert(self,head,data): 
    #Complete this method
        node = Node(data)
        # Creating first node
        if head == None:
            head = node
        # Creating subsequent nodes
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = node
        return head
            
# -------------------------------------- End Solution -------------------------------------------------------------

# ----------------------------------- HackerRank Input Code -------------------------------------------------------

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	
 
# ----------------------------------------- End File --------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
