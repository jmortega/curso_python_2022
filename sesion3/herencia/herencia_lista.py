class MyList(list):
    def min_and_max(self):
        return min(self),max(self)
    
myList = MyList()
myList.extend([100,200,300,400])
print(myList)
print(myList.min_and_max())
