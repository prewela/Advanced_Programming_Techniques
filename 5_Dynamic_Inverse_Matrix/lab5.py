import numpy as np

def swap_rows(A, invA, row: int, row2: int):
    """
    Swaps row and row2 of matrix A and updates the inverse of A.
    """
    if row == row2:
        return A, invA
    A[row], A[row2] = A[row2], A[row]
    for k in range(len(A)):
        invA[k][row], invA[k][row2] = invA[k][row2], invA[k][row]
    return A, invA


def swap_columns(A, invA, col: int, col2: int):
    """
    Swaps col and col2 of matrix A and updates the inverse of A.
    """
    if col == col2:
        return A, invA
    for k in range(len(A)):
        A[k][col], A[k][col2] = A[k][col2], A[k][col]
    invA[col], invA[col2] = invA[col2], invA[col]
    return A, invA


def inverse_n(n, p):
    """
    Returns the inverse of number n in field ℤₚ using Fermat's little theorem.
    p: prime number
    """
    if n % p == 0:
        raise ValueError("The inverse of 0 doesn't exist!")
    return pow(n, p - 2, p)


def print_matrix(A):
    for row in A:
        print(" ".join([str(x) for x in row]))


def check_equality(A, B):
    """
    Checks whether matrices A and B are equal.
    """
    A_np = np.asarray(A)
    B_np = np.asarray(B)
    return np.array_equal(A_np, B_np)


def Dynamic_Inverse_Matrix(n, A, invA, row, col, p):
    """
    Swaps row and col with the last row and column of a square matrix A (over ℤₚ) of size n. 
    Deletes said row and col and calculates the inverse of the new matrix
    """
    A, invA = swap_rows(A, invA, row, row2 = n-1)
    A, invA = swap_columns(A, invA, col, col2 = n-1)
    A, invA = np.asarray(A), np.asarray(invA)

    bnn = int(invA[n-1, n-1])
    if bnn == 0:
        return "NO", None
    inv_bnn = inverse_n(bnn, p)
    B = invA[:n-1, :n-1]
    K = invA[:n-1, -1]
    W = invA[-1, :n-1]
    KW = np.asarray([[0]*(n-1) for i in range(n-1)])
    for i in range(n-1):
        for j in range(n-1):
            KW[i][j] = (K[i]*W[j]*inv_bnn) % p
    C = (B-KW) % p
    return "YES", C

    
def main():
    file_num = "6"

    with open(f"in{file_num}.txt", "rb") as f:
        lines = f.read().decode('utf-8').split('\n')

    with open(f"out{file_num}.txt", "r") as f:
        lines_out = f.readlines()
        lines_out = [x.strip() for x in lines_out]
        
    z = int(lines[0].split(" ")[0]) #number of sets
    p = int(lines[0].split(" ")[1])

    index = 1
    out_index = 0
    tests_passed = True

    for j in range(z):
        n = int(lines[index].split(" ")[0])
        r = int(lines[index].split(" ")[1])
        c = int(lines[index].split(" ")[2])
        A = [[] for i in range(n)]
        invA = [[0]*n for i in range(n)]
        index += 1
        for i in range(n):
            A[i] = list(map(int, lines[index].split()))
            invA[i] = list(map(int, lines[index + n].split()))
            index += 1
        index += n
        
        #Print output
        invertible, inv = Dynamic_Inverse_Matrix(n, A, invA, r, c, p)
        print(invertible)
        if invertible == "YES":
            print_matrix(inv)

        #Test
        if invertible != lines_out[out_index]:
            print(f"Test {j+1} failed!")
            tests_passed = False

        elif invertible == "YES":
            inv_out = []

            for i in range(n-1):
                row = list(map(int, lines_out[out_index + i + 1].strip().split()))
                inv_out.append(row)

            if not check_equality(inv, inv_out):
                print(f"Test {j+1} failed!")
                tests_passed = False
        
        if invertible == "YES":
            out_index += n
        else:
            out_index += 1

    if tests_passed:
        print("\nTests passed.\n")
    else:
        print("\nSome tests failed.\n")


if __name__ == "__main__":
    main()