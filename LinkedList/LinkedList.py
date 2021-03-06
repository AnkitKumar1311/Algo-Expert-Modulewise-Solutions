
#   structure to create a node for the linked list

class Node : 
    data = None 
    next_node = None



class LinkedList : 

    #   cosntructor of the program
    def __init__(self) : 
        self.head = None


    #   method to append a new node at the end of the list
    def append(self, sk) : 
        ptr = Node()
        ptr.data = sk
        ptr.next_node = None

        if self.head is None : 
            self.head = ptr

        else : 
            qptr = self.head
            while qptr.next_node is not None : qptr = qptr.next_node
            qptr.next_node = ptr

    #   printing the class values
    def __str__(self) : 
        self.traverse()
        return ""

    #   iterative method to traverse the linked list
    def traverse(self) : 
        ptr = self.head
        if self.head is None : 
            print("List is empty")
        else : 
            ptr = self.head 
            while ptr is not None : 
                print(ptr.data, end = " : ")
                ptr = ptr.next_node

    
    #   recursive method to traverse the linked list
    def recursive_traversal(self, head) : 
        if head is None : 
            return print("list printed successfully. no data left to display.")

        print(head.data, end = " ")
        return self.recursive_traversal(head.next_node)

    #   method to return the main node
    def returnhead(self) : return self.head
    
    #   method to count the number of nodes in the linked list
    def return_number_of_nodes(self) -> int: 
        total_nodes = 0
        ptr = self.head

        while ptr is not None : 
            total_nodes += 1
            ptr = ptr.next_node

        return total_nodes


    #   method to get the sum of all the nodes in the linked list
    def sum(self, head) : 
        if head is None : return 0
        return head.data + self.sum(head.next_node)


    #   method to find the maximum element in the linked list
    def max(self) -> int : 
        if self.head is None : 
            return 0

        largest = self.head.data

        ptr = self.head.next_node

        while ptr is not None : 
            largest = max(largest, ptr.data)
            ptr = ptr.next_node

        return largest


    #   method to find the element in the linked list
    def search(self, sk) : 
        if self.head is None : 
            print("Linked list is empty")
            return

        ptr = self.head
        flag, element = False, -1
        while ptr.next_node is not None : 
            if ptr.data == sk : 
                flag = True
                element = ptr.data
                break

        if flag : 
            return element
        else : 
            print('Element was not found in the array')
            return

    
    #   method to check if the linked list is sorted or not
    def is_ascending(self) : 
        if self.head is None : 
            print("Linked list is empty")
            return False

        ptr = self.head 
        
        while ptr.next_node is not None : 
            if ptr.data > ptr.next_node.data : 
                return False

            ptr = ptr.next_node
        
        return True


    #   method to make the list cyclic
    def make_cyclic(self) : 
        ptr = self.head

        qptr = ptr.next_node.next_node

        qptr.next_node = ptr
        


    #   method to check if the linked list contains a loop
    def is_cyclic(self) : 
        ptr , qptr = self.head, self.head.next_node

        while ptr is not None and qptr is not None : 
            if ptr == qptr : 
                return True
            ptr = ptr.next_node
            qptr = qptr.next_node.next_node
        
        return False


    #   method to delete duplicates from the linked list
    def delete_duplicates(self) :
        has_seen = set()

        prev, ptr = None, self.head

        while ptr is not None : 
            if ptr.data in has_seen : 
                qptr = ptr
                ptr = ptr.next_node
                prev.next_node = ptr
                del qptr
            else : 
                has_seen.add(ptr.data)
                prev = ptr
                ptr = ptr.next_node
                

    #   method to find the middle element of the linked list
    def middle_element(self) : 
        if self.head is None : 
            print('List is empty')
            return


        ptr = self.head
        qptr = self.head

        while qptr is not None : 
            qptr = qptr.next_node
            if qptr : 
                qptr = qptr.next_node
                ptr = ptr.next_node

        return ptr.data              
                        

    #   method to find the middle element of the linked list using a stack
    def middle_element_stack(self) : 
        ptr = self.head
        result = list()
        while ptr is not None : 
            result.append(ptr.data)
            ptr = ptr.next_node

        return result[len(result)//2]


    #   method to find the intersection of the two linked list
    def intersection(self, head : Node) : 
        ptr = self.head
        qptr = head

        r1 = set();r2 = set()

        while ptr is not None :
            r1.add(ptr)
            ptr = ptr.next_node

        while qptr is not None : 
            if qptr in r1 : 
                return (True, qptr.data)
        
        return False


if __name__ == '__main__' : 

    linkedlist = LinkedList()
    newlist = LinkedList()

    linkedlist.append(1)
    linkedlist.append(1)
    linkedlist.append(4)
    linkedlist.append(3)
    linkedlist.append(5)
    linkedlist.append(5)
    linkedlist.append(1)
    linkedlist.append(7)
    linkedlist.append(8)
    
    linkedlist.delete_duplicates()

    print("intersection = ", linkedlist.intersection(newlist.returnhead()))

    print("Middle node = ", linkedlist.middle_element_stack())
    print("Middle node = ", linkedlist.middle_element())
    
    linkedlist.recursive_traversal(linkedlist.returnhead())
    
    print("total number of nodes = {}".format(linkedlist.return_number_of_nodes()))
    print("Sum of all the nodes = {}".format(linkedlist.sum(linkedlist.returnhead())))
    print("Largest element in the array = {}".format(linkedlist.max()))
    print(linkedlist.is_ascending())
    print(linkedlist)
    linkedlist.make_cyclic()
    print("Cyclic : ", linkedlist.is_cyclic())

    