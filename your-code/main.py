#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.

print(np.__version__)
print(np.show_config())

Me aparece esto:#es normal lo de None al final??
1.21.5
blas_mkl_info:
    libraries = ['mkl_rt']
    library_dirs = ['C:/Users/egcmo/anaconda3\\Library\\lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['C:/Users/egcmo/anaconda3\\Library\\include']
blas_opt_info:
    libraries = ['mkl_rt']
    library_dirs = ['C:/Users/egcmo/anaconda3\\Library\\lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['C:/Users/egcmo/anaconda3\\Library\\include']
lapack_mkl_info:
    libraries = ['mkl_rt']
    library_dirs = ['C:/Users/egcmo/anaconda3\\Library\\lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['C:/Users/egcmo/anaconda3\\Library\\include']
lapack_opt_info:
    libraries = ['mkl_rt']
    library_dirs = ['C:/Users/egcmo/anaconda3\\Library\\lib']
    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
    include_dirs = ['C:/Users/egcmo/anaconda3\\Library\\include']
Supported SIMD extensions in this NumPy install:
    baseline = SSE,SSE2,SSE3
    found = SSSE3,SSE41,POPCNT,SSE42
    not found = AVX,F16C,FMA3,AVX2,AVX512F,AVX512CD,AVX512_SKX,AVX512_CLX,AVX512_CNL
None

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random_sample((2,3,5))

#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?
Yes, los dos tiene un size= 30
a.size==b.size


#8. Are you able to add a and b? Why or why not?

suma= np.add(a,b) No se puede porque tienen distintas estructuras: ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) 


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c=np.transpose(b,(1,2,0))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d= np.add(a,c)
porque tienen la misma estructura

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

a-d nos da todos los valores igual a -1 porque todos los valores de b=1


#12. Multiply a and c. Assign the result to e.

e=a*c

#13. Does e equal to a? Why or why not?

Si porque todos los valores de b=1


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_min=np.min(d)
d_max=np.max(d)
d_mean=np.mean(d)


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f=np.empty((2,3,5))


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
for x, list_d in enumerate(d):
    for y, sublist_d in enumerate(list_d):
        for z, value in enumerate(sublist_d):
            if value>d_min and value<d_mean:
                f[x,y,z]=25
            if value>d_mean and value<d_max:
                f[x,y,z]=75
            if value==d_mean:
                f[x,y,z]=50
            if value==d_min:
                f[x,y,z]=0
            if value==d_max:
                f[x,y,z]=100



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
""" #yes
#y con mi random a:
d=
array([[[1.51694161, 1.73680906, 1.06490521, 1.37152501, 1.60136346],
        [1.97657283, 1.91049219, 1.89574939, 1.72790536, 1.0158965 ],
        [1.049242  , 1.72435271, 1.93230938, 1.7930778 , 1.37358044]],

       [[1.90677194, 1.27768064, 1.32830616, 1.16602182, 1.12875318],
        [1.82819809, 1.08343501, 1.54295178, 1.60920894, 1.82294992],
        [1.82042206, 1.93402721, 1.67611187, 1.4869198 , 1.08776917]]])

f=
array([[[ 25.,  75.,  25.,  25.,  75.],
        [100.,  75.,  75.,  75.,   0.],
        [ 25.,  75.,  75.,  75.,  25.]],

       [[ 75.,  25.,  25.,  25.,  25.],
        [ 75.,  25.,  25.,  75.,  75.],
        [ 75.,  75.,  75.,  25.,  25.]]])

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
#no me deja convertir a string un float :(
for x, list_d in enumerate(d):
    for y, sublist_d in enumerate(list_d):
        for z, value in enumerate(sublist_d):
            if value>d_min and value<d_mean:
                f[x,y,z]="B"
            if value>d_mean and value<d_max:
                f[x,y,z]="D"
            if value==d_mean:
                f[x,y,z]="C"
            if value==d_min:
                f[x,y,z]="A"
            if value==d_max:
                f[x,y,z]="E"