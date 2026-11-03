import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Original array:", arr)

arrr = arr.copy()
arrr[arrr % 2 == 1] = -1

print("Modified array:", arrr)

arrrr = arr.copy()

z = arrrr.reshape(3,3)
print("The whole matrix: \n",z)

p = 0

for i in arrrr:
    p += i
    
print("The sum of whole array",p)