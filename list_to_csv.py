#!/usr/bin/env python
# coding: utf-8

# In[4]:


# example code for Josh. 
# list -> csv
import csv 
data = [['1'], ['2'], ['3'],['4']] 
with open('nums.csv', 'w') as f:
    write = csv.writer(f) 
    write.writerows(data)

print('Downloaded!')

# In[ ]:




