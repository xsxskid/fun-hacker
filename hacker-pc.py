import os
import time
import random
#This app is just for funn
#This app is just for funnn

 #          __________     __________     __________     __________     __________
 #        |L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/L|
 #        |O|....................................................................|O|
 #        |O|...lol.............lol...lol.....loool................lololololol...|O|
 #        |O|...looool.......looool...lol...lool...................lol.....lol...|O|
 #        |O|...lol..loo...ool..lol...loo.oool...[lol]......[lol]..lol...........|O|
 #        |O|...lol...loOoOol...lol...loool........loool..loool....lololololol...|O|
 #        |O|...lol.....lol.....lol...lool............lloll................lol...|O|
 #        |O|...lol.............lol...lol..........loool..loool....lol.....lol...|O|
 #        |O|..loool...........loool..lol........[lol]......[lol]..lololololol...|O|
 #        |L|_________...................................__________     _________|L|
 #        |_\__LOoL__/......Mr-XS:D ["@Mr_xsami"]........\__LOoL__/LOo0L\__LOoL__/_|

#This app is just for funnnn
#This app is just for funnnnn
#This app is just for funnnnnn


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'





def mrxs2():
    print(color.GREEN +"""
      __________     __________     __________     __________     __________
    |L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/L|
    |O|                                                                    |O|
    |O|   lol             lol   lol     loool                lololololol   |O|
    |O|   looool       looool   lol   lool                   lol     lol   |O|
    |O|   lol  loo   ool  lol   loo oool   """+color.RED+"""[lol]      [lol]"""+color.GREEN+"""  lol           |O|
    |O|   lol   loOoOol   lol   loool        """+color.RED+"""loool  loool"""+color.GREEN+"""    lololololol   |O|
    |O|   lol     lol     lol   lool            """+color.RED+"""lloll"""+color.GREEN+"""                lol   |O|
    |O|   lol             lol   lol          """+color.RED+"""loool  loool"""+color.GREEN+"""    lol     lol   |O|
    |O|  loool           loool  lol        """+color.RED+"""[lol]      [lol]"""+color.GREEN+"""  lololololol   |O|
    |L|_________                                   __________     _________|L|
    |_\__LOoL__/  Telegram ID ["@Mr_xsami"] V:1.1.2\__LOoL__/LOo0L\__LOoL__/_|
    
    """)

def mrxs3():
    print(color.GREEN +"""
      __________     __________     __________     __________     __________
    |L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/LOo0L\__LOoL__/L|
    |O|....................................................................|O|
    |O|...lol.............lol...lol.....loool................lololololol...|O|
    |O|...looool.......looool...lol...lool...................lol.....lol...|O|
    |O|...lol..loo...ool..lol...loo.oool..."""+color.RED+"""[lol]      [lol]"""+color.GREEN+"""..lol...........|O|
    |O|...lol...loOoOol...lol...loool........"""+color.RED+"""loool  loool"""+color.GREEN+"""....lololololol...|O|
    |O|...lol.....lol.....lol...lool............"""+color.RED+"""lloll"""+color.GREEN+"""................lol...|O|
    |O|...lol.............lol...lol.........."""+color.RED+"""loool  loool"""+color.GREEN+"""....lol.....lol...|O|
    |O|..loool...........loool..lol........"""+color.RED+"""[lol]      [lol]"""+color.GREEN+"""..lololololol...|O|
    |L|_________...................................__________     _________|L|
    |_\__LOoL__/  Telegram ID ["@Mr_xsami"] V:1.1.2\__LOoL__/LOo0L\__LOoL__/_|

    """)

#  """+color.GREEN+"""

def banner():
    loadapp = (0)
    x = random.randint (5 , 60)
    y = random.randint (61 , 99)
    while True:
        clear()
        mrxs2()
        print("[" +color.WHITE+ "+" +color.GREEN+ "]" +"Attempting to hack the target..  \[",loadapp,"%]")
        if loadapp >= x:
            print("[" +color.WHITE+ "-" +color.GREEN+ "]"+color.RED+"Connection problem or something...")
        time.sleep(.1)
        clear()
        mrxs3()
        print("[" +color.WHITE+ "+" +color.GREEN+ "]" +"Attempting to hack the target... /[",loadapp,"%]")
        if loadapp >= x:
            print("[" +color.WHITE+ "-" +color.GREEN+ "]"+color.RED+"Connection problem or something..")
        time.sleep(.3)
        loadapp += 1
        if loadapp == y:
            input(color.GREEN+"[" +color.RED+ "-" +color.GREEN+ "]"+"ops;Check the internet connection and the target IP then"+color.RED+" try again")
            startshow()



def startshow():
    mrxs3()
    input1 = (input(color.GREEN +"Do you want to start hacking any computer model? \nEnter target IP for start attack or Q to quit \nDefault:192.168.1.1 >>"))
    if input1 != 'q' :
        banner()
    else:
        quit()            

clear()
#print("This app is just for fun \n")

startshow()
                                       