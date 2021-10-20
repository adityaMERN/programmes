class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
#Class Node is denoted as a single element of a linkedlist with data and next values.
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
# to print the linkedlist we first check if the head is empty or not, if it is so then we dont have to print anything
#as the linkedlist is empty. Other wise we will iterate through every node nad print the data.
    def print(self):
        if self.head is None:
            print("Empty linked list")
            return 
        iterator=self.head
        s=""
        while iterator:
            s+=str(iterator.data)+"->"
            iterator=iterator.next
        print(s)
#to insert at the end what we do is basically we first check if the head is NOne or not i.e, if there is any ll 
# before or not,do we have any single node intially or not, so if the head value is none, then we simply have to create
# a new node with data as its value and none as the address and return that node
#otherwise, we store the head value of that node in a varable and iterate till we reach upto that node which
#is the last node of that linkedlist by checking if the next value is null or not, when we find that we simply 
# point the next of that iterator node to the value of this new node's data and address as None.          
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            
            itr=itr.next
        itr.next=Node(data,None)
#we need to insert a set of values, so we simply iterate through each element of the lust and call the 
# insert_in_end function for each data.    
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
# to count the total number of elements in th linkedlist
    def get_lenght(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
#to remove any element at an index if we have to remove at 0 then we simply have to discard the first node
#we put the head value to data of next node.
#otherwise we iterate to the node just before that index and put the next to the next of next of that index node.
    def remove_at(self,index):
        if index<0 or index>ll.get_lenght():
            print("Wrong index")
            return
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index>ll.get_lenght():
            print("Wrong index")
            return
        if index==0:
            self.insert_at_beginning(data)
            return
        if index==ll.get_lenght():
            self.insert_at_end(data)
            return
        count=0
        itr=self.head
        while itr:
            count+=1
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
               
if __name__=='__main__':
    ll=LinkedList()
    # ll.insert_at_beginning(1)
    # ll.insert_at_beginning(2)
    # ll.insert_at_beginning(3)
    # ll.insert_at_end(4)
    # ll.insert_at_end(5)
    ll.insert_values([1,2,3,4,5,6,7,8,9])
    
    #ll.remove_at(3)
    #ll.print()
    ll.insert_at(6,10)
    ll.print()
    
    #x=ll.get_lenght() 
    #print(x)  