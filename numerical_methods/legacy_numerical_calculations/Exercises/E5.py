def matrix_inverse_with_ludecomp(A):
    # First step: LU decomposition of matrix A
    L, U, row_map = lu_decomp_partialpivot(A)
    N = len(row_map)

    Ain = A.copy()
    for c in range(N):
        v = np.zeros(N, float)
        v[c] = 1.
        x = solve_using_lu_partialpivot(L,U,row_map,v)
        Ainv[:,c] = x

    return Ainv

# ----------------------------------------------------------------
print("matrix_inverse_with_ludecomp : \n")
A = np.array([[ 0,  1,  4,  1],
              [ 3,  4, -1, -1],
              [ 1, -4,  1,  5],
              [ 2, -2,  1,  3]], float)

Ainv = matrix_inverse_with_ludecomp(A)
print("A*A^{-1} = \n", tabulate(A.dot(Ainv)))
# ----------------------------------------------------------------
print("matrix_inverse_with_ludecomp : \n")
