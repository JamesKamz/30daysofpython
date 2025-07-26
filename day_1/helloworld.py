# 1. La version de python
import sys
print(sys.version)

# 2. Les opérations sont 3 et 4 
print(3+4) # addition
print(3-4) # soustraction
print(3*4) # multiplication
print(3/4) # division
print(3**4) # exponentielle
print(3 % 4) # module
print(3//4) # division entière

# 3. Write strings on the python interactive shell. The strings are the following:
print('Koffi Jacques')
print('Amouzou')
print('Togo')
print('Je profite de 30 jours de python')

# 4. Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['abeneh', 'Python', 'Finland']))
print(type('Koffi Jacques'))
print(type('Amouzou'))
print(type('Togo'))


# Level 3 exercise
# Python data types
# Nombre : Integer, float, complex
a = 3 # integer
print(type(a))
b = 4.566 # float
print(type(b))
c = 4 +6j # complex
print(type(c))
# String : 
d = 'Amouzou' # string
print(type(d))
# Boolean :
e = True # boolean
print(type(e))
# List:
f = ['Aisha',3,7.6,True,False,['elephant']] #square brackets
print(type(f))
# Tuple:
g = ("red","green") #round brackets
print(type(g))
# Set :
h = {1,3,4,5} # set - curly brackets
print(type(h))
# Dictionary: 
i = {'goat':7,'dog':8,'elephant':9}
print(type(i))

#euclidian distance
# import math module
import math
print(math.dist([2,3],[10,8]))