def transpose(A):
    rows = len(A)
    cols = len(A[0])
    B = [[0] * rows for k in range(cols)]      
    for i in range(rows):
        for j in range(cols):
            B[j][i] = A[i][j]    
    return B

rows_A = int(input("Enter rows of matrix A: "))
cols_A = int(input("Enter columns of matrix A: "))
A = []
for i in range(rows_A):
    row = input(f"Enter row {i+1} of matrix A: ")
    row_elements = list(map(int, row.split()))
    A.append(row_elements)

result = transpose(A)

print("Transpose of matrix A:")
for row in result:
    print(row)
