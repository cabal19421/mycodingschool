__author__ = 'advoc'

class Node:
    data = None
    link = None

    def __init__(self):
        self.data = None
        self.link = None

    def __init__(self, val):
        self.data = val
        self.link = None

    def print(self):
        if self.link is None:
            print("[" + str(self.data) + "]")
        else:
            print("[" + str(self.data) + ", " + "->" + "]")

    def to_str(self):
        if self.link is None:
            return "[" + str(self.data) + "]"
        else:
            return "[" + str(self.data) + ", " + "->" + "]"

class DynamicListAsSinglyLinkedList:
    start = None
    size = 0

    def get_len(self):
        return self.size

    def add(self, val):
        new = Node(val)
        current = self.start
        while current is not None and current.link is not None:
            current = current.link
        if current is None:
            self.start = new
        else:
            current.link = new
        self.size += 1
        self.print()

    def add_at(self, val, pos):
        """Add val at pos in the list. Pos is 0th based index. Worst case O(n) at the end of the list"""
        new = Node(val)
        if self.size == 0: # adding to an empty list
             self.start = new
        elif pos == 0: # adding to the beginning of the list
            prev = self.start
            self.start = new
            self.start.link = prev
        elif self.size == 1:
            self.start.link = new
        else:
            count = 0
            current = self.start
            while (count < self.size) and (count < pos): # traverse the list to find the node where we want to add
                prev = current
                current = current.link
                count += 1
            temp = prev.link
            prev.link = new
            new.link = temp
        self.size += 1
        self.print()

    def remove_at(self, pos):
        """Add Remove the value at pos in the list. Pos is 0th based index. Worst case O(n) at the end of the list"""
        if self.size == 0:
            return
        elif pos == 0:
            self.start = self.start.link
        elif self.size == 1:
            self.start = None
        else:
            current = self.start
            count = 1 # start at one since we're initializing at one
            while (count < self.size) and (count < pos): # traverse the list to find the node where we want to remove
                prev = current
                current = current.link
                count += 1
            temp = current
            prev.link = current.link
            temp.link = None
        self.size -= 1
        self.print()


    def remove(self):
        if self.size == 0:
            self.print()
            return
        if self.size == 1:
            self.start = None
            self.size -= 1
            self.print()
            return
        current = self.start
        while current.link is not None:
            prev = current
            current = current.link
        prev.link = None
        self.size -= 1
        self.print()

    def print(self):
        current = self.start
        result = ""
        if current is not None:
            result += current.to_str()
            result += " "
        while current is not None and current.link is not None:
            current = current.link
            result += current.to_str()
            result += " "
        result += " size=" + str(self.size)
        print(result.strip())

    def reset(self):
        for x in range(self.size, 0, -1):
            self.remove_at(x)
            
            
            
            
            
#
#
#class node:
#
#    def __init__(self):
#        self.data = None
#        self.next = None
#        
#        
#class linkedlist:
#    
#    def __init__(self):
#            self.size = 0
#            self.head = None
#            
#
#    def add(self, newnode, pos = None):
#
#        tmp = self.head
#        if pos is not None and pos<=self.size:
#            cnt = 0
#            prev = None
#            while cnt < pos:
#                prev = tmp
#                tmp=tmp.next
#                cnt+=1
#            if prev == None:
#                self.head=newnode
#                newnode.next=tmp
#            else:
#                prev.next=newnode
#                newnode.next=tmp
#        else:
#            if not self.head:
#                self.head = newnode
#                return
#            else:
#                while tmp.next != None:
#                    tmp=tmp.next
#                tmp.next = newnode
#        self.size+=1
#    
#
#    def prt_list(self):
#
#        tmp = self.head
#        while tmp != None:
#            print tmp.data
#            tmp=tmp.next
#        print "\n\n"
#            
#
#if __name__ == "__main__":
#    jqll = linkedlist()
#    
#    newnode = node()
#    newnode.data = "your mom"
#    jqll.add(newnode)
#    jqll.prt_list()
#    
#    assnode = node()
#    assnode.data = "your sister"
#    jqll.add(assnode)
#    jqll.prt_list()
#    
#    mehnode = node()
#    mehnode.data = "your mom again"
#    jqll.add(mehnode)
#    jqll.prt_list()
#    
#    dicnode = node()
#    dicnode.data = "ima shove my self into the ll"
#    jqll.add(dicnode,2)
#    jqll.prt_list()
#    
#    eicnode = node()
#    eicnode.data = "ima shove my self into the ll # 2"
#    jqll.add(eicnode,0)
#    jqll.prt_list()
#    
#    ticnode = node()
#    ticnode.data = "ima shove my self into the ll # 3"
#    jqll.add(ticnode,jqll.size+1)
#    jqll.prt_list()
#    
