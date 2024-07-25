#Sets are used to store multiple items in a single variable.
#Set items are unchangeable, but you can remove items and add new items.
#sets are unordered so the items will be displayed in any sequence.
set1={"A","B","C","D"}
print(set1)

#you can determine the number of items in the lists using len() function
print(len(set1))

#how to join two sets (actually there are many ways to join sets one of which is...)
set2={"1","2","3"}
set3=set1|set2
print(set3)

#to add new items in sets yo need to use add() method
set1.add("D")
print(set1)

#to remove the items you can use remove() or dsicard() method
set1.remove("A")
print(set1)

#to delete the set completely del keyword is used
set4={"a","b","c"}
del set4
print(set4)#this will cause an error since "set4" no longer exists.