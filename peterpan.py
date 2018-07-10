
import  os
import  time
import  socket
import  colorama
import  threading

from    hostscan_functions  import *
from    portscan_functions  import *
from    colorama            import init, Fore, Back, Style
from    network_interfaces  import *

n_in_oneThread = 2
MAX_PORT_RANGE = 65536


time.sleep(2)
#  M E N U    F U N C T I O N S  #
def mainMenu():
    print(Fore.RED +"##############################################################")                                                                                                                                                                                                                                
    print(Fore.RED +"                      P E T E R P A N")
    print(Fore.RED +"                       Network Tools")
    print(Fore.RED +"##############################################################")                                                                                                                                                                                                                                
    print(Fore.RED +"                  AUTHOR: FURKANCAN B. Y.    "  )                                                                                                                                                                                           
    print(Fore.RED +"##############################################################\n\n")  
    
    print(Fore.CYAN+"[1] Scan ports")
    print(Fore.CYAN+"[2] Scan hosts")
    print(Fore.CYAN+"[3] Show all network interfaces")

    choose=input(">>: ")

    if choose=="1":
        portMenu()
    elif choose=="2":
        hostMenu()         
    elif choose=="3":
        interfaceMenu()
    else:
        print("[*] Wroong choose.")

def hostMenu():
    print(Fore.CYAN+ """
    [1] Print just ports
    [2] Print ports and hostnames
    """)
    choose=input(">>: ")
    print("Enter the 3 digit of IP (with end comma, 192.168.168.) that will be scanned: \n")
    ip_3digit = input()
    print("Enter IP range XXX:( 192.168.168.XXX) [XXX format --> 1:100] : \n")
    range_4th = input()
    args=range_4th.split(":")
    print(args)
    try:
        _initial_ = int(args[0])
        _ended_   = int(args[1])
    except:
        print("Invalid type format. Type like that : '5-78' ")
        print(_initial_)
        print(_ended_)


    threads=defrag_ip_for_thread(_initial_, _ended_, n_in_oneThread)

    if choose=="1":
        printIPs(threads,n_in_oneThread)

    elif choose=="2":
        printIPsWithHosts(threads,n_in_oneThread)
    backMenu()

def portMenu():
    print(Fore.CYAN+ """
    [1] Scan all ports of any IP
    [2] Compare your ports against target IP
    """)
    choose=input(">>: ")

    if choose=="1":
        ip_num = input("Enter the IP adress that ports will be scanned: \n")
        print("\n[*] All ports will be scanned (1:65536), please wait several seconds...\n")
        open_ports=scan_ports(ip_num, 1)
        for i in open_ports:
            print(Fore.GREEN + str(i)+"\t:" + "LISTENING")

    elif choose=="2":
        target_ip_num = input("Enter the target IP adress that will be compare: \n")
        print("\n[*] All ports will be scanned (1:65536), please wait several seconds...\n")
        compared_list = compare_ports(target_ip_num)

        print(Fore.YELLOW+ "\nCOMMON OPEN PORTS:\n")
        common_ports = sorted(compared_list)
        for i in compared_list:
            print(Fore.GREEN + str(i)+"\t:" + "LISTENING")

    backMenu()

def backMenu():
    while 1:
        c=input("Enter b to back previous menu\n")
        if c =="b":
            break
        else:
            print("Please enter valid command.")
            continue

def speedMenu():
    ch_ = input("Wanna run Server or Client?: ")
    if ch_ == "server" or ch_ == "Server":
        server()
    elif ch_ == "client" or ch_ == "Client":
        client()        
    else:
        print("[*] Wrong Choose!. \n Please type 'server' / 'client' ")
    backMenu()

def interfaceMenu():
    show_network_interfaces()
    backMenu()
    
if __name__=="__main__":
    init()                  # FOR COLORAMA ON WINDOWS PLATFORMS
    init(autoreset=True)    # AUTORESET COLORING

    #port_scanner(10,100,"192.168.168.")
    try:
        while 1:
            os.system("cls")
            mainMenu()

    except KeyboardInterrupt:
        print(Fore.RED+"U have succesfully quit :) \n")   


    #os.system("start cmd /c {command here}")     # Launches in new command prompt, closes when done
    #response = os.popen("ping -n 1 "+ str(IP) + " -w " + str(timeout))
   
    
        
    