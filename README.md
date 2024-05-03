# Data Structures Implementation in C++ (and a little of python)

This repository contains implementations of basic linear data structures in C++.

## Introduction

In this repository, you will find C++ implementations of the following data structures:

- Arrays
- Linked Lists (Singly and Doubly)
- Stacks
- Queues

Each data structure is implemented as a separate C++ class, with member functions to perform common operations such as insertion, deletion, and traversal.

## Getting Started

To get started, clone this repository to your local machine:

git clone https://github.com/mariosantos-05/DT.git


Ensure you have a C++ compiler installed on your computer. You can use popular compilers like GCC or Clang.

## Usage

Each data structure is implemented in its own `.cpp` file. You can include these files in your C++ projects or use them directly for learning purposes.

To use a data structure in your own code, include the corresponding header file and create an instance of the class:

```cpp
#include "Array.h"

int main() {
    // Example usage of Array class
    Array<int> arr(5); // Create an array of integers with size 5
    arr.insert(10);    // Insert element 10 at index 0
    arr.insert(20);    // Insert element 20 at index 1
    // Perform other operations...
    return 0;
}
