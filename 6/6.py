#!/usr/bin/env python3
import sys

# p1
# def main():
#     filename = sys.argv[-1]
#     with open(filename) as f:
#         contents = f.read()
#         for i in range(4, len(contents)):
#             this = set(contents[i-4:i])
#             if len(this) == 4:
#                 print(i)
#                 break

# p2 
def main():
    filename = sys.argv[-1]
    with open(filename) as f:
        contents = f.read()
        for i in range(14, len(contents)):
            this = set(contents[i-14:i])
            if len(this) == 14:
                print(i)
                break

if __name__ == "__main__":
    main()
