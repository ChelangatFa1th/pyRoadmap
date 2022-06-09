#Arrays stores multiple data in a single variable
from array import *

from numpy import array2string
my_array = [1, 2, 3, 4, 5]
an_array = [6, 7, 8, 9, 0]
print(my_array, an_array)
#extend() method combines two arrays
my_array.extend(an_array)
print(my_array)
#append() method 
array1 = ["Sedan","Benz","Ford","Lamborghini"]
array2 = ["KDA 123S","KDB 243D","KDD 100E","KDF 345K"]
#append() metod adds an item at the end of the array
array2.append(["KDG 234W"])
#insert() method adds a value to an array ,
#but the added value must be stated and the index location
array1.insert(2, "Bugatti")
#remove()method removes the stated value in array
array1.remove("Sedan")
#pop()method removes the last item in an array
array2.pop()
print(array2)
