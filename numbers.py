#there are 3 numeric type in python int, float, complex. (complex numbers are the numbers with "j" as the imaginary part)
x=19
y=57.4
z=7j
print("Int:",x)
print("Float:",y)
print("Complex:",z)

#you can convert these numbers from one type to other using int(), float() and complex() methods.
a=7
b=6.4
c=9j

print("Before converting:")
print(a)
print(b)
print(c)

#converting
p=float(a)
q=int(b)
r=complex(a)

print("After converting:")
print(p)
print(q)
print(r)

print(type(p))
print(type(q))
print(type(r))