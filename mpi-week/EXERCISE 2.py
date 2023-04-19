#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True :
    if RANK == 0 :
        data = int(input('enter a number : '))
    else :
        data = None

    data = COMM.bcast(data , root = 0)
    
    if data < 0 :
        break

    print(f"The Process {RANK} got the data {data}")

    COMM.Barrier()

