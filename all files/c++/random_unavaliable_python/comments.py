import time # Imports the time module for things related to time
import random # Imports the random modules for things reltated to numbers or choices

while True: # Creates a loop for the user
    ai = input("Generate?\n") # Asks user if they want to generate or not
    
    if ai == "yes": # If they say yes it defines a new line
        def generator(): # Defines a new line for two random numbers between 1 and 9 to add each other
            num1 = random.randint(1,9) # Defines that num1 is equal to a random number between 1 and 9
            num2 = random.randint(1,9) # Defines that num2 is equal to a random number between 1 and 9
            
            print(num1, "+", num2, "=", num1 + num2) # Prints two random numbers plus each other
            
        generator() # Starts with generator if the user inputs yes
        
    elif ai == "no": # If the user inputs no it breaks the loop
        break
    
    elif ai != ("yes", "no"): # If the user input is not yes or no it wait 0.5 seconds to restart the loop
        time.sleep(0.5)