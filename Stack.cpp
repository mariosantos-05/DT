#include <iostream>
#include <stdexcept>

template <typename T>
class Stack{
private:
    T* data; //pointer to the data in focus
    int TopIndex;
    int capacity;
    
public:
    Stack(int capacity) : TopIndex(-1), capacity(capacity) {
        data = new T[capacity];
    }
    ~Stack(){
        delete[] data;
    }
    bool isFull() const{
        return TopIndex == capacity - 1;
    }
    bool isEmpty() const{
        return TopIndex == -1;
    }

    void push(const T& element){
        if(isFull()){
            throw std::overflow_error("Stack Overflow"); 
        }
        data[++TopIndex] = element;
    }
    T pop(){
        if(isEmpty()){
            throw std::underflow_error("Stack Underflow");
        }
        return data[TopIndex--];
    };

    T& peek(){
        if(isEmpty){
            throw std::underflow_error("Stack in empty");
        }
        return data[TopIndex];
    }
};

int main(){
    Stack<int> stack(5);
}