import os
import sys
import cowsay
from time import sleep as timeout
from core.starkmcore import *

def menu():

    print(""" 
	 ..######..########....###....########..##....##
	 .##....##....##......##.##...##.....##.##...##.
	 .##..........##.....##...##..##.....##.##..##..
	 ..######.....##....##.....##.########..#####...
	 .......##....##....#########.##...##...##..##..
	 .##....##....##....##.....##.##....##..##...##.
	 ..######.....##....##.....##.##.....##.##....##

>>CREATED BY:ANIKETSTARK
>>SUBSCRIBE CHANNEL:HTTPS://YOUTUBE.COM/C/ANIKETSTARK

>>THIS IS VIDEO BETA VERSION<<
>>>ONLY FOR TERMUX<<<

===============================================
1. FACEBOOK HACK
2. INSTAGRAM HACK
3. LAZYMUX
4. RED_HAWK
5. SQL INJECTION
6. WEEMAN
7. SQL WEBSITE SCANNER
================================================
8. EXIT
""")

loop = True

while loop:
    menu()
    stark = raw_input("stark > ")
    
    if stark == "1":
          Facebookhack()
    elif stark == "2":
          Instagramgack()
    elif stark == "3":
          Lazymux()
    elif stark == "4":
    	  Redhawk()
    elif stark == "5":
          Sqli()
    elif stark == "6":
    	  Weeman()
    elif stark == "7":
    	   Sqlwebsitescanner()
    elif stark == "8":
    	   sys.exit()
    elif stark == "0":
          restartprogram()
    else:
		  print "\nERROR: Wrong Command Bro !"
		  timeout(2)
		  restartprogram()