#!/usr/bin/env python3
import sys

def main():
    me = 0
    filename = sys.argv[-1]
    with open(filename) as f:
        for line in f:
            order = []
            order = line.split()
            if order[0] == 'A':
                if order[1] == 'X':
                    me = me + 0 + 3 
                elif order[1] == 'Y':
                    me = me + 3 + 1 
                elif order[1] == 'Z':
                    me = me + 6 + 2
            elif order[0] == 'B':
                if order[1] == 'X':
                        me = me + 0 + 1 
                elif order[1] == 'Y':
                        me = me + 3 + 2 
                elif order[1] == 'Z':
                        me = me + 6 + 3
            elif order[0] == 'C':
                if order[1] == 'X':
                        me = me + 0 + 2
                elif order[1] == 'Y':
                        me = me + 3 + 3 
                elif order[1] == 'Z':
                        me = me + 6 + 1
    
    print(me)
    

if __name__ == "__main__":
    main()
