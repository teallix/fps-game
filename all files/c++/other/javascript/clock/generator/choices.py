# Impots time for delays
import time
# Imports random for password generator
import random
# imports collections for fps counter
import collections

# Defines a list for characters to be picked from
lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', ';', ':', ',', '.', '>', '<', '/', '?', '|', '-', '_', '=', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

while True:
    ais = input("What is your choice? Choices include: fps counter[1], game[2], password generator[3], exit[4]\n")
    
    if ais == "1":
        class FPS:
            def __init__(self,avarageof=50):
                self.frametimestamps = collections.deque(maxlen=avarageof)
            def __call__(self):
                self.frametimestamps.append(time.time())
                if(len(self.frametimestamps) > 1):
                    return len(self.frametimestamps)/(self.frametimestamps[-1]-self.frametimestamps[0])
                else:
                    return 0.0
        
        fps = FPS()
        for i in range(100):
            time.sleep(0.1)
            print(fps())
        time.sleep(1)
        
    elif ais == "2":
        def main44():
            name = input("your name?\n")

            print("so, " + name + ", your mission is to assassinate the high value target")
            time.sleep(3)
            print("are you up for the job?")
            introsceners()


        def introsceners():
            userInput = ""
            userInput = input()
            if userInput == "yes":
                print("the target's name is Namasol Carvrov, the president of Nuemnistand")
                time.sleep(3)
                print("you kill him, you get your pilot, you don't or fail to do so, and your pilot gets bleed dry")
                time.sleep(5)
                print("let's do it then")
                time.sleep(2)
                actions()

            elif userInput == "no":
                print("well then, you are no longer")
                time.sleep(3)
                quit()

            else:
                print("that is not an answer")
                time.sleep(1)
                introsceners()
                
        def actions():
            userInput = ""
            print("where do you want to go, there are several places he can be?")
            time.sleep(2)
            print("choose from: quiester, lonuemnfi, and guestinger")
            userInput = input()
            if userInput == "quiester":
                print("ok then, let's go there")
                time.sleep(2)
                quiester()

            elif userInput == "lonuemnfi":
                print("ok then, let's go there")
                lonuemnfi()

            elif userInput == "guestinger":
                print("ok then let's go")
                guestinger()
        
            elif userInput == "no":
                print("ok then")
                time.sleep(3)
                quit()
        
            else:
                print("that is not an answer")
                time.sleep(1)
                actions()


        def quiester():
            userInput = ""
            print("so, you're here, where do you want to go?")
            time.sleep(3)
            print("choose from: farmlands, high rise, and prison")
            userInput = input()
            if userInput == "farmlands":
                print("you head there")
                time.sleep(2)
                print("and he is not there")
                time.sleep(2)
                print("that means your pilot is dead")
                time.sleep(3)
                quit()

            elif userInput == "high rise":
                print("the high rise is the highest point in Nuemnistand")
                time.sleep(3)
                print("he could be there...")
                time.sleep(2)
                highrise()

            elif userInput == "prison":
                print("who knows, he could give the prisoners a visit")
                time.sleep(3)
                print("let's go there then")
                time.sleep(3)
                prison()

            elif userInput == "no":
                print("ok then, i'll drink the blood of your pilot then")
                time.sleep(3)
                quit()

            elif userInput == "back":
                print("ok then")
                time.sleep(2)
                actions()

            else:
                print("that is not an option")
                time.sleep(1)
                quiester()


        def lonuemnfi():
            userInput = ""
            print("you head there")
            time.sleep(2)
            print("where do you want to go now?")
            time.sleep(3)
            print("choose from: locostat forest, nuem mountains, and lire shores")
            userInput = input()
            if userInput == "locostat forest":
                print("nothing is there besides death")
                time.sleep(2)
                print("and that means death for you and your pilot")
                time.sleep(3)
                quit()

            elif userInput == "nuem mountains":
                print("you head there and find a base")
                time.sleep(2)
                print("maybe he's there...")
                time.sleep(2)
                nuem()

            elif userInput == "lire shores":
                print("to shores you go")
                time.sleep(2)
                print("and no one is there")
                time.sleep(2)
                print("wrong judgment just killed your pilot, sorry not sorry")
                time.sleep(4)
                quit()

            elif userInput == "no":
                print("ok then, his blood is on your hands")
                time.sleep(3)
                quit()

            elif userInput == "back":
                print("ok then")
                time.sleep(2)
                actions()

            else:
                print("that is not an answer")
                time.sleep(1)
                lonuemnfi()


        def guestinger():
            userInput = ""
            print("here you are, the home of the president")
            time.sleep(2)
            print("take the shot")
            time.sleep(2)
            print("guess the bullet drop correctly, or else miss and your pilot dies")
            time.sleep(3)
            print("alongside you")
            time.sleep(2)
            print("guess from 1, 2, 3, and 4")
            userInput = input()
            if userInput == "1":
                print("way off, you die and so does your pilot")
                time.sleep(3)
                quit()

            elif userInput == "2":
                print("no, but close, you killed one of his guards")
                time.sleep(3)
                print("but not him, so goodbye to your pilot")
                time.sleep(3)
                quit()

            elif userInput == "3":
                print("correct, and you got him")
                time.sleep(2)
                print("and so here's your pilot")
                time.sleep(2)
                pilot()

            elif userInput == "4":
               print("no, way over his head")
               time.sleep(2)
               print("the blood of your pilot is on your hands now")
               time.sleep(4)
               quit()

            elif userInput == "no":
               print("ok then, say bye bye to your pilot")
               time.sleep(3)
               quit()

            elif userInput == "back":
               print("ok then")
               time.sleep(2)
               actions()

            else:
               print("that is not an option")
               time.sleep(1)
               guestinger()


        def nuem():
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(2)
            print("nuem mountains, huh?")
            time.sleep(2)
            print("well, you're nowhere near the president")
            time.sleep(3)
            quit()


        def prison():
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(2)
            print("prison is full of despair, not a president")
            time.sleep(2)
            print("but now is full of your pilot's blood")
            time.sleep(3)
            quit()


        def highrise():
            userInput = ""
            print("high rise is a highly protected military base on the south side of Nuemnistand")
            time.sleep(4)
            print("to get in you will have to use many different tactics")
            time.sleep(3)
            print("do you: kill the guards and get in side, or sneak around and get inside")
            time.sleep(3)
            print("type: option 1, or option 2")
            userInput = input()
            if userInput == "option 1":
                print("you die because there are too many")
                time.sleep(3)
                print("along with you pilot")
                time.sleep(3)
                quit()

            elif userInput == "option 2":
                print("a guard sees you and you die")
                time.sleep(2)
                print("i guess you aren't good at stealth")
                time.sleep(2)
                print("and so your pilot dies")
                time.sleep(3)
                quit()

            elif userInput == "option 3":
                print("good job, you made it inside")
                time.sleep(2)
                print("but he's not there")
                time.sleep(2)
                print("he was somewhere else")
                time.sleep(3)
                quit()

            elif userInput == "no":
                print("ok then, goodbye pilot")
                time.sleep(3)
                quit()

            elif userInput == "back":
                print("ok then")
                time.sleep(2)
                quiester()
       
            else:
                print("that is not an answer")
                time.sleep(2)
                highrise()


        def pilot():
            name = input("name please...\n")

            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(2)
            print("so, " + name + ", why did you choose to save me?")
            time.sleep(2)
            print("after all, you can't trust anybody")
            time.sleep(2)
            print("because really, i'm not who you think i am")
            time.sleep(2)
            print("i'm dead...")
            time.sleep(1.5)
            print("...and so are you")
            time.sleep(3)
            quit()


        main44()
        
    elif ais == "3":
        def ask():
            aiss = input("Generate Password?\n")
            
            if aiss == "yes":
                # Defines a new line for user input
                def aid():
                    # Asks user how many characters they want in their password
                    # Allows up to 15 characters max
                    ais = input("How many characters? [1 - 15]\n")
            
                    if ais == "1":
                        print(random.choice(lists))
                
                    elif ais == "2":
                        print(random.choice(lists), random.choice(lists))
                
                    elif ais == "3":
                        print(random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "4":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "5":
                        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "6":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "7":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                 
                    elif ais == "8":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "9":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                  
                    elif ais == "10":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "11":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "12":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "13":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "14":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
                    elif ais == "15":
                         print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
            
                    # Allows user to go back to the yes or no input
                    elif ais == "back":
                        return input
                
                    elif ais == "no":
                        quit()
                
                    else:
                        aid()
        
                # Starts with the aid() part for password character amount picking        
                aid()
                
            elif aiss == "no":
                return input
            
            elif aiss == "back":
                return input
            
            else:
                time.sleep(0.1)
                
        ask()
            
            
        
    elif ais == "4":
        quit()
        
    else:
        time.sleep(0.1)