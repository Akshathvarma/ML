def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        return "Error: Matrices cannot be multiplied"
    
    result = [[0] * len(B[0]) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

rows_A = int(input("Enter rows of matrix A: "))
cols_A = int(input("Enter column2s of matrix A: "))
A = []
for i in range(rows_A):
    row = input(f"Enter row {i+1} of matrix A: ")
    row_elements = list(map(int, row.split()))
    A.append(row_elements)


rows_B = int(input("Enter rows of matrix B: "))
cols_B = int(input("Enter columns of matrix B: "))
B = []
for i in range(rows_B):
    row = input(f"Enter row {i+1} of matrix B: ")
    row_elements = list(map(int, row.split()))
    B.append(row_elements)


result = multiply_matrices(A, B)

if isinstance(result, str):
    print(result)
else:
    print("Product of matrices A and B is:")
    for row in result:
        print(row)
