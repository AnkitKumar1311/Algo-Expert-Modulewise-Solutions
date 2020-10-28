"""
PROGRAM TO CREATE A LINKED LIST IN PYTHON
"""

#   class used to create a single node or point to node
class Node : 
    data = None
    next_node = None


#   class to create a linked list
class LinkedList : 

    def __init__(self) : 
        self.head = None


    #   function to insert a node at the end of the linked list    
    def insertData(self, num) : 
        ptr = Node()
        ptr.data = num
        ptr.next_node = None
        
        if self.head == None : 
            self.head = ptr
        else : 
            qptr = self.head
            while qptr.next_node != None : 
                qptr = qptr.next_node

            qptr.next_node = ptr

    

    #   function to traverse the entire linked list (iterative method)
    def traverse(self) :
        if self.head == None : 
            print("No data in the list")
        else : 
            ptr = self.head
            while ptr != None : 
                print(ptr.data, end = " -> ") 
                ptr = ptr.next_node



    #   function to get the head pointer
    def gethead(self) :
        return self.head


    #   function to traverse a linked list recursively
    def recursiveTraverse(self, main_node) : 
        if main_node == None : 
            print("list ended")
            return

        print(main_node.data)
        self.recursiveTraverse(main_node.next_node)


if __name__ == '__main__' : 
    mylist = LinkedList()
    mylist.insertData(5)
    mylist.insertData(4)
    mylist.insertData(3)
    mylist.insertData(2)
    mylist.insertData(1)  

    mylist.recursiveTraverse(mylist.gethead())
