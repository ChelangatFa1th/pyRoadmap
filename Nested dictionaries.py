#A nested dictionary is a dictionary contained in another dictionary
family={
    "father":{
        "Year": 1976,
        "name": "John"
    },
    "mother":{
        "Year": 1980,
        "name": "Julie"
    },
    "fborn":{
        "Year":2000,
        "name":"Dion"
    },
    "sborn":{
        "Year":2006,
        "name":"Celine"
    },
    "tborn":{
        "Year":2012,
        "name":"Wayne"
    }
}
print(family)
#Checking the data type
print(type(family))
#Adding an item to a dictionary
family.update({"xborn":{
    "Year": 2018,
    "name": "Ashye"
}})
#delete method
#removing items in a dictionary
del family["xborn"]
#popmethod()
family.popitem()
#popmethod(), delete an item but specifying the key
family.pop("fborn")
print(family)

child1 = {
    "name": "Jay",
    "year": 2000
}

child2 = {
    "name": "Kim",
    "year": 2002
}

child3 = {
    "name": "Vicky",
    "year": 2004
}

myfamily = {
    "child10": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)
Student1 ={
    "name": "Alphones",
}
Student2 ={
    "name":"Stacy",
}
Student3 ={
    "name":"Malika",
}
Student4 ={
    "name":"Jared"
}
students={
   1 : Student1, 
   2 : Student2,
   3 : Student3,
   4 : Student4
}
myfamily.update(students)
print(myfamily)