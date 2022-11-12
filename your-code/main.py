#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.randint(0, 100, (2, 3, 5))
#np.random.random_sample
#np.random.rand

#4. Print a.

print(a)
print("\n")

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print(b)
print("\n")

#7. Do a and b have the same size? How do you prove that in Python code?

print("Sí, tienen el mismo tamaño pero diferente estructura.")
print(a.size == b.size)
print("\n")

#8. Are you able to add a and b? Why or why not?

print("No se puede sumar ya que no tienen la misma estructura.")
# a + b
print("\n")

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b, (1,2,0))
print("\n")

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
print(d)
print("\n")
print("Ahora funciona ya que la estructura de 'a' y la de 'c' son iguales.\n")

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print("Array 'a': ")
print(a)
print("\n")
print("Array 'd': ")
print(d)
print("\n")
print("La diferencia entre la matriz 'd' menso la 'a' es igual a los valores de la matriz 'b' esto demuestra que 'd' es el producto de la suma de 'a' mas 'b'.")
print("\n")

#12. Multiply a and c. Assign the result to e.

e = a*c
print(e)
print(a)

#13. Does e equal to a? Why or why not?

print(np.all(e == a))
print("""'e' es igual a 'a', ya que 'e' es el resultado de la mutiplicacion de 'a' por la matriz 'c' la cual es la misma que 'b' la cual es 
una matriz de unos y la multiplicacion de un número por uno da el mismo número.\n""")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for array in  range(d.shape[0]):
        for columna in  range(d.shape[1]):
                for fila in range(d.shape[2]):
                        if (d[array, columna, fila] > d_min) & (d[array, columna, fila] < d_mean):
                                f[array, columna, fila] = 25
                        elif (d[array, columna, fila] > d_mean) & (d[array, columna, fila] < d_max):
                                f[array, columna, fila] = 75
                        elif d[array, columna, fila] == d_mean:
                                f[array, columna, fila] = 50
                        elif d[array, columna, fila] == d_min:
                                f[array, columna, fila] = 0
                        elif d[array, columna, fila] == d_max:
                                f[array, columna, fila] = 100
                        


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(f,"\n",d)
print("Si, tengo mi array 'f' esperado.\n")

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
letra = np.empty((2, 3, 5), dtype = str)

for array in  range(d.shape[0]):
        for columna in  range(d.shape[1]):
                for fila in range(d.shape[2]):
                        if (d[array, columna, fila] > d_min) & (d[array, columna, fila] < d_mean):
                                letra[array, columna, fila] = "B"
                        elif (d[array, columna, fila] > d_mean) & (d[array, columna, fila] < d_max):
                                letra[array, columna, fila] = "D"
                        elif d[array, columna, fila] == d_mean:
                                letra[array, columna, fila] = "C"
                        elif d[array, columna, fila] == d_min:
                                letra[array, columna, fila] = "A"
                        elif d[array, columna, fila] == d_max:
                                letra[array, columna, fila] = "E"
                                
print(letra)