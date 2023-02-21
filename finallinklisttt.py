# print("here")
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.head = None

    def insertFirst(self, value):
        # print(value)
        newNode = node(value)  # Create a node
        # jo apna self.start uske phele tempNode aayega, toh tempNode ka next pe self.start, humne aisa code ko bataya

        #  Newvalue  = first value  -> we are telling python to add a value to linked list before start
        # the address of current first node should replace with new one
        newNode.next = self.start # automatically address has 
        self.start = newNode

  # 5|100 --> 10|1200 --> 20|1250  30|1400 --> 40|None
#                               |   |
                          #    25|1300
    def insertMiddle(self, value, pos):
        newNode = node(value)
        # We need to travel from 0 to position-1
        temp = self.start # We should not change the head, so we are taking some temporary variable
        # We should not change the head position, so we need to place the head as it is and we will go with temporary variable and this temporary variable will be keep on moving from 0 to position - 1
        for i in range(pos-1):
            temp = temp.next
            # after first iteration it will move to second place

        newNode.data = value  # 25
        # below both should not be interchange
        newNode.next = temp.next # 1250 will get copy to 1300 place
        temp.next = newNode # this will change to new node address

    def viewList(self):
        if self.start == None:
            print("List is empty")
        else:
            temp=self.start
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next
    
    def deleteFirst(self):
        if self.start==None:
            print("Linked List is empty")
        else:
            print("delete first start: "+str(self.start.data))
            print("delete first next: "+str(self.start.next.data))
            self.start = self.start.next

    def deleteLast(self):
        if self.start==None:
            print("List is empty")
        else:
            temp = self.start
            print("delete_last temp: "+str(temp.data))
            while temp.next.next != None:
                temp = temp.next
                print("temp inside while: "+str(temp.data))
            lastnode = temp.next
            print("lastnode: "+str(lastnode.data))
            print("tempnext: "+str(temp.next.data))
            temp.next = None
            lastnode = None

    def deleteNodeAtGivenPosition(self, position):
        if self.start is None:
            return
        index = 0
        current = self.start
        print("current start: "+str(current.data))
        print("Index:"+str(index))
        print("Position:"+str(position))
        print("Current next: "+str(current.next.data))
        while current.next and index < position:
            previous = current
            print("previous_data: "+str(previous.data))
            current = current.next
            print("current data: "+str(current.data))
            index += 1
            print("Above Index: "+str(index))
        if index < position:
            print("here data")
            print("\nIndex is out of range.")
        elif index == 0:
            print("Here")
            self.start = self.start.next
        else:
            print("direct here")
            print("Previous next: "+str(previous.next.data))
            print("current next: "+str(current.next.data))
            # Unlink the node from linked list
            previous.next = current.next

    def insertLast(self, value):
        newNode = node(value)
        if(self.start == None):
            self.start=newNode
        else:
            temp = self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    
    

mylist = LinkedList() 
mylist.insertFirst(0)
mylist.insertLast(10)
mylist.insertLast(20)
mylist.insertLast(30)
mylist.insertLast(40)
mylist.insertLast(50)
mylist.insertLast(60)
mylist.insertMiddle(25,2)
mylist.viewList()
print()
mylist.deleteFirst()
print()
mylist.deleteLast()
mylist.deleteNodeAtGivenPosition(2)
print()
# mylist.viewList()
print()
# mylist.insertFirst(50)
print()
mylist.viewList()