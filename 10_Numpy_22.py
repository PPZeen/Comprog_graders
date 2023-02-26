import numpy as np
def mult_table(nrows, ncols):
    return np.arange(1,nrows+1).reshape((nrows,1)).dot(np.arange(1,ncols+1).reshape((1,ncols)))
#exec(input().strip())
print(mult_table(2,2))
print(mult_table(3,4))
print(mult_table(12,12))