import numpy as np
def eq(A, B, p):
    size = 1
    for e in A.shape : size = size*e
    check = A==B
    percent = np.sum(check)*100/size
    return percent >= p
def closest_point_indexes(points, p):
    idd = np.arange(points.shape[0])
    dis = (points[:,0]-p[0])**2+(points[:,1]-p[1])**2
    return idd[dis==np.min(dis)]
def number_of_inversions(A):
    diff = A-A.reshape(len(A),1)
    for i in range(len(A)):
        diff[i:,i] = 0
    return np.sum(diff<0)
exec(input().strip())