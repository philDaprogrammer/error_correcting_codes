#!/usr/bin/env python3

from code import code

def dumpMatrix(M: list): 
    for row in M: 
        print(row)

def main():
    k = 4 
    n = 11
    c        = code(n, k)
    codeword = c.encode([1,1,1,1])    

    print(codeword) 

if __name__ == "__main__":
    main()
