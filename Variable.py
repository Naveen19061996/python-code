# Creating  a variable
x = 5
y = "John"
print(x)
print(y)

# overiding variable
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)


#valid Variable declaration
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Invalid Variable declaration
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Many values to multiple variable
x , y, z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z) 

# One values to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = [ "Orange","Banana","Cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)