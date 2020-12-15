#import colorama
import time 
from colorama import Fore,Back,Style
import os 
green=Fore.GREEN
red=Fore.RED
form=Style.BRIGHT
banner=""" _           _        _ _           
 (_)         | |      | | |          
  _ _ __  ___| |_ __ _| | | ___ _ __ 
 | | '_ \/ __| __/ _` | | |/ _ \ '__|
 | | | | \__ \ || (_| | | |  __/ |   
 |_|_| |_|___/\__\__,_|_|_|\___|_|   
     
     writer:: kyaw zin ko ko

     """

banner2=""" _______ _                 _        ______             _    _     _             
 |__   __| |               | |      |  ____|           | |  | |   (_)            
    | |  | |__   __ _ _ __ | | __   | |__ ___  _ __    | |  | |___ _ _ __   __ _ 
    | |  | '_ \ / _` | '_ \| |/ /   |  __/ _ \| '__|   | |  | / __| | '_ \ / _` |
    | |  | | | | (_| | | | |   <    | | | (_) | |      | |__| \__ \ | | | | (_| |
    |_|  |_| |_|\__,_|_| |_|_|\_\   |_|  \___/|_|       \____/|___/_|_| |_|\__, |
                                                                            __/ |
                                                                           |___/ """

choose=input("""Enter your choice
	            1.install
	            2.exit:: """)
if choose==1:
    os.system("clear")
    time.sleep(3)
    print(green+form+banner)
    time.sleep(2)
    os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -")
    os.system("sudo apt-get install apt-transport-https")
    os.system("""echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list""")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install sublime-text")
    print(red+"Finish installing of sublime-text")
    print(red+"Now simply type subl to lunch sublime-text")
if choose==2:
	print(banner2)
	time.sleep(3)
	os.system("exit")

