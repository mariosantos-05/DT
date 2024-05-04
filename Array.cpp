#include <iostream>
#include <stdexcept>

template <typename T>
class Array{
private:
    T* data;
    int size; //current position/size of the array
    int capacity;

    void resize(int newCapacity){
        T* newData = new T[newCapacity];
        for(int i = 0; i < size; ++i){
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
        capacity = newCapacity;
    }

public:
    Array(int capacity) : size(0), capacity(capacity){
        data = new T[capacity];
    }

    ~Array(){
        delete[] data;
    };
    
    //Insert element in the end of the array
    void insert(const T& element){
            if(size >= capacity){
                resize(capacity * 2);
            }
            data[size++] = element;
    }

    // Acess element at index
    T& at(int index){
        if(index < 0 || index >= size){
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }
    
    //Getter's
    int getSize() const{
        return size;
    }

    int getCapacity() const{
        return capacity;
    }

};

int main() {
    Array<int> arr(5); 
    arr.insert(10);    
    arr.insert(20);    
    arr.insert(30);    

    std::cout << "Array elements: ";
    for (int i = 0; i < arr.getSize(); ++i) {
        std::cout << arr.at(i) << " ";
    }
    std::cout << std::endl;

    return 0;
}