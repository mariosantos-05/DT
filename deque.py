#can be refered as Double-ended queue


class Deque:
    def __init__(self):
        self.items = [];
        
    def isEmpty(self):
        return self.items == [];
    def addFront(self, item):
        self.items.append(item);
        
    def addRear(self, item):
        self.items.insert(0,item);
        
    def removeFront(self):
        return self.items.pop();
    
    def removeRear(self):
        return self.items.pop(0);
    
    def size(self):
        return len(self.items);
    
    
#palindrome exercice

def palindrome(s):
    chard = Deque()

    for ch in s:
        chard.addRear(ch)

    equall = True

    while chard.size() > 1 and equall:
        r = chard.removeFront()
        l = chard.removeRear()
        if r != l:
            equall = False

    return equall



print(palindrome('Abacate'))