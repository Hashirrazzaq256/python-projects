# function with default argument
def showEmployee(name, salary=9000):
    print(f"{name} , salary: {salary} ")

showEmployee("hashir", 15000)
showEmployee("hashir")

# multiple return values

def calculation(a, b):
    addition = a + b
    subtraction = a - b
   
    return addition, subtraction
res = calculation(40, 10)
print(res)

# inner function

def outer_function(a,b):
    
    def inner_function():
        return a+b
    result = inner_function() 
    return result+5
answer = outer_function(2,4)    
print(answer)

# recursive function
def function(num):
    if num != 0:
        return num + function(num -1)
    else:
        return 0
result = function(10)
print(result)
#Assign a different name to function and call it through the new name
---
