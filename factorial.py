## Write a program to Find Factorial of Number
## Iterative Approach

##Method Definition
def factorial(n):
    result  = 1
    if n > 1:
        for i in range(1,n+1):
            result = result * i
        return result
    else:
        return -1


## Driver Code
n = 5
result = factorial(n)
print("Factorial using an Iterative Approach is : ",result)




## Recursive Approach

##Method Definition
def Recursivefactorial(n):
    result = 1
    if n==0 or n==1:
        return 1
    elif n > 1:
        result = n * factorial(n-1)
        return result
    else: 
        return -1

## Driver Code
n = 5
result = factorial(n)
print("Factorial using an Recursive Approach is : ",result)  