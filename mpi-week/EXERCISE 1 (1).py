#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#  1
print("Hello World")

#  2
print("Hello World from process %d of %d" % (rank, size))

# 3
if rank == 0:
    print("Hello World from process %d of %d" % (rank, size))

# 4
# If you omit the final MPI procedure call, the program may not terminate properly and can lead to unexpected behavior. Always call MPI.Finalize() at the end of your MPI program.
MPI.Finalize()

