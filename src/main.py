#!/usr/bin/env python3

from code import code

def dumpMatrix(M: list): 
    for row in M: 
        print(row)

def sum_vector(v: list): 
    s = 0 

    for elem in v: 
        s += elem

    return s

def main():
    c        = code(11, 4)
    codeword = c.encode([1,2,3,4])    

    print(codeword)


if __name__ == "__main__":
    main()
