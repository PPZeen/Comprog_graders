import numpy as np

def sum_2_rows( M ):
    return M[::2,:] + M[1::2,:]
def sum_left_right( M ):
    return M[:,:int(M.shape[1]/2):] + M[:,int(M.shape[1]/2)::]
def sum_upper_lower( M ):
    return M[:int(M.shape[0]/2):,:] + M[int(M.shape[0]/2)::,:]
def sum_4_quadrants( M ):
    r = int(M.shape[0]/2)
    c = int(M.shape[1]/2)
    return M[:r:,:c:] + M[:r:,c::] + M[r::,:c:] + M[r::,c::]
def sum_4_cells( M ):
    return sum_2_rows(M)[:,0::2] + sum_2_rows(M)[:,1::2]
def count_leap_years( years ):
    p = (years-543)%400 == 0
    f = (years-543)%4 == 0
    o = (years-543)%100 != 0
    #sum((years-543)%400 == 0)+sum(((years-543)%4 == 0)&((years-543)%100 != 0))
    return sum(p) + sum(f&o)
    
#exec(input().strip())
print(sum_2_rows(np.arange(36).reshape(6,6)))
print(sum_left_right(np.arange(36).reshape(6,6)))
print(sum_upper_lower(np.arange(36).reshape(6,6)))
print(sum_4_quadrants(np.arange(36).reshape(6,6)))
print(sum_4_cells(np.arange(36).reshape(6,6))) 
print(count_leap_years(np.array([2543,2559,2560]))) 