# Simple, clear examples of basic linear algebra concepts using NumPy
# Each small chunk shows one concept, a short plain-English comment, and a tiny example.

import numpy as np

# -------------------- VECTORS (small chunks) --------------------

def add(u, v):
    """Vector addition: elementwise u + v.

    Inputs:
      u, v - array-like (same length)
    Output:
      numpy array (u + v)
    """
    return np.array(u) + np.array(v)


def scalar_mul(a, v):
    """Multiply a vector by a scalar: a * v.

    Inputs:
      a - number
      v - array-like
    Output:
      numpy array (scaled vector)
    """
    return a * np.array(v)


def dot(u, v):
    """Dot product (inner product) of two vectors.

    Formula: sum(u_i * v_i)
    Returns a single scalar.
    """
    return np.dot(np.array(u), np.array(v))


def norm(v):
    """Euclidean length (L2 norm) of a vector.

    Formula: sqrt(sum(v_i^2)).
    """
    return np.linalg.norm(np.array(v))


def angle_deg(u, v):
    """Angle between vectors u and v, in degrees.

    Uses cosine formula: cos(theta) = (u·v)/(|u||v|).
    Clips numerical errors so the result is safe.
    """
    u, v = np.array(u, dtype=float), np.array(v, dtype=float)
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    if nu == 0 or nv == 0:
        return None  # undefined angle with zero vector
    cos_theta = np.dot(u, v) / (nu * nv)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    return np.degrees(np.arccos(cos_theta))


# -------------------- PROJECTION --------------------

def projection(u, v):
    """Project vector u onto vector v.

    Returns the vector component of u that points in the direction of v.
    Formula: proj_v(u) = (u·v / v·v) * v
    If v is the zero vector, returns a zero vector of the same shape.
    """
    u_a = np.array(u, dtype=float)
    v_a = np.array(v, dtype=float)
    denom = np.dot(v_a, v_a)
    if denom == 0:
        return np.zeros_like(v_a)
    return (np.dot(u_a, v_a) / denom) * v_a


# -------------------- MATRICES (small chunks) --------------------

def mat_mul(A, B):
    """Matrix multiplication A @ B (or vector/matrix accordingly)."""
    return np.dot(np.array(A), np.array(B))


def transpose(A):
    """Return transpose of matrix A."""
    return np.array(A).T


def determinant(A):
    """Determinant of a square matrix A (returns scalar)."""
    return float(np.linalg.det(np.array(A)))


def inverse(A):
    """Inverse of a square matrix A. Raises LinAlgError if singular."""
    return np.linalg.inv(np.array(A))


def rank(A):
    """Rank (number of independent rows/columns) of matrix A."""
    return np.linalg.matrix_rank(np.array(A))


def solve_linear_system(A, b):
    """Solve linear system A x = b for x using a direct solver.

    A should be square (n x n) and invertible for a unique solution.
    """
    return np.linalg.solve(np.array(A), np.array(b))


# -------------------- EIGEN / SVD (concepts) --------------------

def eigen_decomposition(A):
    """Return eigenvalues and eigenvectors of square matrix A."""
    return np.linalg.eig(np.array(A))


def svd_decomposition(A):
    """Return SVD (U, S, Vt) where A = U @ diag(S) @ Vt."""
    return np.linalg.svd(np.array(A), full_matrices=False)


# -------------------- ORTHONORMALIZATION --------------------

def gram_schmidt(vectors):
    """Simple Gram-Schmidt to make an orthonormal set from input vectors.

    Input: list/array of vectors (each same length).
    Output: array of orthonormal vectors (each row is a vector).
    """
    vs = [np.array(v, dtype=float) for v in vectors]
    orth = []
    for v in vs:
        w = v.copy()
        for u in orth:
            # remove component in direction u
            w -= np.dot(w, u) * u
        n = np.linalg.norm(w)
        if n > 1e-12:
            orth.append(w / n)
    if len(orth) == 0:
        return np.zeros((0, 0))
    return np.vstack(orth)


# -------------------- DEMONSTRATIONS (tiny, focused examples) --------------------
# Each block shows input, a short comment, and the printed result.
if __name__ == "__main__":
    print("--- VECTOR EXAMPLES ---")
    u = [1, 2, 3]
    v = [4, 0, -1]
    print("u + v ->", add(u, v))           # elementwise add
    print("2 * v ->", scalar_mul(2, v))    # scale vector
    print("dot(u, v) ->", dot(u, v))       # single number
    print("||u|| ->", norm(u))             # length of u
    print("angle(u, v) deg ->", angle_deg(u, v))
    print("proj_u_on_v ->", projection(u, v))

    print("\n--- MATRIX EXAMPLES ---")
    A = np.array([[2.0, 1.0], [1.0, 3.0]])
    B = np.array([[1.0, 2.0], [3.0, 4.0]])
    print("A @ B ->\n", mat_mul(A, B))
    print("A^T ->\n", transpose(A))
    print("det(A) ->", determinant(A))
    print("rank(B) ->", rank(B))
    print("solve A x = [1,1] ->", solve_linear_system(A, [1, 1]))

    print("\n--- EIGEN / SVD ---")
    vals, vecs = eigen_decomposition(A)
    print("eigenvalues(A) ->", vals)
    U, S, Vt = svd_decomposition(B)
    print("singular values of B ->", S)

    print("\n--- ORTHONORMAL BASIS (Gram-Schmidt) ---")
    basis = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    orthonormal = gram_schmidt(basis)
    print("orthonormal (rows):\n", np.round(orthonormal, 6))
    # Quick check: rows should be orthonormal -> dot product matrix approx I
    if orthonormal.size:
        print("Q @ Q.T ->\n", np.round(orthonormal @ orthonormal.T, 6))

    print("\n--- SMALL NOTES ---")
    print("angle_deg returns None if one vector is zero (angle undefined).")
