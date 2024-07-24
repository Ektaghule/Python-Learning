#you can assign multiline string to a variable, using three quotes (you cand also use three single quotes)
x="""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code 
readability with the use of significant indentation."""
print(x)

#strings in Python are arrays of bytes (accessing random character of string is called string slicing)
a= "Ice cream"
print(a[5])

#you can use len() function to get the length of the string
print(len(a))

#you can concatenate two string
s1="Hello"
s2="World"
s3=s1+s2
print(s3)

#now if you want space in between you can add it like this....
s4=s1+" "+s2
print(s4)
