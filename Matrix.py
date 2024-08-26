# Function to check whether a given matrix is upper triangular or not
def upper_tri(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            if m[i][j] != 0:
                return False
    return True

# Function to compute the summation of diagonal elements of a matrix
def sum_dia(m):
    n = len(m)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += m[i][i]
    return diagonal_sum

# Function to compute the transpose of a matrix
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# Function to add two matrices
def add_matrices(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

# Function to subtract two matrices
def subtract_matrices(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)
    return result

# Function to multiply two matrices
def multiply_matrices(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            sum = 0
            for k in range(len(m2)):
                sum += m1[i][k] * m2[k][j]
            row.append(sum)
        result.append(row)
    return result

# Function to find saddle point in a matrix
def saddle_point(m):
    l = len(m)
    n = len(m[0])
    
    for i in range(l):
        # Find the minimum value in row i
        min_val = m[i][0]
        min_index = 0
        for j in range(1, n):
            if m[i][j] < min_val:
                min_val = m[i][j]
                min_index = j
        
        # Check if min_val is also the maximum in column min_index
        is_saddle_point = True
        for k in range(l):
            if m[k][min_index] > min_val:
                is_saddle_point = False
                break
        
        if is_saddle_point:
            return (i, min_index)
    
    return None

# Test case:
m1 = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

m2 = [
    [4, 5, 6],
    [0, 7, 8],
    [0, 0, 9]
]

# a) Check if matrix1 is upper triangular
print("Matrix 1 is upper triangular:", upper_tri(m1))

# b) Compute the summation of diagonal elements of matrix1
print("Sum of diagonal elements in matrix 1:", sum_dia(m1))

# c) Compute the transpose of matrix1
print("Transpose of matrix 1:")
print(transpose(m1))

# d) Add, subtract, and multiply matrix1 and matrix2
print("Addition of matrix 1 and matrix 2:")
print(add_matrices(m1, m2))

print("Subtraction of matrix 1 and matrix 2:")
print(subtract_matrices(m1, m2))

print("Multiplication of matrix 1 and matrix 2:")
print(multiply_matrices(m1, m2))

# e) Find saddle point in matrix1
saddle = saddle_point(m1)
if saddle:
    print(f"Saddle point in matrix 1 at position: {saddle}")
else:
    print("No saddle point found in matrix 1")