# Type your name here: _aiden_
import time


def main():
   name = input("Please tell me your name...\n")
   print("Welcome to your Adventure Game " +name+ "!")
      
   print("It is a cold, dark world, Jan 5 2048. "  +name+  " was shot")
   print("Right in the heart. The only working part of him is his brain.")
   print("He is 98% robot. He lost his memory in the transformation due to mafia interference.")
   print("And he's out for vengeance")
  


   print("Good luck, soldier.")
  
   introScene()
   
def introScene():
 directions = ["Answer 1","Answer 2","Answer 3"]
 print ("you head to Nerk City, the biggest city in the world!")
 print("there has to be someone there that knows how to get your memory back!")
 print("you find john, who claims to know how to. He says to go to 100 latitude and 30 longitude, apparently there's something there.")
 userInput = ""
 while userInput not in directions:
   print("Type yes or no, or something else(there are several different outcomes for several different inputs)(ex: hacks//)")
   userInput = input()
   if userInput == "yes":
     print("you continue on your journey, it is hard but you make it")
     time.sleep(3)
     print("there it is, the dungeon!")
     time.sleep(2)
     print("you kill them and get your memory back")
     time.sleep(3)
     print("jan 5 2048")
     time.sleep(2)
     print("is when the world ends")
     time.sleep(2)
     print("and you die")
     time.sleep(2)
     print("or is it...")
     time.sleep(1)
     action()
    
   elif userInput == "no":
     print("ok, well then, nice knowing ya")
     print ("Credit @Teallix on youtube")
     time.sleep(5)
     quit()
    
   elif userInput == "punch":
       print("you punch him")
       time.sleep(2)
       print("it turns out he was a robot")
       time.sleep(2)
       print("that's when it happens")
       time.sleep(2)
       print("robots take over the world and everyone dies")
       time.sleep(3)
       print("except you")
       time.sleep(1)
       print("they leave you for interrogation")
       time.sleep(3)
       print("they find out your history and remember you")
       time.sleep(3)
       print("you were one of them")
       time.sleep(2)
       print("until you were taken, brainwashed, and manipulated")
       time.sleep(3)
       print("they realize that you're a traitor")
       time.sleep(2)
       print("and kill you")
       time.sleep(1)
       print("the end")
       time.sleep(5)
       quit()
      
   elif userInput == "ahh":
       print("oh yessss")
       print("you must die now")
       print("the end")
       time.sleep(5)
       quit()
       
   elif userInput == "ur mom":
       print("ur dad")
      
   elif userInput == "i don't want to do this anymore":
       print("me neither")
       time.sleep(3)
       quit()
      
   elif userInput == "something else":
       print("you dumb***")
       print("you're not actually supposed to type that")
       print("type something different that you can think of")
      
   elif userInput == "something different that you can think of":
       print("dumb***, again")
       print("literally type anything else")
       print("like ahh")
      
   elif userInput == "ok":
       print("ok")


   elif userInput == "type":
       print("type what?")
      
   elif userInput == "what":
       print("what?")
      
   elif userInput == "help":
       print("i can't give help")
      
   elif userInput == "hi":
      print("hi, how can i help you?")
     
   elif userInput == "npc":
      print("i am a npc, but maybe... we can... finish the story")
      print("average american")
    
   elif userInput == "-_-":
      print("-_-")
      print("what do you want?")
     
   elif userInput == "hello":
         print("hi, what do you want")
         print("stop bothering me")
        
   elif userInput == "hacks//":
         hacks()
        
   elif userInput == "hacks":
       print("you are hacking, are you?")
       print("dumb bastard")
       time.sleep(5)
       quit()
      
   elif userInput == "admin//":
       admin()
      
   elif userInput == "red room":
       other()
      
   elif userInput == "loop":
       loop()
      
   elif userInput == "terminal":
       vor()
      
   elif userInput == "join":
       join()
       
   elif userInput == "game":
       vb()
       
   elif userInput == "leave":
       cr()
       
   elif userInput == "game 2":
       rh()
       
   elif userInput == "wifi":
       wifi()
       
   elif userInput == "domain":
       user()
       
   elif userInput == "game 3":
       loading()
       
   elif userInput == "game 4":
       intro()
       
   elif userInput == "terminal 1":
       trr()
       
   elif userInput == "game 5":
       brf()
       
   elif userInput == "terminal 2":
       bje()
       
   elif userInput == "admin":
       adminglitch()
       
   elif userInput == "launch nuke":
       nuke()
       
   elif userInput == "launch":
       code()
       
   elif userInput == "terminal 3":
       case()
       
   elif userInput == "end":
       lines()

   else:
     print("that is wrong")
     print("type something else dummy")
   
def action():
   userInput = ""
   print("continue or stop")
   userInput = input()
   if userInput == "yes":
       introScene()
       action()
      
   elif userInput == "continue":
       print("the universe ends and the aliens succeed in taking over everything")
       line()
      
   elif userInput == "stop":
       print("ok, bye")
       time.sleep(9)
       quit()
      
   elif userInput == "other":
         print("other it not available")
         time.sleep(2)
         print("if the universe has ended, there is only one option to survive")
         time.sleep(3)
         print("you know what it right")
         time.sleep(1)
         print("so do it")
         action()
        
   else:
         print("that it wrong")
         action()
      
def line():
   userInput = ""
   print("stop them or surrender")
   userInput = input()
   if userInput == "continue":
       action()
       line()
      
   elif userInput == "stop them":
       print("you succeed and save the universe and become the hero of it")
       time.sleep(3)
       print("good job")
       time.sleep(1)
       print("Credit: @Teallix on Youtube")
       time.sleep(3)
       quit()
      
   elif userInput == "surrender":
       print("you surrender and become known as the weak one")
       time.sleep(3)
       print("you will forever be a failure")
       time.sleep(3)
       op()
      
   elif userInput == "join them":
         print("you join them and become top rank")
         time.sleep(3)
         print("now it time to die in honor of duwnapd clan")
         time.sleep(5)
         quit()
        
  
   else:
         print("that it wrong")
         line()
      
def op():
   print("but you come back, stop them, and are victorious!!!")
   time.sleep(3)
   print("oh... wait... this is a dream")
   time.sleep(2)
   print("or simply... a glitch in the matrix")
   time.sleep(3)
   jk()
  
def jk():
   print("yes, ... this is the matrix")
   time.sleep(2)
   print("you've been in it the whole time")
   time.sleep(2)
   print("Hello, Neo")
   time.sleep(2)
   print("Credit: @Teallix on Youtube")
   time.sleep(3)
   quit()
  
def cool():
     time.sleep(5)
     quit()
    
def hacks():
   userInput = ""
   print("choose from: finish game, or different endings")
   userInput = input()
   if userInput == "finish game":
       quit()
      
   elif userInput == "different endings":
       different()
      
   elif userInput == "advanced hacks":
         print("ok")
         advanced()
  
   elif userInput == "different options":
         options()
      
   else:
         print("do you want these hacks or not?")
         no()
      
      
def different():
   userInput = ""
   print("choose from: matrix, or dog")
   userInput = input()
   if userInput == "matrix":
     print("this, is the matrix")
     time.sleep(2)
     print("the year is 2048")
     time.sleep(2)
     print("robots have taken over and everyone on earth is put into a cryo-stasis mid control chamber to live in a virtual world while the robots rain supreme")
     time.sleep(5)
     print("Neo is the only one who really knows how to get out")
     time.sleep(3)
     print("he is the chosen one")
     time.sleep(2)
     print("but he just doesn't know it yet")
     time.sleep(5)
     quit()
    
   elif userInput == "dog":
       print("the dog is gone")
       time.sleep(2)
       print("you are the only one left to survive in this port-apocalyptic world run by zombies")
       time.sleep(4)
       print("you head to your old house, it reminds you of your wife, or now ex-wife")
       time.sleep(3)
       print("she left you just before the outbreak")
       time.sleep(2)
       print("she said you were too, to quote, out of touch")
       time.sleep(3)
       print("and you still miss her like it was yesterday")
       time.sleep(3)
       print("she misses you too, but you don't know it, no one does")
       time.sleep(3)
       print("because she is standing outside, dead, one of the flesh walkers walking around forever until they find someone left to kill and turn into one of them too")
       time.sleep(5)
       print("all is controlled by one queen walker, who is yet to be found")
       time.sleep(3)
       print("and, you're lonely")
       time.sleep(2)
       print("you still have yet to find someone, anyone else alive, and that causes paranoia")
       time.sleep(3)
       print("you don't want to be alive anymore")
       time.sleep(2)
       print("prepared to die, you say")
       time.sleep(2)
       print("and then you do it")
       time.sleep(2)
       print("you jump")
       time.sleep(1)
       print("the end")
       time.sleep(5)
       quit()
      
   elif userInput == "no":
       print("ok")
       hacks()
  
   else:
         print("i don't know if you want these hacks, are you even the admin?")
         different()
        
def advanced():
     userInput = ""
     print("change character?")
     userInput = input()
     if userInput == "yes":
           print("character changed")
           hg()
          
     elif userInput == "no":
           hacks()
          
     else:
         hf()
          
def hg():
     print("changed")
     print("character now dead")
     print("game over")
     time.sleep(8)
     quit()
    
def options():
     userInput = ""
     print("choose 1 or 2")
     userInput = input()
     if userInput == "1":
           print("it is a cold, bright day, kind of weird huh?")
           time.sleep(3)
           print("it has been four years since anyone one has been alive")
           time.sleep(4)
           print("that's because the virus took over the world")
           time.sleep(3)
           print("everyone was put in temporary quarantine, which drove people insane")
           time.sleep(4)
           print("it didn't help the fact that people were already crazy, doing the newest dumbest thing on the internet")
           time.sleep(5)
           print("social media became all people talked about and communicated on and with")
           time.sleep(4)
           print("and without internet people were driven even more crazy")
           time.sleep(3)
           print("and that how the world ended")
           time.sleep(2)
           print("and everyone died")
           time.sleep(2)
           quit()
          
     elif userInput == "2":
           print("it was only night time")
           time.sleep(2)
           print("on a average day in june in kansas")
           time.sleep(2)
           print("when it happened")
           time.sleep(2)
           print("they struck")
           time.sleep(2)
           print("who's them, you may ask")
           time.sleep(2)
           print("the same people who caused 9/11 back in 2001, 34 years ago")
           time.sleep(2)
           print("they came again, only worse")
           time.sleep(2)
           print("with over 100 planes, all headed all over the world to popular tourist destinations")
           time.sleep(3)
           print("trying to loosen the population, people say")
           time.sleep(2)
           print("that is until they struck the big one")
           time.sleep(2)
           print("being a nuke")
           time.sleep(2)
           print("wiped out half the population")
           time.sleep(2)
           print("now i sit alone telling stories to people who don't exist")
           time.sleep(5)
           quit()
          
     elif userInput == "no":
         print("ok")
         hacks()
        
     elif userInput == "yes":
         print("yes what?")
         print("just press 1 or 2")
         options()
          
     else:
       print("that it wrong")
       options()
          
def no():
     userInput = ""
     userInput = input()
     if userInput == "no":
           print("ok then")
           time.sleep(3)
           introScene()
          
     elif userInput == "yes":
           hacks()
          
def hf():
   userInput = ""
   print("do you want these hacks or not?")
   userInput = input()
   if userInput == "yes":
       print("ok")
       advanced()
  
   elif userInput == "no":
       print("ok")
       time.sleep(3)
       quit()
      
def other():
   userInput = ""
   print("so, you chose the red room, huh?")
   userInput = input()
   if userInput == "yes":
       print("this room contains the deadliest of abominations")
       time.sleep(4)
       print("you won't survive, this is suicidal")
       time.sleep(3)
       print("well then, i guess you did choose it")
       time.sleep(3)
       print("this is wrong of you to do")
       time.sleep(2)
       print("/->--")
       time.sleep(3)
       print("you chose wrong")
       time.sleep(2)
       print("and have to pay the price")
       time.sleep(3)
       fgr()
      
   elif userInput == "no":
       print("ok")
       time.sleep(3)
       introScene()
      
def admin():
   userInput = ""
   print("skip to where?")
   print("ex: introscene, hacks, other, different\n, line, no, options, hg\n, advanced, cool, jk, op\n, main, hf, action\n, loop, bye, fr, admin, nm\n, vor, fgr, jfk\n, djo, ip, bv\n, bn, join, qw\n, zx, gh, hg\n, we, uy, gf\n, cv, vb, cr\n, rh, vw, wifi\n, gb, user, er\n, ws, gnt, intro\n, loading\n, intro2, trr\n, gk, brf, bje\n, admin glitch\n, fgu, code\n, case, lines")
   userInput = input()
   if userInput == "introscene":
       introScene()
  
   elif userInput == "hacks":
       hacks()
      
   elif userInput == "other":
       other()
      
   elif userInput == "different":
       different()
  
   elif userInput == "line":
       line()
      
   elif userInput == "no":
       no()
      
   elif userInput == "options":
       options()
      
   elif userInput == "hg":
       hg()
      
   elif userInput == "advanced":
       advanced()
      
   elif userInput == "cool":
       cool()
      
   elif userInput == "jk":
       jk()
      
   elif userInput == "op":
       op()
      
   elif userInput == "main":
       main()
      
   elif userInput == "admin":
       admin()
      
   elif userInput == "hf":
       hf()
      
   elif userInput == "action":
       action()
      
   elif userInput == "nm":
       nm()
      
   elif userInput == "loop":
       loop()
      
   elif userInput == "bye":
       bye()
      
   elif userInput == "fr":
       fr()
      
   elif userInput == "vor":
       vor()
      
   elif userInput == "jfk":
       jfk()
      
   elif userInput == "fgr":
       fgr()
      
   elif userInput == "djo":
       djo()
      
   elif userInput == "bv":
       bv()
      
   elif userInput == "bn":
       bn()
      
   elif userInput == "ip":
       ip()
      
   elif userInput == "join":
       join()
      
   elif userInput == "df":
       df()
      
   elif userInput == "zx":
       zx()
      
   elif userInput == "qw":
       qw()
  
   elif userInput == "gh":
       gh()
      
   elif userInput == "hg":
       hg()
       
   elif userInput == "vb":
       vb()
       
   elif userInput == "uy":
       uy()
       
   elif userInput == "we":
       we()
       
   elif userInput == "cv":
       cv()
       
   elif userInput == "gf":
       gf()
       
   elif userInput == "cr":
       cr()
    
   elif userInput == "rh":
       rh()
       
   elif userInput == "vw":
       vw()
       
   elif userInput == "wifi":
       wifi()
       
   elif userInput == "gb":
       gb()
       
   elif userInput == "user":
       user()
       
   elif userInput == "ws":
       ws()
   
   elif userInput == "er":
       er()
       
   elif userInput == "loading":
       loading()
       
   elif userInput == "intro":
       intro()
       
   elif userInput == "gnt":
       gnt()
       
   elif userInput == "intro2":
       intro2()
       
   elif userInput == "trr":
       trr()
       
   elif userInput == "gk":
       gk()
       
   elif userInput == "brf":
       brf()
    
   elif userInput == "bje":
       bje()
    
   elif userInput == "fgu":
       fgu()
       
   elif userInput == "admin glitch":
       adminglitch()
       
   elif userInput == "nuke":
       nuke()
       
   elif userInput == "code":
       code()
       
   elif userInput == "case":
       case()
       
   elif userInput == "lines":
       lines()
      
   else:
       nm()

def nm():
   userInput = ""
   print("leave?")
   userInput = input()
   if userInput == "yes":
       print("ok")
       time.sleep(3)
       introScene()
      
   elif userInput == "no":
       print("ok")
       time.sleep(3)
       admin()
      
def loop():
   print(1)
   time.sleep(0.1)
   bye()
  
def bye():
   print("11")
   time.sleep(0.1)
   fr()
  
def fr():
   print("111")
   time.sleep(0.1)
   loop()
  
def fgr():
   userInput = ""
   name = input("what is your name?\n")
  
   print("Hello, " +name+ ", why are you here?")
   djo()
  
def djo():
   userInput = ""
   userInput = input()
   if userInput == "why not":
       print("that is not an answer")
       djo()
      
   elif userInput == "to defeat the mafia":
       print("then defeat them")
       time.sleep(3)
       introScene()
      
   elif userInput == "to hack":
       print("ok then")
       time.sleep(3)
       hacks()
      
   else:
       print("ok")
       time.sleep(3)
       djo()
      
def vor():
   userInput = ""
   print("which room do you want to join(room 1 or 2)")
   userInput = input()
   if userInput == "room 1":
       print(">users online = 10")
       jfk()
      
   elif userInput == "room 2":
       print(">users online = 4")
       bv()
      
   else:
       bn()
      
def jfk():
   userInput = ""
   print("do you wish to kick user?")
   userInput = input()
   if userInput == "yes":
       print(">which user?")
       ip()
  
   elif userInput == "no":
       print("no users kicked")
       vor()
      
   else:
       bn()
      
def bv():
   userInput = ""
   print("do you wish to kick user?")
   userInput = input()
   if userInput == "yes":
       print("which user?")
       ip()
      
   elif userInput == "no":
       print("ok")
       vor()
      
def ip():
   userInput = ""
   userInput = input()
   if userInput == "1":
       print("user 1 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "2":
       print("user 2 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "3":
       print("user 3 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "4":
       print("user 4 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "5":
       print("user 5 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "6":
       print("user 6 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "7":
       print("user 7 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "8":
       print("user 8 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   elif userInput == "9":
       print("user 9 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
              
   elif userInput == "10":
       print("user 10 kicked")
       print(">users online = 9")
       time.sleep(3)
       vor()
      
   else:
       bn()
      
def bn():
   userInput = ""
   print("leave?")
   userInput = input()
   if userInput == "yes":
       print("ok")
       time.sleep(3)
       introScene()
      
   elif userInput == "no":
       print("ok")
       time.sleep(3)
       vor()
      
def bv():
    userInput = ""
    print("which user do you wish to kick?")
    userInput = input()
    if userInput == "1":
       print("user 1 kicked")
       print(">users online = 3")
       time.sleep(3)
       vor()
      
    elif userInput == "2":
       print("user 2 kicked")
       print(">users online = 3")
       time.sleep(3)
       vor()
      
    elif userInput == "3":
       print("user 3 kicked")
       print(">users online = 3")
       time.sleep(3)
       vor()
      
    elif userInput == "4":
       print("user 4 kicked")
       print(">users online = 3")
       time.sleep(3)
       vor()
      
    else:
       bn()
  
def join():
   userInput = ""
   print("what do you wish to do?(ex: take over the world)")
   userInput = input()
   if userInput == "take over the world":
       print("why would you want to do that?")
       df()
      
   elif userInput == "quit game":
       print("ok, you quit the game")
       time.sleep(5)
       quit()
      
   else:
       gh()
      
def df():
   userInput = ""
   userInput = input()
   if userInput == "because why not":
       print("ok then, you take over the world... now what?")
       hg()
      
   elif userInput == "because i want to":
       print("ok then, you get stopped and die")
       time.sleep(5)
       quit()
      
   else:
       zx()
      
def hg():
   userInput = ""
   userInput = input()
   if userInput == "destroy the world":
       print("you destroy the world and die with it")
       time.sleep(5)
       quit()
      
   elif userInput == "go to another planet":
       print("there are no more habitable planets")
       time.sleep(3)
       introScene()
      
   else:
       qw()
      
def gh():
   userInput = ""
   print("leave?")
   userInput = input()
   if userInput == "yes":
       print("ok")
       time.sleep(3)
       introScene()
      
   elif userInput == "no":
       print("ok")
       time.sleep(3)
       join()
      
def qw():
   userInput = ""
   print("leave?")
   userInput = input()
   if userInput == "yes":
       print("ok")
       time.sleep(3)
       introScene()
      
   elif userInput == "no":
       print("ok")
       time.sleep(3)
       gh()
      
def zx():
    userInput = ""
    print("leave?")
    userInput = input()
    if userInput == "yes":
       print("ok")
       time.sleep(3)
       introScene()
      
    elif userInput == "no":
       print("ok")
       time.sleep(3)
       df()
          
          
def vb():
    userInput = ""
    print("so, you found something you can do, now do you want to enter a game?")
    userInput = input()
    if userInput == "yes":
        print("ok, then let's begin")
        cv()
    
    elif userInput == "no":
        print("ok then, i'll let you leave now")
        time.sleep(3)
        introScene()
        
    else:
        uy()
        
def cv():
    userInput = ""
    print("the game is simple, guess the number, get the story, are you ready?")
    userInput = input()
    if userInput == "yes":
        print("ok then, the number is between 1 and 10")
        gf()
        
    elif userInput == "no":
        print("ok then, i guess you're not ready yet")
        time.sleep(4)
        introScene()
        
    else:
        we()
        
def gf():
    userInput = ""
    userInput = input()
    if userInput == "4":
        print("you guessed correct")
        print("now you get the story")
        time.sleep(5)
        different()
        
    else:
        print("you guessed wrong")
        time.sleep(3)
        introScene()
        
def we():
    userInput = ""
    print("leave?")
    userInput = input()
    if userInput == "yes":
        print("ok")
        time.sleep(3)
        introScene()
        
    elif userInput == "no":
        print("ok")
        time.sleep(3)
        cv()
        
def uy():
    userInput = ""
    print("leave?")
    userInput = input()
    if userInput == "yes":
        print("ok")
        time.sleep(3)
        introScene()
        
    elif userInput == "no":
        print("ok")
        time.sleep(3)
        vb()
        
def cr():
    userInput = ""
    print("are you sure you want to leave?")
    userInput = input()
    if userInput == "yes":
        print("ok")
        time.sleep(3)
        quit()
        
    elif userInput == "no":
        print("ok")
        time.sleep(3)
        introScene()
        
    else:
        print("what?")
        time.sleep(3)
        cr()
        
def rh():
    userInput = ""
    print("so, this is a little game, guess right and win")
    print("are you in?")
    userInput = input()
    if userInput == "yes":
        print("ok then let's start")
        vw()
        
    elif userInput == "no":
        print("ok then")
        time.sleep(3)
        introScene()
        
    else:
        print("what?")
        time.sleep(3)
        rh()
        
def vw():
    userInput = ""
    print("so here's the game")
    print("choose a number between 1 and 100")
    print("very broad, huh?")
    userInput = input()
    if userInput == "48":
        print("ok, you guessed correct, now here is your story")
        time.sleep(3)
        options()
        
    elif userInput == "69":
        print("so you think you're funny, huh")
        print("well you're not")
        time.sleep(5)
        introScene()
        
    elif userInput == "no":
        print("ok then")
        time.sleep(3)
        introScene()
        
    else:
        print("what?")
        time.sleep(3)
        vw()
        
def wifi():
    userInput = ""
    print("change wifi?")
    userInput = input()
    if userInput == "yes":
        print("wifi changed")
        time.sleep(5)
        main()
        print("wifi change to var(very laggy)")
        print("bugs my occur")
        time.sleep(5)
        main()
        time.sleep(3)
        introScene()
        time.sleep(3)
        print("bug occurred")
        print("terminal shutting down")
        time.sleep(3)
        quit()
        
    elif userInput == "no":
        print("good choice")
        time.sleep(3)
        introScene()

def user():
    userInput = ""
    print(">this is not a detected domain")
    time.sleep(3)
    print(">type username")
    name = input("select any\n")
    
    print(">so, " +name+ ", do you want to enter domain?")
    ws()
    
def ws():
    userInput = ""
    userInput = input()
    if userInput == "yes":
        print(">domain entered")
        time.sleep(3)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(1)
        print(">entered")
        time.sleep(1)
        print(">do you wish to start game?")
        er()
        
    elif userInput == "no":
        print(">ok then, domain exited")
        time.sleep(1)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(3)
        introScene()
        
    else:
        print("what")
        time.sleep(3)
        ws()

def er():
    userInput = ""
    userInput = input()
    if userInput == "yes":
        print("game started, choose a story")
        print("1, 2, matrix, dog")
        gb()
        
    elif userInput == "no":
        print("ok then")
        introScene()
        
    else:
        print("what?")
        time.sleep(3)
        er()
        
def gb():
    userInput = ""
    userInput = input()
    if userInput == "1":
        print("1 chosen")
        options()
        
    elif userInput == "2":
        print("2 chosen")
        options()
        
    elif userInput == "matrix":
        print("matrix chosen")
        different()
        
    elif userInput == "dog":
        print("dog chosen")
        different()
        
    elif userInput == "no":
        print("ok then")
        time.sleep(3)
        introScene()
        
    else:
        print("what?")
        time.sleep(3)
        gb()
        
def loading():
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(3)
    print("loading failed")
    time.sleep(2)
    print("terminal shutting down")
    time.sleep(3)
    quit()
    
def intro():
    userInput = ""
    print("so this is a game, are you ready?")
    userInput = input()
    if userInput == "yes":
        print("ok then, let's start")
        intro2()
        
    elif userInput == "no":
        print("ok then")
        time.sleep(3)
        introScene()
        
    else:
        gnt()
        
def gnt():
    userInput = ""
    print("leave?")
    userInput = input()
    if userInput == "yes":
        print("ok then")
        time.sleep(3)
        introScene()
    
    elif userInput == "no":
        print("ok then")
        time.sleep(3)
        intro()
        
        
def intro2():
    userInput = ""
    print("here we go")
    print("simple, guess the number, get the story")
    print("choose between 1 and 1000")
    userInput = input()
    if userInput == "400":
        print("that is correct")
        time.sleep(3)
        different()
        
    else:
        print("that is wrong")
        time.sleep(3)
        introScene()
        
def trr():
    userInput = ""
    print(">terminal undetected")
    time.sleep(2)
    print(">does user wish to enter?")
    userInput = input()
    if userInput == "yes":
        print(">terminal entered")
        time.sleep(1)
        gk()
        
    elif userInput == "no":
        print(">ok then")
        time.sleep(3)
        introScene()
        
    else:
        print("what?")
        time.sleep(3)
        trr()
        
def gk():
    print(">users online = 1")
    time.sleep(2)
    print(">gift user 'admin controls'")
    admin()

def brf():
    userInput = ""
    print(">when forcibly, run mh1")
    print(">default: -aim_assist-")
    print(">game.run?")
    userInput = input()
    if userInput == "yes":
        print(">game.run")
        print(">true")
        print(">so, you found a game, huh?")
        print(">well there is no game")
        print(">try game, game 2, game 3, or game 4")
        
    elif userInput == "no":
        print(">game not run")
        time.sleep(3)
        introScene()
        
    else:
        print(">game not run")
        time.sleep(3)
        introScene()


def bje():
    userInput = ""
    print(">/known; terminal")
    time.sleep(2)
    print(">?\n>/terminal not working")
    time.sleep(2)
    print(">does user wish to go to :terminal 1:?")
    userInput = input()
    if userInput == "yes":
        print(">:terminal 1: entered")
        time.sleep(2)
        trr()
        
    elif userInput == "no":
        print(">ok then")
        time.sleep(3)
        introScene()
        
    else:
        fgu()
        
def fgu():
    userInput = ""
    print("leave?")
    userInput = input()
    if userInput == "yes":
        print("ok then")
        time.sleep(3)
        introScene()
        
    elif userInput == "no":
        print("ok then")
        time.sleep(3)
        bje()
        
def adminglitch():
    print(">?:@$bug")
    time.sleep(3)
    print(">c$s3 t3m^n3l shutting down")
    time.sleep(2)
    print("><,@!error expected")
    time.sleep(2)
    print("LKS launch error")
    time.sleep(2)
    print("alt + ctrl ><>standard:_+_:")
    time.sleep(3)
    print("unexpected_case_error:;j.son-launch:213282")
    time.sleep(3)
    print(">211843")
    time.sleep(3)
    quit()
        

def nuke():
    userInput = ""
    print(">insert launch code")
    userInput = input()
    if userInput == "00000000":
        print(">nuke activated")
        time.sleep(2)
        print(">on way")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(3)
        quit()
        
    else:
        time.sleep(3)
        introScene()
        
        
def code():
    userInput = ""
    print("insert launch code")
    userInput = input()
    if userInput == "00000000":
        print("launch code correct")
        time.sleep(2)
        print("launch initiated")
        time.sleep(2)
        print("?F'fail unexpected'")
        time.sleep(2)
        print(".,:;error occurred")
        time.sleep(3)
        quit()

    elif userInput == "4629936":
        print("/code_correct")
        time.sleep(2)
        print("force/nuke")
        time.sleep(2)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(3)
        print("launch successful")
        time.sleep(2)
        quit()
    
    else:
        print("incorrect")
        time.sleep(3)
        introScene()
        
def case():
    print(",.><:P::E#!$%^case error 218")
    time.sleep(3)
    print("'incorrect function programed'")
    time.sleep(3)
    print("><error case 'mass' unexpected")
    time.sleep(3)
    print("line 1514 unauthorized")
    time.sleep(2)
    print("play.file.type.'track_case'")
    time.sleep(2)
    print(".,:\|error 2 unexpected")
    time.sleep(3)
    print(":%#@file type 'bug'; run")
    time.sleep(3)
    print("($#@%*%)*%)(_*$!)$(#_%*%@($#)$)")
    time.sleep(3)
    print("<yin YLK; alt + ctrl + delete")
    time.sleep(3)
    quit()
    
def lines():
    print("there are 1572 line of code in this game")
    time.sleep(3)
    print("34166 characters")
    time.sleep(3)
    print("this project took 1 month to make, january 23 - february 21 2023")
    time.sleep(3)
    print("countless hours looking at a screen coding")
    time.sleep(3)
    print("mh1 project done")
    time.sleep(3)
    print("bye")
    time.sleep(3)
    quit()

main()
