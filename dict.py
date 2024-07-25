#Dictionaries are used to store data values in key:value pairs.
d1={
    "name":"Ekta",
    "surname":"Ghule",
    "fav_color":"pink"
}
print(d1)

#values can be referred to by using the key name.
print(d1["fav_color"])

#you can determine the number of items in the dictionaries using len() function
print(len(d1))

#to change the values, you just need to refer it's key name
d1["fav_color"]="blue"
print(d1)

#you can simply add new items without any function or method
d2={
    "fav_animal":"dog",
    "fav_flower":"rose"
}
d2["fav_movie"]="jab we met"
print(d2)

#you can chnage the values using the update() method
d2.update({"fav_animal":"cat"})
print(d2)

#you cant remove the items using the pop() method
d2.pop("fav_movie")
print(d2)