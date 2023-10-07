
def addition(num1,num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1,num2,result))

def subtraction(num1,num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1,num2,result))

def multiplication(num1,num2):
    result = num1 * num2
    print("{0} x {1} = {2}".format(num1,num2,result))

def division(num1,num2):
    if num2 == 0.0:
        print("Invalid 0 value ")
    else:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1,num2,result))

def square(num1):
    result = num1 * num1
    print("The Square Of {0} = {1}".format(num1,result))
    
while True:
    print ("What do you want to compute? ") # The different operation options
    print("1 Addition ")
    print("2 Subtraction ")
    print("3 Multiplication ")
    print("4 Division ")
    print("5 Square of a number ")
    print("6 Exit application ")
    print("\n")

    choice = input("Enter the number that corresponds to your choice: ") # This is where we recieve the command from the user
    int(choice) # Convert the string into an int

    if choice == '6': # To exit the calculator
         break

    if choice > '6': # Stop the calculator if command is not valid
        print("Please choose from the given choices ")
        break

    num1 = float(input("Enter The First Number : ")) # User will input the first number
    if choice == '5':
       square(num1)

    else:
       num2 = float(input("Enter The Second Number : ")) # User will input the second number

    if choice == '1': # Basic functions
             addition(num1,num2)
    elif choice == '2':
             subtraction(num1,num2)
    elif choice == '3':
              multiplication(num1,num2)
    elif choice == '4':
              division(num1,num2)

    print("\n")    
