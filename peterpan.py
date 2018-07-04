
import socket
import  colorama
import os
import threading
from colorama   import  init, Fore, Back, Style
import time

#lock = threading.Lock()
n_in_oneThread = 2
MAX_PORT_RANGE = 65536

# HOST SCANNING FUNCTIONS

class ThreadScanHosts(threading.Thread):
        def __init__(self,st,en,IP):
            threading.Thread.__init__(self)
            self.st = st
            self.en = en
            self.NET = IP
            self.IPS = []
            self.HOSTS = []
        
        def run(self):
            ph = hostip_scanner(self.st,self.en,self.NET)
            self.IPS = ph[0]
            self.HOSTS = ph[1]

        def get_ports(self):
            r =self.IPS
            return r
        
        def get_hosts(self):
            r =self.HOSTS
            return r

def get_host_name(IP):
    socket.setdefaulttimeout(750)
    
    try:
        
        hostname= socket.gethostbyaddr(IP)
        if hostname=="":
            #print("Nameless")
            return "Nameless"
        else:
            #print(str(hostname[0]))
            return hostname[0]

    except Exception as e:
        #print("Not-Found")
        return "Not Found"

def get_host_status(IP,timeout):
    response = os.popen("ping -n 1 "+ str(IP) + " -w " + str(timeout))
    dead_port_flag=0
        
    for k in response:
        if k.find("TTL")>0:
            #print( Fore.GREEN + str(IP) + "\t--> LIVE",end="")
            return  Fore.GREEN + str(IP) + "\t--> LIVE"
            dead_port_flag=1
            break                   

    if dead_port_flag==0:
        #print( Fore.RED + str(IP) + "\t--> DEAD",end="")
        return  Fore.RED+str(IP) + "\t--> DEAD"

def hostip_scanner(start,end,IP_3_digit):
    NET=IP_3_digit
    PORT_STATUS =[]
    HOST_NAMES = []
    
    for i in range(start,end):

        PORT_STATUS.append(get_host_status(NET+str(i),1000))
        #print("\t",end="")
        HOST_NAMES.append(get_host_name(NET+str(i)))
    return [PORT_STATUS,HOST_NAMES]
    
def defrag_ip_for_thread(st1,en1,n_in_oneThread):        
    
    total_ip =en1-st1
    total_thread = round((total_ip / n_in_oneThread)+1) # n_in_oneThread:number of ip handled by one thread
    threads = []

    print("Total threaded scanner: " + str(total_thread),end="\n")

    try:
        for i in range(total_thread):
            en = st1 + n_in_oneThread
            
            if(en > en1):
                en = en1
            #print("BAS: "+st1 + "SON:"+en)
            
            threads.append(ThreadScanHosts(st1,en,"192.168.168."))
            threads[i].start()
            st1 =en
    except Exception as e:
        print("ERROR: Unable to start thread"+ str(e))


    return threads    
    
def printIPs(threads,n_in_oneThread):
    for th in threads:
        th.join()

    for th in threads[0:len(threads)-1]:
        #print(th.getName())
        liste =th.get_ports()
        for i in range(n_in_oneThread):
            print(liste[i])
        #print("\n")

def printIPsWithHosts(threads,n_in_oneThread):
    for th in threads:
        th.join()

    for th in threads[0:len(threads)-1]:
        #print(th.getName())
        liste =th.get_ports()
        liste2 = th.get_hosts()
        for i in range(n_in_oneThread):
            print(liste[i],end="\t")
            print(liste2[i])
        #print("\n")


# PORT SCANNING FUNCTIONS

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(host_ip, delay):

    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes

    # Spawning threads to scan ports
    for i in range(MAX_PORT_RANGE):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)
        threads[i].start()

    # Locking the script until all threads complete
    for i in range(MAX_PORT_RANGE):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(MAX_PORT_RANGE):
        if output[i] ==  'Listening':
            print(Fore.GREEN  + str(i) + ': ' + output[i])


# MENU FUNCTIONS
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
   
    
        
    