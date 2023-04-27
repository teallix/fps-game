import time

def divide(x, y):
    return x / y
    
def multiply(x, y):
    return x * y
    
def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
while True:
    ai = input("Multiply[1], Divide[1], Add[3], or Subtract[4]?\n")
    
    if ai == "2":
        def aid():
            num1 = int(input("Enter first number"))
            num2 = int(input("Enter second number"))
            
            print(num1, "/", num2, "=", divide(num1, num2))
            
        aid()
        
    elif ai == "1":
        def ais():
            num1 = int(input("Enter first number"))
            num2 = int(input("Enter second number"))
            
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        ais()
        
    elif ai == "3":
        def ghi():
            num1 = int(input("Enter first number"))
            num2 = int(input("Enter second number"))
            
            print(num1, "+", num2, "=", add(num1, num2))
            
        ghi()
        
    elif ai == "4":
        def ter():
            num1 = int(input("Enter first number"))
            num2 = int(input("Enter second number"))
            
            print(num1, "-", num2, "=", subtract(num1, num2))
            
        ter()
        
    elif ai == "no":
        break
        
    else:
        time.sleep(0.1)
