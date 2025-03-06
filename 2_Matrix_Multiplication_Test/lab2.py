
import random 
import time
import numpy as np


def multiply_matrices(A, B):
    """
    Multiplies matrices A (of size m x n) and B (of size n x k).
    """

    # Check size
    if len(A) == 0 or len(B) == 0 or len(A[0]) != len(B):
        raise ValueError("Number of columns of A must equal number of rows of B")
    
    AB = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Multiply 
    for i in range(len(A)):               # A rows
        for j in range(len(B[0])):        # B columns
            for k in range(len(B)):       
                AB[i][j] += A[i][k] * B[k][j]
    return AB


def check_multiplied(A, B, C):
    """
    Multiplies square matrices A and B and checks if AB = C.
    """

    # Check size
    if len(A[0]) != len(A) or len(B[0]) != len(B) or len(C[0]) != len(C):
        raise ValueError("Square matrices only!!!")
    
    if len(C[0]) != len(B[0]) or len(C) != len(A):
        return "NO"
    
    # Multiply
    AB = multiply_matrices(A, B)

    # Check elementwise
    n = len(C)
    for i in range(n):
        for j in range(n):
            if AB[i][j] != C[i][j]:
                return "NO"
    return "YES"


def random_vector(n, p):
    """
    Randomly generates a vector (of size n) of elements from field ℤₚ, where p is a prime number.
    """
    return [random.randrange(p) for _ in range(n)]


def multiply_mod_p(A, x, p):
    """
    Calculates modular multiplication:
    Right multiplies matrix A (of size m x n) by vector x (of size n).
    The result is the product modulo p.
    """
    
    # Check size
    if len(x) != len(A[0]):
        return ValueError("Number of columns of A must equal vector size")
    
    n = len(A[0])
    Ax = [0 for _ in range(n)]

    # Modular multiplication
    for i in range(n):
        for k in range(n):
            Ax[i] += A[i][k] * x[k]
        Ax[i] = Ax[i] % p
    return Ax


def check_equality(A, B, C):
    """
    Checks if AB = C by right multiplying by random vector x of elements from field ℤₚ, 
    where p is a prime number.
    """

    # Check size
    if len(A[0]) != len(A) or len(B[0]) != len(B) or len(C[0]) != len(C):
        raise ValueError("Square matrices only!!!")
    if len(A[0]) != len(B):
        raise ValueError("Number of columns of A must equal number of rows of B")
    if len(C[0]) != len(B[0]):
        return "NO"
    
    # List of prime numbers to randomly choose from
    prime_set = [1621, 1801, 1879, 1907, 1987]

    p = random.choice(prime_set)
    n = len(A)

    x = random_vector(n, p)
    Bx = multiply_mod_p(B, x, p = p) 
    ABx = multiply_mod_p(A, Bx, p = p) 
    Cx = multiply_mod_p(C, x, p = p) 

    for i in range(n):
        if ABx[i] != Cx[i]:
            return "NO"
    return "YES"


def main():

    #Read data
    start_time = time.time()
    with open('in6.txt', 'rb') as f:
        lines = f.read().decode('utf-8').split('\n')
    end_time = time.time()
    print(f"Read time: {end_time - start_time} \n")
    
    amount_data = int(lines[0].strip())
    i = 1
    
    for k in range(amount_data):
        n = int(lines[i].strip())
        i += 1

        A = [list(map(int, lines[i + j].strip().split())) for j in range(n)]
        i += n
        B = [list(map(int, lines[i + j].strip().split())) for j in range(n)]
        i += n
        C = [list(map(int, lines[i + j].strip().split())) for j in range(n)]
        i += n

        #Matrices multiplication test
        start_time = time.time()
        outcome_mm = check_multiplied(A, B, C)
        end_time = time.time()
        time_mm = end_time - start_time

        #Random vector method test
        start_time = time.time()
        outcome_rv = check_equality(A, B, C)
        end_time = time.time()
        time_rv = end_time - start_time

        print(f"Test {k+1}:")
        print(f"Matrices multiplication: \n Result: {outcome_mm}\n Time: {time_mm}")
        print(f"Random vector method: \n Result: {outcome_rv}\n Time: {time_rv} \n")


if __name__ == "__main__":
    main()