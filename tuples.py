#tuples are also used to store multiple items in a single variable, it is the collection which is ordered and unchangeable. Assigning values to a tuple is called "packing".
tuple1=("red","blue","green","yellow")
print(tuple1)

#you can access the tuple items through index munbers
print(tuple1[3])

#you can also access the range of items from the tuple 
print(tuple1[0:3])
print(tuple1[-1])

#if you want to append(add) items in the tuples then you first need to conver tuple into list, add the item in list and then, convert the list back into tuple.
t2=("dog","cat","cow","goat")
l1=list(t2)
l1.append("sheep")
t2=tuple(l1)
print(t2)

#if you want to change the tuples then you first need to conver tuple into list, chnage the list and then, convert the list back into tuple.
t3=("rose","lily","sunlower","jasmine")
l2=list(t3)
l2[2]="tulip"
t3=tuple(l2)
print(t3)

#you can get the number of items in the tuple using len() function
print(len(t2))

#how to join two tuples
t4=t2+t3
print(t4)

#unpacking a tuple, extracting the values back into variables is calles "unpacking"
f=("orange","kiwi","apple","mango")
(o,k,a,m)=f
print(o)
print(k)
print(a)
print(m)