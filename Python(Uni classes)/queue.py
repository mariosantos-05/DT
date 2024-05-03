#first in first out (FIFO)

class Queue:
    def __init__(self):
        self.items = [];
        
    def isEmpty(self):
        return self.items == [];
    
    def enqueue(self, item):
        self.items.insert(0,item);
   
    def dequeue(self):
        return self.items.pop();
    def size(self):
        return len(self.items);
    
    
#Hot potato (exercice)

def H_Potato(num, listname):
    fila = Queue();
    for name in listname:
        fila.enqueue(name);
    while fila.size() > 1:
        for i in range(num):
            fila.enqueue(fila.dequeue());
        fila.dequeue();
            
    return fila.dequeue();        
    
    
    
print(H_Potato(10,["Ana", "Moon", "james", "John", "herbert"]))        
            
