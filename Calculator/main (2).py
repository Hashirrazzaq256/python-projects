from art import logo
def add(n1,n2):
  return n1+n2
  
def subtract(n1,n2):
  return n1-n2

def product(n1,n2):
  return n1*n2

def division(n1,n2):
  return n1/n2

operation = {
  "+":add,
  "-":subtract,
  "*":product,
  "/":division
}
def calculator():
  print(logo)
  num1 = float(input("what is your first number "))
  
  for keys in operation:
    print(keys)
  should_continue = True
  while  should_continue:
    operational_symbol= input("what operation do you want to perform ")  
    num2 = float(input("what is next number ")) 
    calculation = operation[operational_symbol]
    answer = calculation(num1,num2)
    print(f"{num1} {operational_symbol} {num2} = {answer}")
    if input(f"type y if you want to continue performing operations on {answer} and press 'n to star again '").lower()=="y":
      num1 = answer
    else:
      should_continue = False
      calculator()
      
    # operational_symbol = input("what is the next operation")
    # num3 = int(input("what is your next number"))
    # calculation = operation[operational_symbol]
    # answer = calculation(answer,num3)
calculator()