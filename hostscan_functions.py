
import  os
import  socket
import  colorama
import  threading

from    colorama    import init, Fore, Back, Style

n_in_oneThread = 2
MAX_PORT_RANGE = 65536

#  H O S T   S C A N N I N G   F U N C T I  O N S  #

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
    
    for i in range(start,end+1):

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

    for th in threads[0:(len(threads))]:
        #print(th.getName())
        liste =th.get_ports()
        liste2 = th.get_hosts()
        for i in range(n_in_oneThread):
            try:
                print(liste[i],end="\t")
                print(liste2[i])
            except:
                pass
        #print("\n")