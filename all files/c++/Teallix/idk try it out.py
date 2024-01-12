import time
import random

while True:
    def a():
        ai = input("make one?\n")

        if ai == "yes":
            def ae():
                for i in range(1000):
                    print(random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10,99), "|",i)
                    time.sleep(0.1)
                time.sleep(0.1)

            ae()

        elif ai == "admin":
            def aid():
                ai = input("go to where? [1], [2], [4]\n")

                lisu = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '|', ':', '"', ',', '.', '<', '>', '/', '?']
                lisi = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
                if ai == "1":
                    def restartornot():
                        ao = input("ready?\n")

                        ac = ("ready")
                        av = ("not ready")

                        if ao == "yes":
                            print("user is: ", ac)
                            time.sleep(1)
                            def ap():
                                aq = input("Enter first input: ")
                                
                                if aq == "7":
                                    def al():
                                        ax = input("Enter other input: ")
                                        
                                        if ax == "3":
                                            def ay():
                                                ar = input("Enter third input: ")
                                                
                                                if ar == "7":
                                                    def aw():
                                                        ab = input("Enter other input: ")
                                                        
                                                        if ab == "1":
                                                            def at():
                                                                an = input("Enter fifth input: ")
                                                                
                                                                if an == "1":
                                                                    def am():
                                                                        print("ex: ", random.choice(lisi), "utf- ", random.choice(lisi), "_$",)
                                                                        time.sleep(1)
                                                                        print("%error utf is", random.choice(lisi), "not in", random.choice(lisi), "interect")
                                                                        time.sleep(1)
                                                                        print("T in", random.choice(lisi), "+", random.choice(lisi), "[not_in] file_name_Pylace")
                                                                        time.sleep(1)
                                                                        try:
                                                                            print(KeyboardInterrupt, "is", reversed)
                                                                            
                                                                        finally:
                                                                            time.sleep(1)
                                                                            print(KeyError, "is not a", property, "for input_file_2Pylace")
                                                                            
                                                                        try:
                                                                            time.sleep(1)
                                                                            print("Error in --", lisi, "line 38: unexpected ", object)
                                                                            
                                                                        finally:
                                                                            time.sleep(1)
                                                                            print(type, ": E34-920-1i59 Error")
                                                                            quit()
                                                                            
                                                                    am()
                                                                    
                                                                elif an == "no":
                                                                    aw()
                                                                    
                                                                else:
                                                                    time.sleep(1)
                                                                    at()
                                                                    
                                                            at()
                                                            
                                                        elif ab == "no":
                                                            ay()
                                                            
                                                        else:
                                                            time.sleep(1)
                                                            aw()
                                                            
                                                    aw()
                                                    
                                                elif ar == "no":
                                                    al()
                                                    
                                                else:
                                                    time.sleep(1)
                                                    ay()
                                                    
                                            ay()
                                            
                                        elif ax == "no":
                                            ap()
                                            
                                        else:
                                            al()
                                    al()
                                elif aq == "no":
                                    restartornot()
                                    
                                else:
                                    time.sleep(1)
                                    ap()
                            ap()

                        elif ao == "no":
                            print("user is: ", av)
                            time.sleep(1)
                            aid()

                        else:
                            print("ex error")
                            time.sleep(1)
                            restartornot()

                    restartornot()

                elif ai == "2":
                    print("1", random.choice(lisu), "2")

                elif ai == "3":
                    print("3", random.choice(lisu), "4")

                else:
                    time.sleep(0.1)
                    aid()

            aid()

        elif ai == "no":
            quit()

        else:
            time.sleep(0.1)

    a()