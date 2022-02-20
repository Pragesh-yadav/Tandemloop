class Calculator:
    # Addition
    def add(self, a, b):
        return a+b
    # Subtraction
    def subtract(self, a, b):
        return a-b
    # Multipication  
    def multiply(self, a, b):
        return a*b
    # Divition
    def divide(self, a, b):
        return a//b

#creating a Calculator Object
my_cal = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    
    ch = int(input("Select operation: "))
    
    #Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4, 5):
        
        #first check whether user want to exit
        if(ch == 5):
            break
        
        #If not then ask fo the input and call appropiate methods        
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if(ch == 1):
            print(a, "+", b, "=", my_cal.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", my_cal.subtract(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", my_cal.multiply(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", my_cal.divide(a, b))
    
    else:
        print("Invalid Input")
