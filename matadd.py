m=int(input("Enter matrix row size : "))
n=int(input("Enter matrix coloumn size : "))

A=[[0]*m for j in range(n)]
B=[[0]*m for j in range(n)]
result =[[0]*m for j in range(n)]

print("Enter the values for A Matrix")
for i in range(m):
    for j in range(n):
        A[i][j] = int(input())
       
       
# Printing the values of A Matrix
print (" Print A Matrix")
for a in A:
    print(a)
    
      
print("Enter the values for B Matrix")
for i in range (m):
    for j in range (n):
        B[i][j] = int(input())

# Printing the values of B Matrix
print (" Print B Matrix")
for b in B:
    print(b)
    

# Addition of A and B matrix

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
    

# Result of  Matrix
print ("Sum of Matrices is:")
for r in result:
        print(r)
    
