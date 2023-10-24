import datetime # importing time and date to be used with each instance

# Created a class to for making a available shopping items to test the Cart class 
class Item():
    def __init__(self,name,price,descript,e,time): 
        self.name = name
        self.price = price
        self.descript = descript
        self.e = e
        self.time = time

# Creating the first instance        
e = 1
list_item = []
name = "Basketball"
price = 15.99
descrip = "Special Edition"
time = datetime.datetime.now()                               # used for time stamp
list_item.append(Item(name,price,descrip,e,time))
e += 1                                                       # Used to show the index of the items in the list

# Creating the 2nd instantance
name = "Baseball"
price = 5.99
descrip = "Regulation Size"
time = datetime.datetime.now()
list_item.append(Item(name,price,descrip,e,time))
e +=1

# Creating the 3rd instantance
name = "Football"
price = 8.99
descrip = "Regulation Size"
time = datetime.datetime.now()
list_item.append(Item(name,price,descrip,e,time))
e +=1

# Creating the 4th instantance
name = "Basketball"
price = 9.99
descrip = "Youth"
time = datetime.datetime.now()
list_item.append(Item(name,price,descrip,e,time))
e +=1

# Creating the 5th instantance
name = "Hockey Stick"
price = 12.53
descrip = "Youth"
time = datetime.datetime.now()
list_item.append(Item(name,price,descrip,e,time))

#for x in list_item:
    #print(x.name,x.price,x.descript)