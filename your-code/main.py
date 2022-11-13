#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.randint(0,100, (2,3,5))
# Las tres maneras para crear arrays aleatorias son: np.random.randint, np.random.rand y np.random.random_sample.


#4. Print a.
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))


#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
def check_size(a, b):
        if a.size == b.size:
                return "The arrays have the same size"
        else:
                return "The arrays doesn't have the same size"

print(check_size(a, b))

#8. Are you able to add a and b? Why or why not?
#No se pueden sumar, ya que no tienen la misma forma (suma = np.add(a, b) daría error)


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = b.transpose(1, 2, 0)
print("Esto es la array c")
print(c)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add(a, c)
print(d)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("Esto es la array a")
print(a)
print("Esto es la array d")
print(d)
#Cada valor de la array d es un número más grande que su correspondiente pareja de valor en la array a.

#12. Multiply a and c. Assign the result to e.
e = np.multiply(a, c)


#13. Does e equal to a? Why or why not?
print("Esto es la array e")
print(e)
print("Esto es la array a")
print(a)
print(np.array_equal(e, a))
# Son iguales ya que la array e ha sido el resultado de multiplicar la array a por la array c (esta array c estaba formada 
# por unos, con lo que al multiplicarla ha quedado igual.)



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty((2, 3, 5))
print("Esto es la array f")
print(f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
# Lo he hecho yo solo y me siento un hacker de la ostia, creo que está bien:
for columnas in range(d.shape[0]):
    for filas in range(d.shape[1]):
        for valores in range(d.shape[2]):
                if ((d[columnas][filas][valores] > d_min) & (d[columnas][filas][valores] < d_mean)).any():
                        f[columnas][filas][valores] = 25
                elif ((d[columnas][filas][valores] > d_mean) & (d[columnas][filas][valores] < d_max)).any(): 
                        f[columnas][filas][valores] = 75
                elif (d[columnas][filas][valores] == d_mean).any():
                        f[columnas][filas][valores] = 50
                elif (d[columnas][filas][valores] == d_min).any():
                        f[columnas][filas][valores] = 0
                elif (d[columnas][filas][valores] == d_max).any():
                        f[columnas][filas][valores] = 100


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
print("Esto es la array f")
print(f)


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
f1 = f.astype("str")
for columnas in range(d.shape[0]):
    for filas in range(d.shape[1]):
        for valores in range(d.shape[2]):
                if ((d[columnas][filas][valores] > d_min) & (d[columnas][filas][valores] < d_mean)).any():
                        f1[columnas][filas][valores] = "A"
                elif ((d[columnas][filas][valores] > d_mean) & (d[columnas][filas][valores] < d_max)).any(): 
                        f1[columnas][filas][valores] = "B"
                elif (d[columnas][filas][valores] == d_mean).any():
                        f1[columnas][filas][valores] = "C"
                elif (d[columnas][filas][valores] == d_min).any():
                        f1[columnas][filas][valores] = "D"
                elif (d[columnas][filas][valores] == d_max).any():
                        f1[columnas][filas][valores] = "E"

print("Esto es la array f1")
print(f1)