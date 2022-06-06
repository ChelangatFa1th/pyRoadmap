#Nested list is a list that contain many other lists
electronic =[["Microsoft","MacBook","Hp","Dell","Lenovo","Asus","Acer"],
              ["iPhone","Samsung","Oppo","Huawei","Tecno","RedMe","RealMe"],
              ["Samsung","Flamingo","LG","Vitron","Hifinit","Hisense","Sony"],
              ]

#electronic.pop()
#electronic.append("Huawei")
Vehicle = [["Sedan","Nissan"],
           ["TX","Subaru"],
           ["Benz","BMW","Lexus"]]
#electronic.insert(1,Vehicle[1])
#print(electronic)
Vehicle.insert(1,electronic[0][3])
print(Vehicle)


