# Imports the time module for time stops
import time
# Imports the random module for randomizing things
import random

# Defines a(/a/) list(s) for characters to be picked from
lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', ';', ':', ',', '.', '>', '<', '/', '?', '|', '-', '_', '=', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# Creates a loop for the main part to be in to restart with everytime
while True:
    # Asks user if they want to generate a password
    ai = input("Generate password?\n")
    
    if ai == "yes":
        # Defines a new line for user input
        def aid():
            # Asks user how many characters they want in their password
            # Allows up to 15 characters max
            
            ais = input("Which mode?(c+n, c, n)\n")
            
            if ais == "yes":
                def hg():
                    al = input("How many characters?(1-15)\n")
                    
                    if al == "1":
                        print(random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "2":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), )
                        
                    elif al == "3":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "4":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "5":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "6":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "7":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "8":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "9":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                    
                    elif al == "10":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                    
                    elif al == "11":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "12":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                    
                    elif al == "13":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                    
                    elif al == "14":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                    
                    elif al == "15":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                    
                    elif al == "yes":
                        print(random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3), random.choice(lists), random.choice(list2), random.choice(list3))
                        
                    elif al == "back":
                        return
                    
                    elif al == "no":
                        quit()
                    
                    else:
                        time.sleep(0.1)
                        hg()
                        
                hg()
            if ais == "c+n":
                def rf():
                    aie = input("How many characters?(1-15)\n")
                    
                    if aie == "1":
                        print(random.choice(lists))
                
                    elif aie == "2":
                        print(random.choice(lists), random.choice(lists))
                
                    elif aie == "3":
                        print(random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "4":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "5":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "6":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "7":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "8":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "9":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "10":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "11":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "12":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "13":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "14":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif aie == "15":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
            
                    # Allows user to go back to the yes or no input
                    elif aie == "back":
                        aid()
                        
                    elif aie == "no":
                        quit()
                        
                    else:
                        time.sleep(0.1)
                        rf()
                rf()
            
            elif ais == "c": # Uses only characters in the password
                def gh():
                    fr = input("How many characters?(1-15)\n")
                    
                    if fr == "1":
                        print(random.choice(list2))
                        
                    elif fr == "2":
                        print(random.choice(list2), random.choice(list2))
                        
                    elif fr == "3":
                        print(random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "4":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "5":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "6":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "7":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "8":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "9":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "10":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "11":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "12":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "13":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "14":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "15":
                        print(random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2))
                        
                    elif fr == "back":
                        aid()
                        
                    elif fr == "no":
                        quit()
                        
                    else:
                        time.sleep(0.1)
                        gh()
                        
                gh()
            
            elif ais == "n": # Uses only numbers in the password
                def gt():
                    af = input("How many characters?(1-15)\n")
                    
                    if af == "1":
                        print(random.choice(list3))
                        
                    elif af == "2":
                        print(random.choice(list3), random.choice(list3))
                        
                    elif af == "3":
                        print(random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "4":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "5":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "6":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "7":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "8":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "9":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "10":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "11":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "12":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "13":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "14":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                        
                    elif af == "15":
                        print(random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3))
                    
                    elif af == "back":
                        aid()
                    
                    elif af == "no":
                        quit()
                    
                    else:
                        time.sleep(0.1)
                        gt()
                gt()
            
            elif ais == "no":
                quit()
                
            elif ais == "back":
                return
                
            else:
                aid()
        
        # Starts with the aid() part for password character amount picking        
        aid()
        
    # If user chooses no the loop breaks
    elif ai == "no":
        break
    
    # If the user enters anything other than allowed it restarts the loop
    else:
        time.sleep(0.1)
