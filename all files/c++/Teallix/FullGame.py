import time
import random

while True:
    ao = input("Start?\n")
    
    lin = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if ao == "yes":
        def at():
            ai = input("Enter Firebase?\n")
            
            if ai == "yes":
                def al():
                    au = input("Find the eye where? Plane crash[1], Dr. Weaver[2], or Burnt Building[3]\n")
                    
                    if au == "1":
                        def PlaneCrash():
                            ap = input("First you must fight off a horde. Do you use Spray-ray[1], Main Weapon[2], or Lethal[3]\n")
                            
                            if ap == "1":
                                def SprayRayOut():
                                    ar = input("You fought off the horde. Do you pick up the Eyeball?\n")
                                    
                                    if ar == "yes":
                                        def EyeballPickup():
                                            print("Krevchenko: You must make sure that eye is the correct one")
                                            time.sleep(3)
                                            print("For that you must fend off an attack on the eye")
                                            time.sleep(2)
                                            ah = input("Do you use Spray-ray[1], Ray-k[2], or run[3]\n")
                                            
                                            if ah == "1":
                                                def MakeEyeSpray():
                                                    print("Krevchenko: I see you survived")
                                                    time.sleep(2)
                                                    print("Now you must get the keycard from Weaver")
                                                    time.sleep(2)
                                                    print("Then you need to open the cabinets with that keycard until you find the mix")
                                                    ad = input("Which cabinet do you choose? [1], [2], [3], [4], or [5]\n")
                                                    
                                                    if ad in ["1", "4"]:
                                                        def CorrectCabinet():
                                                            print("Krevchenko: Put this serum in the fan above of Dr. Peck")
                                                            time.sleep(2.5)
                                                            print("This will hallucinate him and force him to give you the code to the satelite")
                                                            time.sleep(3)
                                                            print("This will let us restore power to the base")
                                                            time.sleep(2)
                                                            ax = input("Do you place serum[1], or not place serum[2]\n")

                                                            if ax == "1":
                                                                def SerumPlacedPeckCode():
                                                                    print("Peck: You used my own serum against me?")
                                                                    time.sleep(2.3)
                                                                    print("Is it even a proper dose?")
                                                                    time.sleep(1.5)
                                                                    print("Oh it might be")
                                                                    time.sleep(1.2)
                                                                    print("Symtom check: Goosebumps, Feeling of loneliness, and euphoria, a feeling of happiness")
                                                                    time.sleep(3.5)
                                                                    print("Weaver: What is the code Peck?")
                                                                    time.sleep(1.7)
                                                                    print("Peck: Fine, the code is ", random.choice(lin), random.choice(lin), random.choice(lin), random.choice(lin), "-", random.choice(lin), random.choice(lin), random.choice(lin), random.choice(lin), "-", random.choice(lin), random.choice(lin), random.choice(lin), random.choice(lin))
                                                                    time.sleep(3)
                                                                    print("Weaver: Go to the satelite and start the portal")
                                                                    time.sleep(1.8)
                                                                    ad = input("Do you got to the satelite[1] or not[2]\n")

                                                                    if ad in ("yes", "1"):
                                                                        def BossFightStart():
                                                                            print("Krevchenko: Get back to Weaver, Orda is almost here")
                                                                            time.sleep(1.75)
                                                                            print("Weaver: You have to fend off that beast or else it was all for nothing")
                                                                            time.sleep(2.5)
                                                                            print("Get Maxis back alive")
                                                                            time.sleep(1.5)
                                                                            aq = input("Do you use Spray-Ray[1], Ray k84[2], or Main gun[3]\n")

                                                                            if aq == "1":
                                                                                def BossFightOver():
                                                                                    print("Orda: You can't do this to me")
                                                                                    time.sleep(1.5)
                                                                                    print("Maxis: Too late now")
                                                                                    time.sleep(1.5)
                                                                                    print("Hey Peck, your plan backfired, how do you feel now?")
                                                                                    time.sleep(2)
                                                                                    print("Peck: I didn't expect this to happen")
                                                                                    time.sleep(2)
                                                                                    print("|================================================================|")
                                                                                    print("|  Player name  |  Score  |  Kills  |  Critical kills  |  Downs  |")
                                                                                    print("|  Jmoney26     | ", random.randint(100000, 200000), "| ", random.randint(1500, 2500), "  | ", random.randint(1000, 1500), "           |  5      |")
                                                                                    print("|================================================================|")

                                                                                BossFightOver()

                                                                            elif aq == "2":
                                                                                print("Apparently 1584 damage is not enough against Orda")
                                                                                time.sleep(2)
                                                                                print("Because you died")
                                                                                time.sleep(1)
                                                                                print("What a shame")
                                                                                time.sleep(1)
                                                                                quit()

                                                                            elif aq == "3":
                                                                                print("You do realize that was a bad idea, right?")
                                                                                time.sleep(1.75)
                                                                                print("Because you died")
                                                                                time.sleep(1)
                                                                                quit()

                                                                            else:
                                                                                time.sleep(1)
                                                                                BossFightStart()

                                                                        BossFightStart()

                                                                    elif ad in ("no", "2"):
                                                                        print("What are you thinking?")
                                                                        time.sleep(1)
                                                                        print("Choices have consequences")
                                                                        time.sleep(1.5)
                                                                        quit()

                                                                    else:
                                                                        time.sleep(1)
                                                                        SerumPlacedPeckCode()

                                                                SerumPlacedPeckCode()

                                                            elif ax == "2":
                                                                print("Really now?")
                                                                time.sleep(1.5)
                                                                print("Betray your only savior?")
                                                                time.sleep(2)
                                                                quit()

                                                            else:
                                                                time.sleep(1)
                                                                SerumPlacedPeckCode()
                                                            
                                                        CorrectCabinet()
                                                        
                                                    else:
                                                        time.sleep(2)
                                                        print("Wrong one")
                                                        time.sleep(1.5)
                                                        print("With choices come consequences")
                                                        time.sleep(2)
                                                        print("And yours is death")
                                                        time.sleep(2)
                                                        quit()
                                                    
                                                MakeEyeSpray()
                                                
                                            elif ah == "2":
                                                def MakeEyeK():
                                                    print("You run out of ammo")
                                                    time.sleep(2)
                                                    print("Now you must do something")
                                                    time.sleep(2)
                                                    print("But you are overrun")
                                                    time.sleep(1.5)
                                                    quit()
                                                    
                                                MakeEyeK()
                                                
                                            elif ah == "3":
                                                print("Krevchenko: You coward")
                                                time.sleep(2)
                                                print("Krevchenko: Now the world will burn")
                                                time.sleep(3)
                                                quit()
                                                
                                        EyeballPickup()
                                    
                                    elif ar == "no":
                                        return
                                    
                                    else:
                                        time.sleep(1)
                                        SprayRayOut()
                                        
                                SprayRayOut()
                                
                            elif ap == "2":
                                print("Not Enough damage")
                                time.sleep(1)
                                print("You died")
                                time.sleep(1)
                                at()
                                
                            elif ap == "3":
                                print("They run towards you and you kill yourself with your own lethal")
                                time.sleep(1)
                                print("You Died")
                                time.sleep(1)
                                at()
                                
                            else:
                                time.sleep(1)
                                PlaneCrash()
                                
                        PlaneCrash()
                        
                    elif au == "2":
                        def DrPeck():
                            print("Dr. Peck: Why are you here?")
                            time.sleep(2.5)
                            print("Dr. Peck: I do not have whatever it is you are looking for")
                            time.sleep(2.5)
                            print("You: How do i know that?")
                            time.sleep(2.5)
                            print("Dr. Peck: Because I would be dead right now, so would you")
                            time.sleep(2.5)
                            print("You: What does that mean?")
                            time.sleep(2.5)
                            print("Dr. Peck: That eye emits large ammounts of radiation")
                            time.sleep(2.5)
                            print("And you must not know this")
                            time.sleep(2.5)
                            print("You Died")
                            time.sleep(1.5)
                            quit()
                            
                        DrPeck()
                        
                    elif au == "3":
                        def BurntBuilding():
                            print("The building is on 27th street, next to Der Dozen")
                            time.sleep(2.5)
                            print("It has had nothing in there in years")
                            time.sleep(1.5)
                            print("All there is is Mer`da, queen of the megatons")
                            time.sleep(2.5)
                            print("She is said to have taken something very vaulable many years ago")
                            time.sleep(2.5)
                            print("That eye might be it")
                            time.sleep(1)
                            ag = input("Do you fight her[1], or not go[2]\n")
                            
                            if ag == "1":
                                def MerdaFight():
                                    ac = input("Do you use Ray-k[1], Raygun[2], or Main gun[3]\n")
                                    
                                    if ac == "1":
                                        print("Too slow")
                                        time.sleep(1.5)
                                        print("You can't kill her in time and get overrun")
                                        time.sleep(2)
                                        quit()
                                        
                                    elif ac == "2":
                                        def MerdaEnd():
                                            print("She didn't have the eye")
                                            time.sleep(1.5)
                                            print("It was all for nothing")
                                            time.sleep(1.5)
                                            quit()
                                            
                                        MerdaEnd()
                                        
                                    elif ac == "3":
                                        print("Not enough for the queen")
                                        time.sleep(1.5)
                                        print("You cannot hold her off")
                                        time.sleep(1.5)
                                        quit()
                                        
                                MerdaFight()
                                
                            elif ag == "2":
                                print("Krevchenko: You coward, run away?")
                                time.sleep(1.5)
                                print("Pathetic")
                                time.sleep(1)
                                quit()
                                
                            
                        BurntBuilding()
                    elif au in ["back", "no"]:
                        return
                    
                    else:
                        time.sleep(1)
                        al()
                al()
                
            elif ai == "no":
                return
            
            else:
                time.sleep(1)
                at()
                
        at()
        
    elif ao == "no":
        break
    
    else:
        time.sleep(1)