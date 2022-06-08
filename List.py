#List stores multiple data
#List stores diffent data types unlike arrays
#which stores one data type at a time
#List stores data values in [] and values separated by a comma(,)
#List are mutable - can be changed
countries = ["Kenya","Libya","South Africa","Egypt","Nigeria"
             ,"USA","Canada","Mexico","Argentina","Brazil",
             "France","Norway","Germany","Spain","England",
             "China","Japan","Singapore","UAE","Qatar"]
print(countries)
print(type(countries))
print(len(countries))
print(countries[0])
print(countries[6:10])
print(countries[-19:6])

#To add a value to a list we use insert method 
#Insert method need spefic location of the value 
countries.insert(1,"Ethiopia")
countries.insert(6,"Cuba")
countries.insert(12,"Switzerland")
countries.insert(17,"India")
print(countries)

#We can remove data values in a list using
#pop method, remove method, delete method
#pop method - remove the last value of the list
countries.pop()
#Remove method , you aught to specify which value you are removing
countries.remove("India")
#Delete method uses index number to remove values from a list
del(countries[0])

#Sort method filters the list alphabetically(string)
#for integers it filters in an ascending order
countries.sort()
print(countries)



