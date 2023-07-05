import os
import time
import sys
from colorama import init,Fore

init()

try:
    print("¡USE THIS SCRIPT IN A LINUX SYSTEM!")
    time.sleep(1)
except PermissionError:
    print("You need root!")
    sys.exit()

banner_credits = """
-------------------------------------------------------------------------                
   _____          _          _   _                 _     ____  _  _     |
  / ____|        | |        | | | |               | |   |___ \| || |    |
 | |     ___   __| | ___  __| | | |__  _   _   ___| |__   __) | || |_   |
 | |    / _ \ / _` |/ _ \/ _` | | '_ \| | | | |_  / '_ \ |__ <|__   _|  |
 | |___| (_) | (_| |  __/ (_| | | |_) | |_| |  / /| | | |___) |  | |    |
  \_____\___/ \__,_|\___|\__,_| |_.__/ \__, | /___|_| |_|____/   |_|    |
                                        __/ |                           |
                                       |___/                            |
------------------------------------------------------------------------|                                                                       |
"""
time.sleep(2)
print(Fore.RED+banner_credits)


banner = """

$$\   $$\ $$\      $$\  $$$$$$\  $$$$$$$\$$\     $$\ 
$$$\  $$ |$$$\    $$$ |$$  __$$\ $$  __$$\$$\   $$  |
$$$$\ $$ |$$$$\  $$$$ |$$ /  $$ |$$ |  $$ \$$\ $$  /   
$$ $$\$$ |$$\$$\$$ $$ |$$$$$$$$ |$$$$$$$  |\$$$$  /  
$$ \$$$$ |$$ \$$$  $$ |$$  __$$ |$$  ____/  \$$  /   
$$ |\$$$ |$$ |\$  /$$ |$$ |  $$ |$$ |        $$ |    
$$ | \$$ |$$ | \_/ $$ |$$ |  $$ |$$ |        $$ |    
\__|  \__|\__|     \__|\__|  \__|\__|        \__|                                    

1:  Half-Scan                       11:  OS Detection
2:  TCP Complete Scan               12:  Scan UDP
3:  Service Detection normal        13:  Scan 1000 famous ports
4:  Firewall Detection              14:  Scan unique port
5:  List Scan                       15:  Detailed Scan
6:  Ping scan                       16:  Agressive Scan
7:  XMAX Scan                       17:  Service detection Agressive
8:  Fin Scan                        18:  No ping scan
9:  Null Scan                       19:  TCP Windows Scan
10: IP protocol Scan               20:   SCTP Scan
                                        
0 - Exit
"""
time.sleep(2)
print(Fore.LIGHTGREEN_EX+banner)

def nmap_menu():
    os.system('clear')
    try:
        os.system('python3 nmapy.py')
    except FileNotFoundError:
        sys.exit()

def messaje():
    message_error = "Scan failed :( )"
    print(message_error)
    time.sleep(0.5)
    nmap_menu()


user_option = input(">>>")
if user_option=='0':
    print("Thanks for using my script... :)\nGood Luck! ")
    sys.exit()

elif user_option=='1':
    
    print("Shhhhh")
    ip_victim = input("Enter the target: ")
    print("Scanning... Please be patient")
    try:
         half_scan = os.system('nmap -sS'+ " "+ip_victim)
         input("Press ENTER to continue:")
         nmap_menu()

    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
            print("Conection error")
            nmap_menu()

elif user_option=='2':
    print("TCP Complete Scan? Ok...")
    ip_victim = input("Enter the target: ")
    print("Scanning be patient please :) ")
    try:
        tcp_scan = os.system('nmap -sT'+ " "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='3':
    print("Service normal detection? Ok...")
    ip_victim = input("Enter the target: ")
    try:
        normal_detection = os.system('nmap -sV'+ " "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='4':
    print("Firewall detection? I like that")
    ip_victim = input("Enter the target: ")
    try:
        firewall_detec = os.system('nmap -sA'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='5':
    print("Okay. Trying lo list hosts")
    ip_victim = input("Enter the target: ")
    try:
        sl = os.system('nmap -sL'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='6':
    print("Oh! Ping Scan")
    ip_victim= input("Enter the target: ")
    try:
        ping = os.system('nmap -sn'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='7':
    print("Okay. XMAX Scan!")
    ip_victim = input("Enter the target: ")
    try:
        xmax = os.system('nmap -sX '+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()


elif user_option=='8':
    print("Well...Fin Scan")
    ip_victim = input("Enter the target: ")
    try:
        fn = os.system('nmap -sF'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()


elif user_option=='9':
    print("Ok.Null Scan")
    ip_victim = input("Enter the target: ")
    try:
        ns = os.system('nmap -sN'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='10':
    print("Lets go")
    ip_victim = input("Enter the target: ")
    try:
        ip_scan = os.system('nmap -sO'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except  (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()


elif user_option=='11':
    print("Let's guess the operating system")
    ip_victim = input("Enter the target ")
    try:
        ip_scan = os.system('nmap -O'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except  (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='12':
    print("Let's guess UDP ports")
    ip_victim = input("Enter the target: ")
    try:
        ip_scan = os.system('nmap -sU'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='13':
    print("Interesting option")
    ip_victim = input("Enter the target: ")
    try:
        ports_scan = os.system('nmap --top-ports 1000'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()
elif user_option=='14':
    print("Alright")
    ip_victim = input("Enter the target: ")
    try:
        port = input("Enter the port:  ")
        unique_port = os.system('nmap -p'+" "+port+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='15':
    print("Prepare your screen...")
    ip_victim = input("Enter the target: ")
    try:
        detailed = os.system('nmap -Pn -A -sV'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='16':
    print("Be careful! This type of scan can leave traces in the target!")
    ip_victim = input("Enter the target: ")
    try:
        agressive = os.system('nmap -A'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()

elif user_option=='17':
    print("Be careful! This type of scan can leave traces in the target!")
    ip_victim = input("Enter the target: ")
    try:
        agressive_detailed = os.system('nmap -sV -T5'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()
elif user_option=='18':
    print("Lets try it!")
    ip_victim = input("Enter the target: ")
    try:
        agressive_detailed = os.system('nmap -Pn'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()
elif user_option=='19':
    print("This scan relies on an implementation detail of a minority of systems out on the internet,so you can't alwayes trust it.")
    ip_victim = input("Enter the target: ")
    try:
        windows_scan = os.system('nmap -sW'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()
elif user_option=='20':
    print("Perfect...")
    ip_victim = input("Enter the target: ")
    try:
        windows_scan = os.system('nmap -sY'+" "+ip_victim)
        input("Press ENTER to continue:")
        nmap_menu()
    except (ConnectionError,ConnectionRefusedError,NameError,ValueError):
        messaje()
else:
    print("You have not chose any option!")
    nmap_menu()