
from numpy import array
from numpy.linalg import inv

# create a vector
v = array([1, 2, 3])
print(f"Vector v : \n {v}\n")

# multiply vectors
a = array([1, 2, 3])
print(f"a : \n {a} \n")

b = array([1, 2, 3])
print(f"b : \n {b} \n")

c = a * b
print(f"c = a * b : \n {c} \n")

# add matrices
A = array([[1, 2, 3], [4, 5, 6]])
print(f"Matrice A :  \n {A}\n")

B = array([[1, 2, 3], [4, 5, 6]])
print(f"Matrice B : \n {B}\n")

C = A + B
print(f"Matrice C = A + B : \n {C} \n")

# matrix dot product
A = array([[1, 2], [3, 4], [5, 6]])
print(f"Matrice A : \n {A}\n")

B = array([[1, 2], [3, 4]])
print(f"Matrice B : \n {B}\n")

C = A.dot(B)
print(f"Matrice Produit => C = A.dot(B) : \n {C} \n")


# transpose matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(f"Matrice A : \n {A}\n")

C = A.T
print(f"Matrice Transposee => A.T  : \n {C} \n")


# define matrix
A = array([[1.0, 2.0], [3.0, 4.0]])
print(f"Matrice A : \n {A}\n")
# invert matrix
B = inv(A)
print(f"Matrice Inverse  B = inv(A)  : \n {B} \n")
