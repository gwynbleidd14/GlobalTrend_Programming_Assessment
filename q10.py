'''
10. Write a Python function that takes a 2D list (matrix) and returns its transpose.
'''

def transpose(old_matrix, trans_matrix):
    for i in range(len(old_matrix)):
        for j in range(len(old_matrix[0])):
            trans_matrix[j][i] = old_matrix[i][j]    
    
    
n = int(input("No. of rows: "))
m = int(input("No. of columns: "))
a = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input("Enter elements: "))
b = [[0]*n for _ in range(m)]
print("\nEntered Matrix is:")
print(a)
transpose(a, b)
print("Transpose of entered matrix is:")
print(b)