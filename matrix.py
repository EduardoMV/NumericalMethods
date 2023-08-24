#%%
import numpy as np

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
A
# %%
a = np.array([[10,11,12]])
A = np.concatenate((A, a), axis=0)
#Axis 0 for row
#Axis 1 for col
A
# %%
