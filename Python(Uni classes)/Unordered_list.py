#Linked list have the need of the "Node" structure.

class Node:
    def __init__(self, initdata):
        self.data = initdata;
        self.next = None;
    
    def getData(self):
        return self.data;
    
    def GetNext(self):
        return self.next;
    
    def setData(self,newdata):
        self.data = newdata;
        
    def setNext(self, newnext):
        self.next = newnext;
        
class UnorderedList:
    def __init__(self):
        self.head = None;
        
    def isEmpty(self):
        return self.head == None;
    
    def add(self, item):
        aux = Node(item);
        aux.setNext(self.head);
        self.head = aux;    
        
    def size(self):
        count = 0;
        current = self.head;
        while current != None:
            count += 1;
            current = current.GetNext();
        return count;
    
    def search(self, item):
        current = self.head;
        found = False;
        while current != None and not found:
            if current.getData() == item:
                found = True;
            else:
                current = current.GetNext()
        return found;
    
    def remove(self,item):
        current = self.head;
        previous = None;
        found = False;
        while not found:
            if current.getData() == item:
                found = True;
            else:
                previous = current;
                current = current.GetNext();
        if previous == None:
            self.head = current.GetNext();
        else:
            previous.setNext(current.GetNext());        
                                              

