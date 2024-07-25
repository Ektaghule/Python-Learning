 #there are 4 built-in data types in Python used to store collections of data, which are  List, Tuple, Sets, and Dictionary, all with different qualities and usage.
#lists are used to store multiple values in a single variable
items=["apple","orange","kiwi","mango"]
print(items)

#you can access the list items through index munbers
print(items[2])

#you can also access the range of items from the list 
print(items[0:3])
print(items[-1])

#you can append(add) new items in the list using append() method
items.append("pineapple")

#you can get the number of items in the lists using len() function
print(len(items))

#how to join two lists
list1=["red","green","yellow"]
list2=["mysql","c","c++","python"]
l3=list1+list2
print(l3)

#you can check if a perticular item is present in the list or not using 'in' operator
print("kiwi" in items)
print("watermelon" in items)