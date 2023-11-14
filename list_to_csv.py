#!/usr/bin/env python3

# example code for Josh. 

# list -> csv
import csv 
data = [['1'], ['2'], ['3'],['4']] 
with open('nums.csv', 'w') as f:
    write = csv.writer(f) 
    write.writerows(data)

print('Downloaded!')
