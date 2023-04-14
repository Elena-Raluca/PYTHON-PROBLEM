  
# Function for printing the matrix 
def print_matrix(n,matrix1):
  for i in range(n): 
     for j in range(n): 
         print(matrix1[i][j], end = " ") 
     print() 



def dimension_matrix(n,matrix1): #the dimension of a square matrix is nxn so we are calculating and returning the product
    w=n*n
    return w



def add_matrices(n,matrix1,matrix2,result): #the addition here actually means the concatenation of the strings that are at the same positions in the two matrix
 for i in range(n): 
  for j in range(n):
   result[i][j] = matrix1[i][j]+matrix2[i][j]
 print("The Sum of Above two Matrices is : ")
 print_matrix(n,result)


def string_from_matrix(matrix1,k,l): #we are priting the string from the row k and column l
 print(matrix1[k][l])
 
def search_string(matrix1,x,n): #we are searching a given string x in the whole matrix
 for i in range(n):
  for j in range(n):
   if x==matrix1[i][j]:
    print("The string is found at position i= ",i, "and j=" ,j) #we print all the positions where we find the given string



def multiply_matrices(n,matrix1,matrix2,result):
    # iterate through rows of matrix1
 for i in range(len(matrix1)):
   # iterate through columns of matrix2
   for j in range(len(matrix2[0])):
       # iterate through rows of matrix2
       for k in range(0,len(matrix2),+1):
           #result[i][j] += matrix1[i][k] * matrix2[k][j]
           x=matrix2[k][j]
           x1=matrix2[k][j]
           y=matrix1[i][k]
           for w in range(0,len(x),+1):
               z=ord(x[w])-ord('a')
               x1.replace(x[w],str(z))
           for h in range(0,int(x1),+1):
               y=y+matrix1[i][k]
               result[i][j]+=y
            
           

 for r in result:
   print(r)

def matrix_comparison(matrix1,matrix2,n): #we compare the strings that are at the same positions in the two matrix
 aux=0
 for i in range(n):
  for j in range(n):
      if matrix1[i][j]<matrix2[i][j] and matrix1[i][j]!=matrix2[i][j]:
         print("matrix1<matrix2")
         aux=1
         break
      if matrix1[i][j]>matrix2[i][j] and matrix1[i][j]!=matrix2[i][j]:
           print("matrix1>matrix2")
           aux==1
           break
  if aux==1:
      break
  if aux==0:
      print("matrix1=matrix2")
