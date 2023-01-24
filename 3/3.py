#!/usr/bin/env python3
from calendar import c
import sys

def main():
    sum = 0
    filename = sys.argv[-1]
    linenum = 0
    common = []
    with open(filename) as f:
        for line in f:
            linenum = (linenum + 1) % 3 
            common.append(line)
            if linenum == 0:
                com = decode2(common)
                sum = sum + grabVal(com)
                common = []
    print(sum)

def decode2(common):
    for x in [*common[0]]:
        for y in [*common[1]]:
            for z in [*common[2]]:
                if x == y:
                    if x == z:
                        return(x)


def decode(line):
    compartment1 = slice(0,len(line)//2)
    compartment2 = slice(len(line)//2,len(line))
    for i in [*line[compartment1]]:
        for y in [*line[compartment2]]:
            if i == y:
                return(i)
  

def grabVal(letter):
    lets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    val = 1   
    for i in lets:       
        if letter == i:
            return val
        else:
            val = val+1 
    for i in lets:
        if letter.lower() == i:
            return val
        else:
            val = val+1

if __name__ == "__main__":
    main()
