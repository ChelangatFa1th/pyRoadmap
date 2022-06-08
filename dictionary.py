#Dictionaries
#Dictionary stores data value in form of key and value
#with dictionaries are used to store data values in Key:value pairs.
#A dictionary is a collection that is ordered, changeable and
#does not allow duplicates.
#They  are written in curly brackets and have keys and values
#We use colon (:)  to separate value from key
from re import X


mydict={
    "University of Helsinki":"Geomatics and Land mapping",
    "Masacheusates Institute of Technology":"Computer Science",
    "University of Cambridge":"Urban planning",
    "Stanford University":"Robotics",
    "Year":2000,
    "Female":True,
    "Male":False,
    "School fee":2334555.7890857823
}
#Extending the dictionary using update method
mydict.update({"Course":"Machine Learning"})
#Replacing the value in a dictionary by specifying the key
mydict["Year"]=2101
print(mydict)
#Checking the data types
print(type(mydict))
#Accessing the value in a dictionary using a key
x = mydict["University of Helsinki"]
print(x)
#Removing items in a dictionary using pop() method and 
#specifying the key
mydict.pop("School fee")
#Popitem()removes the last item in a dictionary
mydict.popitem()
#delete method we specify the key of the item
#using[] to call the key
del mydict["Male"]
print(mydict)