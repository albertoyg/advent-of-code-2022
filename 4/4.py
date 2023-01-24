#!/usr/bin/env python3
from itertools import count
import sys


## #p1
# def main():
#     count=0
#     filename = sys.argv[-1]
#     with open(filename) as f:
#         for line in f:
#             sections = line.split(',')
#             section1 = sections[0].split('-')
#             section2 = sections[1].split('-')
#             if(int(section1[0])==int(section1[1])):
#                 range1 = set([int(section1[0])])
#             else:
#                 range1 = set()
#                 for i in range(int(section1[0]),int(section1[1])+1):
#                     range1.add(i)
#             if(int(section2[0])==int(section2[1])):
#                 range2 = set([int(section2[0])])
#             else:
#                 range2 = set()
#                 for i in range(int(section2[0]),int(section2[1])+1):
#                     range2.add(i)
#             if range1.issubset(range2) or range2.issubset(range1) :
#                 count = count + 1 
#     print(count)

#p2
def main():
    count=0
    filename = sys.argv[-1]
    with open(filename) as f:
        for line in f:
            sections = line.split(',')
            section1 = sections[0].split('-')
            section2 = sections[1].split('-')
            if(int(section1[0])==int(section1[1])):
                range1 = set([int(section1[0])])
            else:
                range1 = set()
                for i in range(int(section1[0]),int(section1[1])+1):
                    range1.add(i)
            if(int(section2[0])==int(section2[1])):
                range2 = set([int(section2[0])])
            else:
                range2 = set()
                for i in range(int(section2[0]),int(section2[1])+1):
                    range2.add(i)
            if range1 & range2:
                count = count + 1
            
        print(count)


        

if __name__ == "__main__":
    main()
