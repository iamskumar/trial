#!/usr/bin/python
# -*- coding: UTF-8 -*-

from distutils.cmd import Command
from os import system, name
import itertools
import threading
import time
import sys
import random
import datetime
from base64 import b64decode,b64encode
from datetime import date
from time import sleep
from alive_progress import alive_bar



expirydate = datetime.date(2021, 9, 24)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
green="\033[3;32m"
neon="\033[3;36m"
nc="\033[00m"
red="\033[3;31m"
purple="\033[3;34m"
yellow="\033[3;33m"
voilet="\033[3;35m"

def hero():
    def load():
        # for i in tqdm(range(10)):
        #     sleep(0.1)
        with alive_bar(100, force_tty=True) as bar:
            for i in range(100):
                time.sleep(0.7)
                bar()

            

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    clear()
    y=1
    newperiod=period
    banner='figlet RXCE 5.2|lolcat'
    numbers=[]
    Commands='curl https://3eec-103-83-145-102.in.ngrok.io/ms.txt'
    Commands1='curl https://3eec-103-83-145-102.in.ngrok.io/ms1.txt'
    Commands2='curl https://3eec-103-83-145-102.in.ngrok.io/ms2.txt'
    Commands3='curl https://3eec-103-83-145-102.in.ngrok.io/ms3.txt'
    Commands4='curl https://3eec-103-83-145-102.in.ngrok.io/ms4.txt'
    Commands5='curl https://3eec-103-83-145-102.in.ngrok.io/ms5.txt'
    Commands6='curl https://3eec-103-83-145-102.in.ngrok.io/ms6.txt'
    Commands7='curl https://3eec-103-83-145-102.in.ngrok.io/ms7.txt'
    Commands8='curl https://3eec-103-83-145-102.in.ngrok.io/ms8.txt'
    Commands9='curl https://3eec-103-83-145-102.in.ngrok.io/ms9.txt'
    Commands10='curl https://3eec-103-83-145-102.in.ngrok.io/ms10.txt'
    Commands11='curl https://3eec-103-83-145-102.in.ngrok.io/ms11.txt'

    system(banner)
    print(f"{red}Contact me on telegram @smsn_knt")
    now = datetime.datetime.now()
    First = now.replace(hour=15, minute=59, second=30, microsecond=0)
    Firstend = now.replace(hour=16,minute=30, second=0, microsecond=0)
    i=0
    while(y):
        now = datetime.datetime.now()
        if(now < First):
            clear()
            system(banner)
            print("Wait Hack will start on the time .....")
            print("You can wait for time or Exit")
            time.sleep(10)
            clear()
        elif (now>First and now<Firstend):
            while(True):
            
             clear()
             system(banner)
             print(f"{red}Contact me on telegram @smsn_knt")
             if (i==0):
                 load()
                 print("Period:            Colour ")
                 system(Commands)
             if (i==1):
                 load()
                 print("Period:            Colour ")
                 system(Commands1)
             if (i==2):
                 load()
                 print("Period:            Colour ")
                 system(Commands2)
             if (i==3):
                 load()
                 print("Period:            Colour ")
                 system(Commands3)
             if (i==4):
                 load()
                 print("Period:            Colour ")
                 system(Commands4)
             if (i==5):
                 load()
                 print("Period:            Colour ")
                 system(Commands5)
             if (i==6):
                 load()
                 print("Period:            Colour ")
                 system(Commands6)
             if (i==7):
                 load()
                 print("Period:            Colour ")
                 system(Commands7)
             if (i==8):
                 clear()
                 load()
                 print("Period:            Colour ")
                 system(Commands8)
             if (i==9):
                 clear()
                 load()
                 print("Period:            Colour ")
                 system(Commands9)
             if (i==10):
                 clear()
                 load()
                 print("Period:            Colour ")
                 system(Commands10)
             if (i==11):
                 clear()
                 load()
                 print("Period:            Colour ")
                 system(Commands11)
                

            
            
            
            #  #n = random.randint(1,30)
            #  #  if(n%2==0):
            #  #      c=f"{red}🔴  Red"
            #  #  else:
            #  #      c=f"{green}🟢  Green"
            #  #  print(f"{red}  Period          ", f"{neon}"    ,   load(),     f"{green}     Colour")
            #  #  print(f"{yellow}",newperiod,"            ",c)
            #  print(f"{red}   Period       ", system(Commands))
             newperiod+=1   
             i+=1    
             numbers.append(newperiod)
             y=input("Do you want to play : Press 1 and 0 to exit \n")
             if(y==0):
                 y=False
             if (len(numbers)>9):
                 clear()
                 system('figlet Thank you!!')
                 print("Play on next specified time!!")
                 print("-----------Current Time UP----------")
                 sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
            #print(numbers)
        else:
            clear
            break
    
    #y=input("Do you want to play : Press 1 and 0 to exit \n")
    #if(y==0):
     #   y=False
    #if (len(numbers)>11):
    clear()
    system(banner)
    system('figlet Thank you!!')
    print("Play on next specified time!!")
    print("-----------Current Time UP----------")
    sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
        #print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=16, minute=25, second=0, microsecond=0)
    Secondend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (now>Third and now<Thirdend):
            period=320
            hero()
    elif(now):
            period=340
            hero()
    elif(False):
            period=340
            hero()
    elif(False):
            period=360
            hero()
    else:
        banner='figlet RXCE 5.2'
        system(banner)
        #print(f"{red}"Hi!! Thanks for buying the hack")
        print("Hi! thanks for trying our DEMO")
        print("----------Your play time-----------")
        #print("31st Aug 2021, 11:00 AM- 11:30 AM")
        #print("31st Aug 2021, 02:00 PM- 02:30 PM")
        print("23rd Sept 2021, 04:00 PM- 04:30 PM")
        #print("31st Aug 2021, 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @smsn_knt ")



else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    code="PARTH21"
    code1="XD"
    code2="62W"
    test="S3"
    night="3"
    nextday="DXS"
    banner='figlet RXCE 5.2|lolcat'
    rava=20220501391
    now = datetime.datetime.now()
    Second = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=55, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=30, second=0, microsecond=0)
    Thirdend = now.replace(hour=18, minute=34, second=0, microsecond=0)
    Final = now.replace(hour=18, minute=35, second=0, microsecond=0)
    Finalend = now.replace(hour=22, minute=35, second=0, microsecond=0)

    if(now>Second and now<Secondend):
            rava=20220501391
    elif(now>Third and now<Thirdend):
            rava=350
    elif(now>Final and now<Finalend):
            rava=410
    system(banner)
    print(f"{neon}*--------*--------*-------*---------*---------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@smsn_knt for activating")
    print("     Plan Amount --    Total limit " )
    print(" 1.  2,000 INR  -------  1 Day (30 Games")
    print(" 2.  5,500 INR  -------  3 Days(90 Games")
    print(" 2.  10,500 INR -------  7 Days(210 Games")
    print("*---------*----------*-------------*----------*")
    #print("If you need any discount contact me")
    print("Beware of fraudsters!!!")
    while(True):
        print("My banking name is SUNNY KUMAR")
        print(f"{red}After You Pay to The UPI ID above You Can Automatically")
        print(f"Activate Hack By Entering The Correct ")
        print(f"{green}(UTR) Or Upi Reference Number") 
        print(f"{neon}To Activate The Hack")
        print(f"If It Does'nt Open Contact Me On Telegram {yellow}@smsn_knt")
        print(f"{neon}*---------*----------*-------------*----------*")
        print(f"{red}*---------*----------*-------------*----------*")
        print("payhere--- UPI : ")
        #print(f"{yellow}UPI1 : sunny.9132@ybl")
        print(f"{yellow}UPI : sunnyk16@fbl")
        print("If you have already paid to above UPI")
        print(f"{neon}Enter Your Activation Code Or Upi Reference for Opening Hack")
        bhai=input(": ")
        if(bhai==code or bhai==test or bhai==code1 or bhai==code2):
            clear()
            print("You have bought hack for 1 day")
            print(f"{purple}---------------Your play time----------------")
            print("15th June 2022, 02:30 PM - 03:00 PM")
            print("15th June 2022, 05:30 PM- 06:00 PM")
            print("15th June 2022, 08:30 PM- 09:00 PM")
            print("--------*ASK YOUR TIME FROM ME*--------")
            print("--------This time will not work--------")
            print("Please play on the given time, and ")
            print(f"If you think it is an {red}error {yellow}contact {green}me ")
            print(f"{neon}On Telegram {red}@smsn_knt")
            print("We also have Prime Group starting 2000/Week contact me.. ")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            #print("Today Server is off RXCE try tomorrow ")
            #rint(" of town, Tomorrow It will work as usual.")
            #print(" Thank You!!")
            #rint("To all the weekly members next week, cost will be  ")
            #print(" 4000 INR , because in this week 2 days off " )
            #print("Thank You!! ")
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
        elif(bhai==nextday):
            clear()
            banner='figlet RXCEV5.1|lolcat'
            system(banner)
            print("----------Your play time-----------")
            print("30th-1st feb 2021, 02:00 PM- 02:30 PM")
            print("30th-1st feb 2021, 06:00 PM- 06:30 PM")
            print("30th-1st feb 2021, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            #period("Sorry too many people(>20) using hack in same time ")
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
        elif(bhai==night):
            clear()
            print("----------Your play time-----------")
            print("11th Feb 2022,  08:00 PM- 08:30 PM")
            print("12th Feb 2022, 08:00 PM- 08:30 PM")
            print("13th Feb 2022, 08:00 PM- 08:30 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=400
            hero()
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
        else:
            clear()
            banner='figlet RXCE 5.2|lolcat'
            system(banner)
            print("Incorrect Activation Code :")
     
