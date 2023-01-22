#!/usr/bin/env python3
import sys

def main():
    cals = 0
    calslist = []
    filename = sys.argv[-1]
    with open(filename) as f:
        for line in f:
            if line == '\n':
                calslist.append(cals)
                cals = 0
            else:
                cals = cals + int(line)

    GetTopThree(calslist)

def GetTopThree(list):
    sum = 0
    for i in range(3):
        sum = sum + max(list)
        list.remove(max(list))
    print(sum)
    
    

if __name__ == "__main__":
    main()
