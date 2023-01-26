#!/usr/bin/env python3
import sys

directories = {

}
currentDir = []
filename = sys.argv[-1]
with open(filename) as f:
    for line in f:
            line = line.split()
            if line[0] == '$':
                if line[1] == 'cd':
                    name = line[2]
                    if name == '..':
                        currentDir.pop()
                    else:
                        if name not in directories:
                            directories[name] = {}
                            currentDir.append(name)
                            directories = directories[name]
                           

                    

                
   
