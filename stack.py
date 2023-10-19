#LIFO (Last in, First out)

#Data-structure in python are implemented with creation of classes.


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

        
# paranteses balance (practice question)

def check(a):
    s = Stack();
    balanced = True;
    index = 0;
    quant = 0;
    while index < len(a) and balanced:
        symbol = a[index];
        if symbol == '(':
            s.push(symbol);
        else:
            if s.isEmpty():
                balanced = False;
            else:
                quant+= 1
                s.pop();
        index += 1; 
    return quant    

s = input();


print(check(s))