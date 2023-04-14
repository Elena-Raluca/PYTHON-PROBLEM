from functions import print_matrix, dimension_matrix, add_matrices, string_from_matrix, search_string, matrix_comparison, multiply_matrices


# A basic code for square matrix input from user 
n = int(input("Enter the number of rows and of colums:"))
# Initialize matrix 
matrix1 = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(n):          # A for loop for row entries 
    a =[] 
    for j in range(n):      # A for loop for column entries 
         a.append(str(input())) 
    matrix1.append(a) 

# Initialize second matrix 
matrix2 = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(n):          # A for loop for row entries 
    a =[] 
    for j in range(n):      # A for loop for column entries 
         a.append(str(input())) 
    matrix2.append(a) 

 # Initialize result matrix with 0 everywhere
result=[[0 for i in range(n)] for i in range(n)]

def test1():
    print_matrix(n,matrix1)
    print()
    print_matrix(n,matrix2)
test1()

def test2():
    print(dimension_matrix(n,matrix1))
test2()

def test3():
 add_matrices(n,matrix1,matrix2,result)
test3()

def test4():
    string_from_matrix(matrix2,0,1)
test4()

def test5():
    search_string(matrix2,"bb",n)
test5()

#def test6():
#    multiply_matrices(n,matrix1,matrix2,result)
#test6()

def test7():
    matrix_comparison(matrix1,matrix2,n)
test7()
