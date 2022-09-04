# There are multiple interesting ways to reverse a string in python


# 1st Approach :- Using a loop
text = "Python"
reversed_text = ""

for i in range(1,len(text)+1):
    reversed_text +=text[-i]
print(reversed_text)


# 2nd Approach :- using join
text = "Python"
reversed_text = "".join(reversed(text))
print(reversed_text)

# 3rd Approach :- using string slicing

text = "Python"
reversed_text = text[::-1]
print(reversed_text)
