import numpy as np


def linsolve_gaussian(A0, v0):
    # Initialization
    A = A0.copy()
    v = v0.copy()
    N = len(v)

    # Gaussian elimination
    for r in range(N):
        # Divide row r by diagonal element
        div = A[r, r]
        if (div == 0.):
            print(
                "Diagonal element is zero! Cannot solve the system with simple Gaussian elimination")
            return None
        A[r, :] /= div
        v[r] /= div

        # Now subtract this row from the Lower rows
        for r2 in range(r+1, N):
            mult = A[r2, r]
            A[r2, :] -= mult * A[r, :]
            v[r2] -= mult * v[r]

    # Backsubstitution
    x = np.empty(N, float)
    for r in range(N-1, -1, -1):
        x[r] = v[r]
        for c in range(r+1, N):
            x[r] -= A[r][c] * x[c]

    return x


def linsolve_gaussian_partialpivot(A0, v0):
    # Initialization
    A = A0.copy()
    v = v0.copy()
    N = len(v)

    # Gaussian elimination
    for r in range(N):
        # Find the pivot element (Largest in magnitude)
        r_pivot = r
        for i in range(r + 1, N):
            if (abs(A[i][r]) > abs(A[r_pivot][r])):
                r_pivot = i

        # Swap the rows
        A[[r, r_pivot]] = A[[r_pivot, r]]
        v[[r, r_pivot]] = v[[r_pivot, r]]

        # Divide row r by the pivot element
        div = A[r, r]
        if (div == 0.):
            print("Diagonal element is zero! The system appears to be singular")
            return None
        A[r, :] /= div
        v[r] /= div

        # Now subtract this row from the Lower rows
        for r2 in range(r+1, N):
            mult = A[r2, r]
            A[r2, :] -= mult * A[r, :]
            v[r2] -= mult * v[r]

    # Backsubstitution
    x = np.empty(N, float)
    for r in range(N-1, -1, -1):
        x[r] = v[r]
        for c in range(r+1, N):
            x[r] -= A[r][c] * x[c]

    return x


def lu_decomp(A):
    # Initialization
    U = A.copy()
    N = len(A)  # در تصویر len(v) بود که به دلیل عدم وجود v، به A اصلاح شد
    L = np.zeros((N, N), float)

    # Gaussian elimination
    for r in range(N):
        # Record the elements of L
        for r2 in range(r, N):
            L[r2][r] = U[r2][r]

        # Divide row r by diagonal element
        div = U[r, r]
        if (div == 0.):
            print(
                "Diagonal element is zero! LU decomposition without pivoting is not possible!")
            return None
        U[r, :] /= div

        # Now subtract this row from the Lower rows
        for r2 in range(r+1, N):
            mult = U[r2, r]
            U[r2, :] -= mult * U[r, :]

    return L, U


def solve_using_lu(L, U, v):
    # L * U * x = v
    # First solve L * y = v with forward substitution
    # Then solve U * x = y with backsubstitution
    # Initialization

    N = len(v)
    # Backsubstitution for L * y = v
    y = np.empty(N, float)
    for r in range(N):
        y[r] = v[r]
        for c in range(r):
            y[r] -= L[r][r - 1 - c] * y[r - 1 - c]
        y[r] /= L[r][r]

    # Backsubstitution for U * x = y
    x = np.empty(N, float)
    for r in range(N - 1, -1, -1):
        x[r] = y[r]
        for c in range(r + 1, N):
            x[r] -= U[r][c] * x[c]

    return x


def lu_decomp_partialpivot(A):
    # Initialization
    U = A.copy()
    N = len(A)
    L = np.zeros((N, N), float)

    # Keep track of all row swaps
    row_map = [i for i in range(N)]

    # Gaussian elimination
    for r in range(N):
        # Find the pivot element (Largest in magnitude)
        r_pivot = r
        for i in range(r + 1, N):
            if (abs(U[i][r]) > abs(U[r_pivot][r])):
                r_pivot = i

        row_map[r], row_map[r_pivot] = row_map[r_pivot], row_map[r]
        U[[r, r_pivot]] = U[[r_pivot, r]]
        L[[r, r_pivot]] = L[[r_pivot, r]]

        # Record the elements of L
        for r2 in range(r, N):
            L[r2][r] = U[r2][r]

        # Divide row r by the pivot element
        div = U[r, r]
        if (div == 0.):
            print("Diagonal element is zero! The system appears to be singular")
            return None
        U[r, :] /= div

        # Now subtract this row from the Lower rows
        for r2 in range(r + 1, N):
            mult = U[r2, r]
            U[r2, :] -= mult * U[r, :]

    return L, U, row_map


def solve_using_lu_partialpivot(L, U, row_map, v):
    # L*U*x = v
    # First solve L*y = v with forward substitution
    # Then solve U*x = y with backsubstitution
    # Initialization

    N = len(v)
    # Backsubstitution for L*y = v
    y = np.empty(N, float)
    for rr in range(N):
        r = row_map[rr]
        y[rr] = v[r]
        for c in range(rr):
            y[rr] -= L[rr][rr - 1 - c] * y[rr - 1 - c]
        y[rr] /= L[rr][rr]

    # Backsubstitution for U*x = y
    x = np.empty(N, float)
    for rr in range(N - 1, -1, -1):
        x[rr] = y[rr]
        for c in range(rr + 1, N):
            x[rr] -= U[rr][c] * x[c]

    return x


# tests :
# ----------------------------------------------------------------
print("linsolve_gaussian : \n")
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)

v = np.array([-4, 3, 9, 7], float)

x = linsolve_gaussian(A, v)

print("x = ", x)
print("Ax = ", A.dot(x))
print("v", v)

# Terminal :

# x =  [ 2. -1. -2.  1.]
# Ax =  [-4.  3.  9.  7.]
# v [-4.  3.  9.  7.]
# ----------------------------------------------------------------
print("\nlinsolve_gaussian_partialpivot : \n")
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)

v = np.array([-4, 3, 9, 7], float)

x = linsolve_gaussian_partialpivot(A, v)

print("x = ", x)
print("Ax = ", A.dot(x))
print("v = ", v)

# Terminal :

# x =  [ 2. -1. -2.  1.]
# Ax =  [-4.  3.  9.  7.]
# v =  [-4.  3.  9.  7.]
# ----------------------------------------------------------------
print("\nlu_decomp : \n")
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)

L, U = lu_decomp(A)

print("L = ", L)
print("U = ", U)
print("LU = ", np.dot(L, U))
print("A = ", A)

# Terminal :

# L =  [[  2.    0.    0.    0. ]
# [  3.    2.5   0.    0. ]
# [  1.   -4.5 -13.6   0. ]
# [  2.   -3.  -11.4  -1. ]]
# U =  [[ 1.   0.5  2.   0.5]
# [ 0.   1.  -2.8 -1. ]
# [-0.  -0.   1.  -0. ]
# [-0.  -0.  -0.   1. ]]
# LU =  [[ 2.  1.  4.  1.]
# [ 3.  4. -1. -1.]
# [ 1. -4.  1.  5.]
# [ 2. -2.  1.  3.]]
# A =  [[ 2.  1.  4.  1.]
# [ 3.  4. -1. -1.]
# [ 1. -4.  1.  5.]
# [ 2. -2.  1.  3.]]
# ----------------------------------------------------------------
print("\nsolve_using_lu : \n")
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)

L, U = lu_decomp(A)

v = np.array([-4, 3, 9, 7], float)
x = solve_using_lu(L, U, v)

print("x = ", x)
print("Ax = ", A.dot(x))
print("v = ", v)

# Terminal :

# x =  [ 2. -1. -2.  1.]
# Ax =  [-4.  3.  9.  7.]
# v =  [-4.  3.  9.  7.]
# ----------------------------------------------------------------
print("\nsolve_using_lu_partialpivot : \n")
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)

L, U, row_map = lu_decomp_partialpivot(A)

v = np.array([-4, 3, 9, 7], float)
x = solve_using_lu_partialpivot(L, U, row_map, v)

print("x = ", x)
print("Ax = ", A.dot(x))
print("v = ", v)

# Terminal :

# x =  [ 2. -1. -2.  1.]
# Ax =  [-4.  3.  9.  7.]
# v =  [-4.  3.  9.  7.]
