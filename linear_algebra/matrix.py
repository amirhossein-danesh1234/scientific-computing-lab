def _is_square(matrix):
    """Return True when the matrix is non-empty and each row has equal length."""
    if not matrix:
        return False
    size = len(matrix)
    return all(len(row) == size for row in matrix)


def _minor(matrix, column):
    """Return the minor obtained by removing the first row and the given column."""
    return [row[:column] + row[column + 1 :] for row in matrix[1:]]


def matrix_determinant(matrix):
    """Recursively calculate the determinant of a square matrix."""
    if not _is_square(matrix):
        raise ValueError("Determinant is defined only for non-empty square matrices.")

    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for column, value in enumerate(matrix[0]):
        sign = -1 if column % 2 else 1
        determinant += sign * value * matrix_determinant(_minor(matrix, column))
    return determinant


def matrix_show(matrix):
    """Pretty-print a matrix with aligned columns."""
    if not matrix:
        print("[]")
        return

    max_width = max(len(str(item)) for row in matrix for item in row)
    rows = len(matrix)
    for idx, row in enumerate(matrix):
        left = "[" if idx == 0 else "|"
        right = "]" if idx == rows - 1 else "|"
        formatted_row = " ".join(f"{str(value):>{max_width}}" for value in row)
        print(f"{left} {formatted_row} {right}")


def matrix_to_string(matrix):
    """Return a string representation similar to matrix_show."""
    if not matrix:
        return "[]"
    max_width = max(len(str(item)) for row in matrix for item in row)
    rows = len(matrix)
    lines = []
    for idx, row in enumerate(matrix):
        left = "[" if idx == 0 else "|"
        right = "]" if idx == rows - 1 else "|"
        formatted_row = " ".join(f"{str(value):>{max_width}}" for value in row)
        lines.append(f"{left} {formatted_row} {right}")
    return "\n".join(lines)


def _cofactor_matrix(matrix):
    """Return the cofactor matrix of a square matrix."""
    if not _is_square(matrix):
        raise ValueError("Cofactor is defined only for square matrices.")

    n = len(matrix)
    if n == 0:
        raise ValueError("Empty matrix has no cofactor matrix.")

    cof = []
    for i in range(n):
        cof_row = []
        for j in range(n):
            # Build minor for element (i, j)
            sub = [row[:j] + row[j + 1 :] for k, row in enumerate(matrix) if k != i]
            sign = -1 if (i + j) % 2 else 1
            cof_row.append(sign * matrix_determinant(sub))
        cof.append(cof_row)
    return cof


def _transpose(matrix):
    return [list(row) for row in zip(*matrix)] if matrix else []


def _adjugate(matrix):
    return _transpose(_cofactor_matrix(matrix))


def matrix_inverse(matrix):
    """Return the inverse of a square matrix using adjugate/determinant method.

    Raises ValueError when the matrix is not square or singular.
    """
    if not _is_square(matrix):
        raise ValueError("Inverse is defined only for non-empty square matrices.")

    det = matrix_determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and not invertible (determinant = 0).")

    adj = _adjugate(matrix)
    inv = [[elem / det for elem in row] for row in adj]
    return inv


def matrix_multiply(A, B):
    """Multiply two matrices A (n x m) and B (m x p).

    Validates rectangular shapes and inner-dimension compatibility.
    Returns the n x p product matrix.
    """
    if not A or not B:
        raise ValueError("Both matrices must be non-empty.")

    n = len(A)
    m = len(A[0])
    # Validate A is rectangular
    if any(len(row) != m for row in A):
        raise ValueError("Left matrix is not rectangular.")

    m2 = len(B)
    p = len(B[0])
    # Validate B is rectangular
    if any(len(row) != p for row in B):
        raise ValueError("Right matrix is not rectangular.")

    if m != m2:
        raise ValueError("Inner dimensions do not match for multiplication (A: n x m, B: m x p).")

    # Compute product
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def get_matrix():
    matrix = []
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input(f"Enter the element at row {i + 1} and column {j + 1}: ")))
        matrix.append(row)
    return matrix

def inverse_matrix(matrix):
    determinant = matrix_determinant(matrix)
    if determinant == 0:
        return "The matrix is not invertible"
    else:
        return "The matrix is invertible"
    adjugate_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        adjugate_matrix.append(row)
    return adjugate_matrix

def matrix_product(matrix_1, matrix_2):
    """Backward-compatible wrapper for matrix multiplication."""
    return matrix_multiply(matrix_1, matrix_2)


# -------- Additional core utilities --------

def shape(A):
    return (len(A), len(A[0]) if A else 0)


def is_rectangular(A):
    return bool(A) and all(len(row) == len(A[0]) for row in A)


def zeros(n, m):
    return [[0.0 for _ in range(m)] for _ in range(n)]


def identity(n):
    I = zeros(n, n)
    for i in range(n):
        I[i][i] = 1.0
    return I


def diagonal_matrix(diag):
    n = len(diag)
    D = zeros(n, n)
    for i, v in enumerate(diag):
        D[i][i] = float(v)
    return D


def matrix_add(A, B):
    n, m = shape(A)
    n2, m2 = shape(B)
    if n != n2 or m != m2:
        raise ValueError("Matrices must have the same shape for addition.")
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]


def matrix_sub(A, B):
    n, m = shape(A)
    n2, m2 = shape(B)
    if n != n2 or m != m2:
        raise ValueError("Matrices must have the same shape for subtraction.")
    return [[A[i][j] - B[i][j] for j in range(m)] for i in range(n)]


def scalar_multiply(alpha, A):
    return [[alpha * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def conjugate(A):
    return [[complex(A[i][j]).conjugate() for j in range(len(A[0]))] for i in range(len(A))]


def conjugate_transpose(A):
    return _transpose(conjugate(A))


def trace(A):
    if not _is_square(A):
        raise ValueError("Trace is defined only for square matrices.")
    return sum(A[i][i] for i in range(len(A)))


def gauss_jordan_inverse(A):
    if not _is_square(A):
        raise ValueError("Inverse is defined only for square matrices.")
    n = len(A)
    # Make augmented matrix [A | I]
    aug = [list(map(float, A[i])) + identity(n)[i] for i in range(n)]
    # Perform Gauss-Jordan with partial pivoting
    for col in range(n):
        # Pivot
        pivot_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot_row][col]) < 1e-12:
            raise ValueError("Matrix is singular and not invertible.")
        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        # Normalize pivot row
        pivot = aug[col][col]
        factor = pivot
        aug[col] = [v / factor for v in aug[col]]
        # Eliminate other rows
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor != 0:
                aug[r] = [aug[r][c] - factor * aug[col][c] for c in range(2 * n)]
    # Extract inverse
    inv = [row[n:] for row in aug]
    return inv


def lu_decomposition(A):
    """LU with partial pivoting. Returns P, L, U, swaps.

    P*A = L*U
    """
    if not is_rectangular(A) or not _is_square(A):
        raise ValueError("LU needs a square matrix.")
    n = len(A)
    U = [list(map(float, row)) for row in A]
    L = identity(n)
    P = identity(n)
    swaps = 0
    for k in range(n):
        # Pivot
        pivot = max(range(k, n), key=lambda r: abs(U[r][k]))
        if abs(U[pivot][k]) < 1e-12:
            raise ValueError("Matrix is singular to working precision.")
        if pivot != k:
            U[k], U[pivot] = U[pivot], U[k]
            P[k], P[pivot] = P[pivot], P[k]
            if k > 0:
                L[k][:k], L[pivot][:k] = L[pivot][:k], L[k][:k]
            swaps += 1
        # Eliminate below
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            for j in range(k, n):
                U[i][j] -= L[i][k] * U[k][j]
    return P, L, U, swaps


def det_lu(A):
    P, L, U, swaps = lu_decomposition(A)
    detU = 1.0
    for i in range(len(U)):
        detU *= U[i][i]
    return (-1 if swaps % 2 else 1) * detU


def rank(A, tol=1e-10):
    # Row-reduction to RREF and count nonzero rows
    M = [list(map(float, row)) for row in A]
    n, m = shape(M)
    r = 0
    for c in range(m):
        # Find pivot
        pivot = max(range(r, n), key=lambda i: abs(M[i][c]))
        if abs(M[pivot][c]) <= tol:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        # Normalize row r
        factor = M[r][c]
        M[r] = [v / factor for v in M[r]]
        # Eliminate other rows
        for i in range(n):
            if i == r:
                continue
            factor = M[i][c]
            if abs(factor) > 0:
                M[i] = [M[i][j] - factor * M[r][j] for j in range(m)]
        r += 1
        if r == n:
            break
    return r


def is_hermitian(A, tol=1e-8):
    if not _is_square(A):
        return False
    H = conjugate_transpose(A)
    n = len(A)
    for i in range(n):
        for j in range(n):
            if abs(complex(A[i][j]) - complex(H[i][j])) > tol:
                return False
    return True


def is_orthogonal(A, tol=1e-8):
    if not _is_square(A):
        return False
    At = _transpose(A)
    AtA = matrix_multiply(At, A)
    I = identity(len(A))
    n = len(A)
    for i in range(n):
        for j in range(n):
            if abs(AtA[i][j] - I[i][j]) > tol:
                return False
    return True


def is_unitary(A, tol=1e-8):
    if not _is_square(A):
        return False
    AhA = matrix_multiply(conjugate_transpose(A), A)
    I = identity(len(A))
    n = len(A)
    for i in range(n):
        for j in range(n):
            if abs(complex(AhA[i][j]) - complex(I[i][j])) > tol:
                return False
    return True


def upper_triangularize(A):
    # Return an upper-triangular form via elimination (does not return multipliers)
    U = [list(map(float, row)) for row in A]
    n, m = shape(U)
    r = 0
    for c in range(m):
        if r >= n:
            break
        # pivot
        pivot = max(range(r, n), key=lambda i: abs(U[i][c]))
        if abs(U[pivot][c]) < 1e-12:
            continue
        U[r], U[pivot] = U[pivot], U[r]
        # eliminate below
        for i in range(r + 1, n):
            if U[r][c] == 0:
                continue
            factor = U[i][c] / U[r][c]
            for j in range(c, m):
                U[i][j] -= factor * U[r][j]
        r += 1
    return U


def normalize_vector(v):
    import math
    norm = math.sqrt(sum((abs(x) ** 2 for x in v)))
    if norm == 0:
        return v
    return [x / norm for x in v]


def qr_decomposition(A):
    # Modified Gram-Schmidt
    n, m = shape(A)
    Q = zeros(n, m)
    R = zeros(m, m)
    # Work on copy of columns
    V = [[A[i][j] for i in range(n)] for j in range(m)]
    for j in range(m):
        for i in range(j):
            R[i][j] = sum(Q[r][i] * V[j][r] for r in range(n))
            for r in range(n):
                V[j][r] -= R[i][j] * Q[r][i]
        norm = (sum(V[j][r] * V[j][r] for r in range(n))) ** 0.5
        if norm < 1e-15:
            continue
        R[j][j] = norm
        for r in range(n):
            Q[r][j] = V[j][r] / norm
    return Q, R


def power_method(A, max_iter=1000, tol=1e-10):
    import random
    n, m = shape(A)
    if n != m:
        raise ValueError("Power method needs a square matrix.")
    v = [random.random() for _ in range(n)]
    v = normalize_vector(v)
    eigval_old = 0.0
    for _ in range(max_iter):
        Av = [sum(A[i][k] * v[k] for k in range(n)) for i in range(n)]
        v = normalize_vector(Av)
        eigval = sum(v[i] * Av[i] for i in range(n))
        if abs(eigval - eigval_old) < tol:
            break
        eigval_old = eigval
    return eigval, v


def qr_eigenvalues(A, max_iter=200, tol=1e-12):
    # Basic QR iteration for eigenvalues (good for symmetric A)
    Ak = [row[:] for row in A]
    n, m = shape(Ak)
    if n != m:
        raise ValueError("QR eigenvalues require a square matrix.")
    for _ in range(max_iter):
        Q, R = qr_decomposition(Ak)
        Ak1 = matrix_multiply(R, Q)
        # Convergence: sum of absolute subdiagonal entries
        off = sum(abs(Ak1[i][j]) for i in range(n) for j in range(n) if i > j)
        Ak = Ak1
        if off < tol:
            break
    return [Ak[i][i] for i in range(n)]


def matrix_power(A, n):
    if not _is_square(A):
        raise ValueError("Matrix power requires a square matrix.")
    if n == 0:
        return identity(len(A))
    if n < 0:
        A = gauss_jordan_inverse(A)
        n = -n
    # Exponentiation by squaring
    result = identity(len(A))
    base = [row[:] for row in A]
    while n > 0:
        if n & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        n >>= 1
    return result


def expm_taylor(A, terms=20):
    # exp(A) ≈ sum_{k=0}^{terms-1} A^k / k!
    from math import factorial
    if not _is_square(A):
        raise ValueError("Matrix exponential requires a square matrix.")
    n = len(A)
    result = identity(n)
    Ak = identity(n)
    for k in range(1, terms):
        Ak = matrix_multiply(Ak, A)
        result = matrix_add(result, scalar_multiply(1.0 / factorial(k), Ak))
    return result


def rotation_x(theta):
    import math
    c, s = math.cos(theta), math.sin(theta)
    return [[1, 0, 0], [0, c, -s], [0, s, c]]


def rotation_y(theta):
    import math
    c, s = math.cos(theta), math.sin(theta)
    return [[c, 0, s], [0, 1, 0], [-s, 0, c]]


def rotation_z(theta):
    import math
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


def euler_zyx(roll, pitch, yaw):
    # Z (yaw) then Y (pitch) then X (roll)
    Rz = rotation_z(yaw)
    Ry = rotation_y(pitch)
    Rx = rotation_x(roll)
    return matrix_multiply(matrix_multiply(Rz, Ry), Rx)

# ---- GUI (Tkinter) ----
import tkinter as tk
from tkinter import ttk, messagebox


class MatrixGUI:
    """GUI aligned with the requested UX flow (input → operations → output)."""

    def __init__(self, root):
        self.root = root
        root.title("Matrix Lab")
        root.geometry("960x720")

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.container = ttk.Frame(root, padding=12)
        self.container.grid(row=0, column=0, sticky="nsew")
        for i in range(3):
            self.container.rowconfigure(i, weight=0)
        self.container.rowconfigure(2, weight=1)
        self.container.columnconfigure(0, weight=1)

        self._build_input_section()
        self._build_operation_section()
        self._build_output_section()

        self.a_entries = []
        self.b_entries = []
        self.operations_enabled = False
        self._configure_states()

    # ------------------------------------------------------------------ UI BUILDERS
    def _build_input_section(self):
        input_frame = ttk.LabelFrame(self.container, text="A) ورودی ماتریس")
        input_frame.grid(row=0, column=0, sticky="nsew")
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)

        # Matrix A controls
        a_frame = ttk.Frame(input_frame)
        a_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        a_frame.columnconfigure(0, weight=1)

        ttk.Label(a_frame, text="سطرها (n)").grid(row=0, column=0, sticky="w")
        ttk.Label(a_frame, text="ستون‌ها (m)").grid(row=0, column=2, sticky="w")
        self.a_rows_var = tk.StringVar(value="3")
        self.a_cols_var = tk.StringVar(value="3")
        ttk.Entry(a_frame, width=5, textvariable=self.a_rows_var).grid(row=0, column=1, padx=4)
        ttk.Entry(a_frame, width=5, textvariable=self.a_cols_var).grid(row=0, column=3, padx=4)
        ttk.Button(a_frame, text="ساخت ماتریس A", command=self.build_a).grid(row=0, column=4, padx=6)

        self.a_grid_frame = ttk.Frame(a_frame, relief="groove", padding=6)
        self.a_grid_frame.grid(row=1, column=0, columnspan=5, pady=6, sticky="nsew")
        a_frame.rowconfigure(1, weight=1)

        # Matrix B controls (only when needed)
        b_frame = ttk.Frame(input_frame)
        b_frame.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        b_frame.columnconfigure(0, weight=1)

        ttk.Label(b_frame, text="سطرهای B").grid(row=0, column=0, sticky="w")
        ttk.Label(b_frame, text="ستون‌های B").grid(row=0, column=2, sticky="w")
        self.b_rows_var = tk.StringVar(value="3")
        self.b_cols_var = tk.StringVar(value="3")
        ttk.Entry(b_frame, width=5, textvariable=self.b_rows_var).grid(row=0, column=1, padx=4)
        ttk.Entry(b_frame, width=5, textvariable=self.b_cols_var).grid(row=0, column=3, padx=4)
        ttk.Button(b_frame, text="ساخت ماتریس B", command=self.build_b).grid(row=0, column=4, padx=6)

        self.b_grid_frame = ttk.Frame(b_frame, relief="groove", padding=6)
        self.b_grid_frame.grid(row=1, column=0, columnspan=5, pady=6, sticky="nsew")
        b_frame.rowconfigure(1, weight=1)

    def _build_operation_section(self):
        ops_frame = ttk.LabelFrame(self.container, text="B) انتخاب عملیات")
        ops_frame.grid(row=1, column=0, sticky="ew", pady=(8, 8))
        ops_frame.columnconfigure(1, weight=1)

        ttk.Label(ops_frame, text="عملیات").grid(row=0, column=0, padx=4, pady=4, sticky="w")
        self.operation_var = tk.StringVar()
        self.operations = [
            "جمع A+B",
            "تفریق A−B",
            "ضرب ماتریسی A×B",
            "ضرب اسکالر α×A",
            "ترانهاده A^T",
            "مزدوج مختلط Conjugate(A)",
            "رد Trace(A)",
            "دترمینان det(A) [LU]",
            "معکوس Gauss-Jordan",
            "رتبه Rank(A)",
            "LU تجزیه",
            "QR تجزیه",
            "مقدار ویژه غالب (Power)",
            "مقادیر ویژه (QR)",
            "توان A^n",
            "exp(A) سری تیلور",
            "چک Hermitian",
            "چک Orthogonal",
            "چک Unitary",
            "بالامثلثی کردن",
            "ساخت دیاگونال از پارامتر",
            "چرخش حول X (deg)",
            "چرخش حول Y (deg)",
            "چرخش حول Z (deg)",
            "اویلر ZYX (deg: roll,pitch,yaw)",
            "فقط نمایش A",
        ]
        self.operation_combo = ttk.Combobox(
            ops_frame,
            values=self.operations,
            textvariable=self.operation_var,
            width=36,
            state="disabled",
        )
        self.operation_combo.grid(row=0, column=1, padx=4, pady=4, sticky="ew")
        self.operation_combo.bind("<<ComboboxSelected>>", lambda _: self._update_operation_state())

        ttk.Label(ops_frame, text="Param / توضیح").grid(row=0, column=2, padx=4, pady=4)
        self.param_var = tk.StringVar()
        self.param_entry = ttk.Entry(ops_frame, width=28, textvariable=self.param_var, state="disabled")
        self.param_entry.grid(row=0, column=3, padx=4, pady=4)

        self.compute_btn = ttk.Button(ops_frame, text="محاسبه", command=self.on_run_operation, state="disabled")
        self.compute_btn.grid(row=0, column=4, padx=8, pady=4)

        # Secondary actions
        actions = ttk.Frame(ops_frame)
        actions.grid(row=1, column=0, columnspan=5, sticky="ew", pady=(4, 0))
        actions.columnconfigure(0, weight=1)
        actions.columnconfigure(1, weight=1)
        actions.columnconfigure(2, weight=1)
        actions.columnconfigure(3, weight=1)

        self.save_btn = ttk.Button(actions, text="ذخیره ماتریس", command=self.save_matrix, state="disabled")
        self.save_btn.grid(row=0, column=0, padx=4, pady=2, sticky="ew")
        self.copy_btn = ttk.Button(actions, text="کپی خروجی", command=self.copy_output, state="disabled")
        self.copy_btn.grid(row=0, column=1, padx=4, pady=2, sticky="ew")
        self.reset_btn = ttk.Button(actions, text="پاک کردن صفحه", command=self.reset_all)
        self.reset_btn.grid(row=0, column=2, padx=4, pady=2, sticky="ew")
        self.new_op_btn = ttk.Button(actions, text="شروع عملیات جدید", command=self.clear_operation, state="disabled")
        self.new_op_btn.grid(row=0, column=3, padx=4, pady=2, sticky="ew")

    def _build_output_section(self):
        out_frame = ttk.LabelFrame(self.container, text="C) نمایش نتیجه")
        out_frame.grid(row=2, column=0, sticky="nsew")
        out_frame.columnconfigure(0, weight=1)
        out_frame.rowconfigure(0, weight=1)

        self.output = tk.Text(out_frame, height=16, wrap="word", font=("Consolas", 11))
        self.output.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(out_frame, orient="vertical", command=self.output.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.output.configure(yscrollcommand=scrollbar.set)

    # ------------------------------------------------------------------ STATE MGMT
    def _configure_states(self):
        self._set_operations_enabled(False)
        self._set_secondary_actions(False)

    def _set_operations_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self.operation_combo.configure(state=state)
        if enabled:
            self.param_entry.configure(state="disabled")
        else:
            self.param_entry.configure(state="disabled")
        self.compute_btn.configure(state=state)
        self.operations_enabled = enabled
        if enabled:
            self._update_operation_state()

    def _set_secondary_actions(self, enabled):
        state = "normal" if enabled else "disabled"
        self.save_btn.configure(state=state)
        self.copy_btn.configure(state=state)
        self.new_op_btn.configure(state=state)

    # ------------------------------------------------------------------ INPUT BUILD
    def _parse_size(self, rows_var, cols_var):
        try:
            n = int(rows_var.get())
            m = int(cols_var.get())
            if n <= 0 or m <= 0:
                raise ValueError
            return n, m
        except Exception:
            raise ValueError("Rows and columns must be positive integers.")

    def _build_grid(self, parent, rows, cols, storage_attr):
        for child in parent.winfo_children():
            child.destroy()
        grid = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = ttk.Entry(parent, width=6)
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")
                entry.bind("<KeyRelease>", lambda _event: self._validate_and_toggle())
                row_entries.append(entry)
            grid.append(row_entries)
        setattr(self, storage_attr, grid)
        self._validate_and_toggle()

    def build_a(self):
        try:
            n, m = self._parse_size(self.a_rows_var, self.a_cols_var)
            self._build_grid(self.a_grid_frame, n, m, "a_entries")
            self.b_rows_var.set(str(m))
            self._write_status("ماتریس A ساخته شد. مقادیر را وارد کنید.")
        except Exception as exc:
            messagebox.showerror("خطا", str(exc))

    def build_b(self):
        try:
            n, m = self._parse_size(self.b_rows_var, self.b_cols_var)
            self._build_grid(self.b_grid_frame, n, m, "b_entries")
            self._write_status("ماتریس B ساخته شد (برای ضرب یا جمع/تفریق).")
        except Exception as exc:
            messagebox.showerror("خطا", str(exc))

    def _entries_complete(self, grid):
        if not grid:
            return False
        for row in grid:
            for entry in row:
                txt = entry.get().strip()
                if txt == "":
                    return False
                try:
                    float(txt)
                except ValueError:
                    return False
        return True

    def _validate_and_toggle(self):
        if self._entries_complete(self.a_entries):
            self._set_operations_enabled(True)
        else:
            self._set_operations_enabled(False)

    def _read_matrix(self, entries):
        if not entries:
            raise ValueError("ابتدا ماتریس را بسازید.")
        if not self._entries_complete(entries):
            raise ValueError("تمام خانه‌های ماتریس باید مقدار عددی داشته باشند.")
        matrix = []
        for row in entries:
            matrix.append([float(entry.get()) for entry in row])
        return matrix

    # ------------------------------------------------------------------ ACTIONS
    def clear_operation(self):
        self.operation_var.set("")
        self.param_var.set("")
        self._write_status("عملیات ریست شد.")
        self._set_secondary_actions(False)

    def reset_all(self):
        self.a_rows_var.set("3")
        self.a_cols_var.set("3")
        self.b_rows_var.set("3")
        self.b_cols_var.set("3")
        for frame in (self.a_grid_frame, self.b_grid_frame):
            for child in frame.winfo_children():
                child.destroy()
        self.a_entries = []
        self.b_entries = []
        self.operation_var.set("")
        self.param_var.set("")
        self.output.delete("1.0", tk.END)
        self._configure_states()
        self._write_status("برنامه ریست شد. ابعاد جدید را انتخاب کنید.")

    def save_matrix(self):
        try:
            data = self.output.get("1.0", tk.END).strip()
            if not data:
                raise ValueError("ابتدا نتیجه‌ای داشته باشید.")
            with open("matrix_output.txt", "w", encoding="utf-8") as fh:
                fh.write(data)
            self._write_status("نتیجه در فایل matrix_output.txt ذخیره شد.")
        except Exception as exc:
            messagebox.showerror("خطا", str(exc))

    def copy_output(self):
        data = self.output.get("1.0", tk.END).strip()
        if not data:
            messagebox.showwarning(" هشدار", "چیزی برای کپی وجود ندارد.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(data)
        self._write_status("نتیجه در کلیپ‌بورد کپی شد.")

    def _write_output(self, text):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)
        self._set_secondary_actions(True)

    def _write_status(self, message):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, message)

    # ------------------------------------------------------------------ OPERATIONS
    def _parse_param_list(self, text):
        if not text.strip():
            return []
        parts = [p.strip() for p in text.replace("،", ",").split(",")]
        values = []
        for part in parts:
            if part:
                values.append(float(part))
        return values

    def _update_operation_state(self):
        op = self.operation_var.get()
        needs_param = op in {"ضرب اسکالر α×A", "توان A^n", "exp(A) سری تیلور",
                             "ساخت دیاگونال از پارامتر", "چرخش حول X (deg)",
                             "چرخش حول Y (deg)", "چرخش حول Z (deg)",
                             "اویلر ZYX (deg: roll,pitch,yaw)"}
        if self.operations_enabled and needs_param:
            self.param_entry.configure(state="normal")
        else:
            self.param_entry.configure(state="disabled")

    def on_run_operation(self):
        try:
            if not self.operations_enabled:
                raise ValueError("ابتدا ماتریس را بسازید و داده‌ها را کامل کنید.")
            op = (self.operation_var.get() or "").strip()
            if not op:
                raise ValueError("یک عملیات انتخاب کنید.")
            A = self._read_matrix(self.a_entries)
            result_text = ""

            if op == "فقط نمایش A":
                result_text = matrix_to_string(A)
            elif op == "جمع A+B":
                B = self._read_matrix(self.b_entries)
                result_text = matrix_to_string(matrix_add(A, B))
            elif op == "تفریق A−B":
                B = self._read_matrix(self.b_entries)
                result_text = matrix_to_string(matrix_sub(A, B))
            elif op == "ضرب ماتریسی A×B":
                B = self._read_matrix(self.b_entries)
                result_text = matrix_to_string(matrix_multiply(A, B))
            elif op == "ضرب اسکالر α×A":
                params = self._parse_param_list(self.param_var.get())
                if len(params) != 1:
                    raise ValueError("پارامتر α را وارد کنید.")
                result_text = matrix_to_string(scalar_multiply(params[0], A))
            elif op == "ترانهاده A^T":
                result_text = matrix_to_string(_transpose(A))
            elif op == "مزدوج مختلط Conjugate(A)":
                result_text = matrix_to_string(conjugate(A))
            elif op == "رد Trace(A)":
                result_text = f"Trace(A) = {trace(A)}"
            elif op == "دترمینان det(A) [LU]":
                result_text = f"det(A) ≈ {det_lu(A)}"
            elif op == "معکوس Gauss-Jordan":
                result_text = matrix_to_string(gauss_jordan_inverse(A))
            elif op == "رتبه Rank(A)":
                result_text = f"Rank(A) = {rank(A)}"
            elif op == "LU تجزیه":
                P, L, U, _ = lu_decomposition(A)
                result_text = f"P:\n{matrix_to_string(P)}\n\nL:\n{matrix_to_string(L)}\n\nU:\n{matrix_to_string(U)}"
            elif op == "QR تجزیه":
                Q, R = qr_decomposition(A)
                result_text = f"Q:\n{matrix_to_string(Q)}\n\nR:\n{matrix_to_string(R)}"
            elif op == "مقدار ویژه غالب (Power)":
                eig, vec = power_method(A)
                result_text = f"λ_max ≈ {eig}\nvector:\n{matrix_to_string([[v] for v in vec])}"
            elif op == "مقادیر ویژه (QR)":
                values = qr_eigenvalues(A)
                result_text = "Eigenvalues (QR):\n" + "\n".join(str(v) for v in values)
            elif op == "توان A^n":
                params = self._parse_param_list(self.param_var.get())
                if len(params) != 1 or int(params[0]) != params[0]:
                    raise ValueError("n باید عدد صحیح باشد.")
                result_text = matrix_to_string(matrix_power(A, int(params[0])))
            elif op == "exp(A) سری تیلور":
                params = self._parse_param_list(self.param_var.get())
                terms = int(params[0]) if params else 20
                result_text = matrix_to_string(expm_taylor(A, terms=terms))
            elif op == "چک Hermitian":
                result_text = "Hermitian" if is_hermitian(A) else "غیر Hermitian"
            elif op == "چک Orthogonal":
                result_text = "Orthogonal" if is_orthogonal(A) else "غیر Orthogonal"
            elif op == "چک Unitary":
                result_text = "Unitary" if is_unitary(A) else "غیر Unitary"
            elif op == "بالامثلثی کردن":
                result_text = matrix_to_string(upper_triangularize(A))
            elif op == "ساخت دیاگونال از پارامتر":
                diag = self._parse_param_list(self.param_var.get())
                if not diag:
                    raise ValueError("لیست درایه‌های قطر را وارد کنید.")
                result_text = matrix_to_string(diagonal_matrix(diag))
            elif op in ("چرخش حول X (deg)", "چرخش حول Y (deg)", "چرخش حول Z (deg)"):
                import math
                params = self._parse_param_list(self.param_var.get())
                if len(params) != 1:
                    raise ValueError("زاویه (درجه) را وارد کنید.")
                angle = math.radians(params[0])
                if op.endswith("X (deg)"):
                    result_text = matrix_to_string(rotation_x(angle))
                elif op.endswith("Y (deg)"):
                    result_text = matrix_to_string(rotation_y(angle))
                else:
                    result_text = matrix_to_string(rotation_z(angle))
            elif op == "اویلر ZYX (deg: roll,pitch,yaw)":
                import math
                params = self._parse_param_list(self.param_var.get())
                if len(params) != 3:
                    raise ValueError("roll,pitch,yaw (درجه) را وارد کنید.")
                roll, pitch, yaw = [math.radians(v) for v in params]
                result_text = matrix_to_string(euler_zyx(roll, pitch, yaw))
            else:
                raise ValueError("عملیات انتخاب شده پشتیبانی نمی‌شود.")

            self._write_output(result_text)
        except Exception as exc:
            messagebox.showerror("خطا", str(exc))


if __name__ == "__main__":
    app = tk.Tk()
    MatrixGUI(app)
    app.mainloop()
