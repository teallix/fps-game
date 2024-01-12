import time
import random
import sys
import re
import math
import locale
from resource import *
import resource

def main1():
    time.sleep(0.1)
    def main():
        ai = input("Time[1], Random[2], Sys[3], Re[4], Return[5], Math[6], Locale[7], Resource[8]\n")
        
        if ai == "1":
            for i in range(random.randint(10000,100000)):
                print(time.ctime(), "|", i)
                time.sleep(0.01)
        
        elif ai == "2":
            for i in range(random.randint(1000, 10000)):
                print(random.randint(10,99), random.randint(10,99), random.randint(10,99), "|", i)
                time.sleep(0.0001)
        
        elif ai == "3":
            def st():
                time.sleep(1)
                def is_even(list):
                    print(sys.argv[0])
                    print('Number of arguments present =', len(sys.argv))
                    print('Total argument list:', str(sys.argv))
                    if any(i%2==1 for i in list):
                        print("ERROR: Odd one is present in the even list! ")
                        sys.exit()
                    else:
                        print("Pure Even List")
                    list=[2,4,5,6,8,10]
                    is_even(list)
                    is_even(list)
                is_even(list)
            st()
            
        elif ai == "4":
            sta = 'word: Error, a, b, pi = 3.141592653'
            match = re.search(r'3.14', sta)
            
            if match:
                print(match.group())
                print(match.group(1))
                print(match.group(2))
                time.sleep(1)
                main1()
                
            elif not match:
                print('not', match.group(1))
                time.sleep()
                sys.exit()
                
            else:
                print('not found')
                time.sleep(1)
                main1()
        
        elif ai == "5":
            x = int(input("Enter first number: "))
            y = int(input("Enter other number: "))
            print(x // y)
            
        elif ai == "6":
            π = 3.14159265359
            r = 3
            Positive_Infinity = math.inf
            print(f"Positive_Infinity = {math.inf}")
            circumference = 2 * math.pi * r
            float("inf") == math.inf is True
            print(f"Circumference of a Circle = 2 * {math.pi:.4} * {r} = {circumference:.4} with π =", π)
            
        elif ai == "7":
            locale.setlocale(locale.LC_ALL, '')
            loc = locale.getlocale()
            locale.setlocale(locale.LC_ALL, 'de_DE')
            locale.strcoll('f\xe4n', 'foo')
            locale.setlocale(locale.LC_ALL, '')
            locale.setlocale(locale.LC_ALL, 'C')
            locale.setlocale(locale.LC_ALL, loc)
            locale.gettext('locale_language')
            for lang in locale.windows_locale.values():
                print(lang)
                
            for lang in locale.locale_alias.values():
                print(lang)
                
            for key, value in locale.localeconv().items():
                print("%s: %s" % (key, value))
                
        elif ai == "8":
            
            time.sleep(1)
            print(getrusage(RUSAGE_SELF))
            
            for i in range(10 ** 8):
                _ = 1 + 1
            print(getrusage(RUSAGE_SELF), "    ")
            time.sleep(1)
            print(getrusage(RLIM_INFINITY), "  ")
            time.sleep(1)
            print(getrusage(RUSAGE_CHILDREN), "")
            time.sleep(1)
            print(getrusage(RUSAGE_THREAD), "  ")
            for RLIMIT_DATA in range(1,2):
                RLIMIT_DATA = 5
        
    main()
    
main1()