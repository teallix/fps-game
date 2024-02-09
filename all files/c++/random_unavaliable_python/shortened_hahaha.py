import time
import random

while True:
    ai = input("Generate?\n")
    if ai == "yes":
        print(random.randint(1,9), "+", random.randint(1,9), "=", random.randint(1,9))
    elif ai == "yes ":
        while True:
            ais = input("Are you sure you want to loop?\n")
            if ais == "yes":
                while True:
                    aif = input("Are you positive?(This may crash your computer)\n")
                    if aif == "yes":
                        while True:
                            aid = input("Input '12345' to begin loop\n")
                            if aid == "12345":
                                while True:
                                    print(random.randint(1,100000000000000000000000000000000000000))
                            elif aid == "no":
                                break
                            elif aid not in ("yes", "no"):
                                time.sleep(0.1)
                    elif aif == "no":
                        break
                    elif aif not in ("yes", "no"):
                        time.sleep(0.1)
            elif ais == "no":
                break
            elif ais not in ("yes", "no"):
                time.sleep(0.1)
    elif ai == "no":
        break
    elif ai not in ("yes", "no", "yess"):
        time.sleep(0.1)