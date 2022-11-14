#1. Import the NUMPY package under the name np.
import numpy as np 

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
'''FIRST WAY'''
a= np.random.rand(2,3,5)

'''SECOND WAY'''
a2= np.random.randint(0,100, (2,3,5))
''' LAST WAY'''
a3 = np.random.random_sample((2,3,5))
#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))
#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

if a.size == b.size:
        print("They have the same size")
else:
        print("they have different sizes")

#8. Are you able to add a and b? Why or why not?

#print(a+b)
'''we can not add a and b , because they have different shapes a is (2,3,5) and b is (5,2,3)'''

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c= np.transpose(b,(1,2,0))
print(f" c is : \n {c}")

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d= a+c
print(d)
'''we can add a and b because both have the same shape now'''

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(f" a is:\n  {a} \n and d is \n {d}")

'''a is a random array and d is the same array added 1 '''

#12. Multiply a and c. Assign the result to e.

e= a*c
print(f" e is : \n {e}")
#13. Does e equal to a? Why or why not?

'''they are the same because we are multiplying the array with 1 numbers of the a array, that is by the property of identity, every number multiplied by 1 is the same'''


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max= np.max(d)
d_min= np.min(d)
d_mean= np.mean(d)

print(f"the maximun number of d array is {d_max}, the minimun is {d_min} and the mean is {d_mean}")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f= np.empty((2,3,5))


#16 #17

for x in range(d.shape[0]):
        for y in range(d.shape[1]):
                for z in range (d.shape[2]):
                        if d[x][y][z]>d_min and d[x][y][z]< d_mean:
                                f[x][y][z]= 25
                        elif d[x][y][z]> d_mean and d[x][y][z]< d_max:
                                f[x][y][z]= 75
                        elif d[x][y][z]== d_mean:
                                f[x][y][z]= 50
                        elif d[x][y][z]== d_min:
                                f[x][y][z]= 0
                        elif d[x][y][z] == d_max:
                                f[x][y][z]=100
print(f"d is \n {d}")
print(f"f is \n {f}")

#Bonus

'''First we create an empty  array of type string '''

s=np.empty((2,3,5), dtype= str)

'''Then, we  replace the values of the previous loop  with the new array of string "s", and finally we put the letters "A,B,C,A,E" for each  previous number  '''
for x in range(d.shape[0]):
        for y in range(d.shape[1]):
                for z in range (d.shape[2]):
                        if d[x][y][z]>d_min and d[x][y][z]< d_mean:
                                s[x][y][z]= "B"
                        elif d[x][y][z]> d_mean and d[x][y][z]< d_max:
                                s[x][y][z]= "D"
                        elif d[x][y][z]== d_mean:
                                s[x][y][z]= "C"
                        elif d[x][y][z]== d_min:
                                s[x][y][z]= "A"
                        elif d[x][y][z] == d_max:
                                s[x][y][z]="E"

print(s)