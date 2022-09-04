x = str(5)
# y = int(3)
# z = float(5)
# print(x)
# print(y)
# print(z)


# name = "Sam"
# letters = "PTJB"

# for letter in letters:
#     print(letter + name[1:])


# def hello():
#     name = input("Enter the name:")
#     print("Hello " + name)

# hello()




# for number in numbers:
#     if number%2==0:
#         print(number, "is Even")
#     else:
#         print(number, "is Odd")


# for number in numbers:
#     if number == 0:
#         print("Zero")
#     elif number > 0:
#         print("positive")
#     else:
#         print("Negative")  
# 
# 

# def even(x):
#     return x % 2 == 0
        

# print(even(4))      
    

# for row in range(1,11):
#     # print(row)
#     for col in range(1,row):
#         print('{:2}'.format(col),end='')
#     print()

# numbers = [1,2,3,-4,0,6,5,10,9]

# def Pos_Neg(x):
#     if number == 0:
#         print("zero")
#     else:
#         if number > 0:
#             print("Positive")
#         else:
#             print("Negative")


# for number in numbers:
    # print(number)
    # Pos_Neg(number)


# def hello():
#     name = input("Enter the name:")
#     print("Hello {} nice to meet you.".format(name))

# hello() 

#increment and decrement
# i=0
# i=i+1
# i=0
# i+=1
# i-=1
# print(i)

#can i do math on string 
# i='5'
# print(type(i)) # <class 'str'>
# print(i+5)  # TypeError: can only concatenate str (not "int") to str

#how to use while loop

# count = int(input("Enter the number : "))
# while count > 0:
#     print(count)
#     count -=1


numbers = [1,-5,2,-4,0,6,-10,3]
# print(type(numbers))

pos = []
neg = []
for number in numbers:
    if number > 0:
        pos.append(number)
    else:
        neg.append(number)

print(pos)
print(neg)

