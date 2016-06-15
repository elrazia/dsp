# Matrix Algebra

import numpy as np

# define matrices, arrays, and scalar
A = np.mat([[1,2,3],[2,7,4]])
B = np.mat([[1,-1],[0,1]])
C = np.mat([[5,-1],[9,1],[6,0]])
D = np.mat([[3,-2,-1],[1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1],[8],[0],[5]])
alpha = 6

# 1. Matrix Dimensions

print A.shape
# 2x3
print B.shape
# 2x2
print C.shape
# 3x2
print D.shape
# 2x3
print u.shape
# 1x4
print w.shape
# 4x1

# 2. Vector Operations

print u + v
# [[ 9  7 -4  9]]
print u - v
# [[ 3 -3 -2  1]]
print alpha*u
# [[ 36  12 -18  30]]
print np.dot(u,v)
# 51
print np.linalg.norm(u)
# 8.60232526704

# 3. Matrix Operations

print A + C
# not defined
print A + C.T
# [[-4 -7 -3], [ 3  6  4]]
print C.T + 3*D
# [[14  3  3], [ 2  7  9]]
print B*A
# [[-1 -5 -1], [ 2  7  4]]
print B*A.T
# not defined

# Optional

print B*C
# not defined
print C*B
# [[ 5 -6], [ 9 -8], [ 6 -6]]
print B**4
# [[ 1 -4], [ 0  1]]
print A*A.T
# [[14 28], [28 69]]
print D.T*D
# [[10 -4  0], [-4  8  8], [ 0  8 10]]
