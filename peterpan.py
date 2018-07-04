
import  os
import  time
import  socket
import  colorama
import  threading

from    hostscan_functions  import *
from    portscan_functions  import *
from    colorama            import init, Fore, Back, Style

n_in_oneThread = 2
MAX_PORT_RANGE = 65536

#  M E N U    F U N C T I O N S  #
def mainMenu():
    
    print(Fore.CYAN+"[1] Scan ports")
    print(Fore.CYAN+"[2] Scan hosts")
    choose=input(">>: ")

    if choose=="1":
        portMenu()

    elif choose=="2":
        hostMenu()

def hostMenu():
    print(Fore.CYAN+ """
    [1] Print just ports
    [2] Print ports and hostnames
    """)
    choose=input(">>: ")
    threads=defrag_ip_for_thread(10,18,n_in_oneThread)

    if choose=="1":
        printIPs(threads,n_in_oneThread)

    elif choose=="2":
        printIPsWithHosts(threads,n_in_oneThread)

def portMenu():

    threads=defrag_ip_for_thread(10,18,n_in_oneThread)
    ip_num = input("Enter the IP adress that ports will be scanned: \n")
    scan_ports(ip_num, 1)

if __name__=="__main__":
    init()                  # FOR COLORAMA ON WINDOWS PLATFORMS
    init(autoreset=True)    # AUTORESET COLORING

    #port_scanner(10,100,"192.168.168.")
    mainMenu()
    #os.system("start cmd /c {command here}")     # Launches in new command prompt, closes when done
    #response = os.popen("ping -n 1 "+ str(IP) + " -w " + str(timeout))
   
    
        
    