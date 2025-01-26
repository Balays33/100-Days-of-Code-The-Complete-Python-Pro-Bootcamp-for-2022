from art import logo

# #print(logo)

# #TODO: write out fuctions - add - subtract - multiply - divide

# def add(n1,n2):
#     return(n1+n2)

# def subtract(n1,n2):
#     return(n1-n2)

# def multiply(n1,n2):
#     return(n1*n2)

# def divide(n1,n2):
#     return(n1/n2)

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def operator(n1,n2):
#     for symbol in operations:
#         print(symbol)
#         if symbolum == symbol:
#             calculator = operations[symbol]
#             print(f" The calculation result: { calculator(n1,n2)}")


# newCalculator = True
# while newCalculator:
    
#     n1 = int(input("Number 1 : "))
#     n2 = int(input("Number 2 : "))
#     symbolum = input("What is your operator +: add,\n-: subtract,\n*: multiply,\n/: divide\n...: ")
#     operator(n1,n2)
#     procees = input("Do you want to continue C  with the last number or NEW calculation or EXIT : ").lower()
#     if procees == "exit":
#         newCalculator = False
#     elif procees == "new":
#         newCalculator = True
#     elif procees == "c":
#         n1= 10
#         print(n1) 
#         n2 = int(input("Number 2 : "))
#         operator(n1,n2)
#         continue
#     else:
#         print("Invalid input")


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("+"))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()


    