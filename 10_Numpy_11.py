import numpy as np
def get_column_from_bottom_to_top( A, c ):
    return A[::-1,-c] 
def get_odd_rows( A ):
    return A[1::2,:]
def get_even_column_last_row( A ):
    return A[-1,::2]
def get_diagonal1( A ):
    B = A*np.identity((A.shape[0]),int)
    return B[B!=0]
def get_diagonal2( A ):
    return np.array([A[:,::-1][i,i] for i in range(A.shape[0])])
#exec(input().strip())
#A=np.array([[1,2],[3,4]]);print(get_column_from_bottom_to_top(A,1))
#A=np.array([[1,2],[3,4],[5,6],[7,8]]);print(get_odd_rows(A)) 
#A=np.array([[1,2,3],[4,5,6]]);print(get_even_column_last_row(A))
#A=np.array([[1,2,3],[4,5,6],[7,8,9]]);print(get_diagonal1(A))
A=np.array([[1,2,3],[4,5,6],[7,8,9]]);print(get_diagonal2(A)) 
A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]);print(get_diagonal2(A))
