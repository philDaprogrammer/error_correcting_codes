#!/usr/bin/env python3

from code import code

def dumpMatrix(M: list): 
    for row in M:  
        print("[ ", end="")

        for elem in row: 
            print("{:>2} ".format(elem), end="")

        print(" ]")

def main():
    c        = code(16, 4)
    codeword = c.encode([1,2,3,4])    

    dumpMatrix(c.G)
    print("\n" + str(codeword))

if __name__ == "__main__":
    main()
