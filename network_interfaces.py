import 	wmi
import socket
import  colorama

from    colorama            import init, Fore, Back, Style

def show_network_interfaces():
	""" return SELECTED NETWORK INTERFACE NAME"""
	c=wmi.WMI()
	qry = "select Name from Win32_NetworkAdapter where NetEnabled=True and NetConnectionStatus=2"
	lst = [o.Name for o in c.query(qry)]
	i=1
	print(Fore.CYAN+"\nNetwork interfaces on your machine:")
	for adapter in lst:
		print(Fore.YELLOW+"["+str(i)+"]"+adapter)
		i+=1
	return lst
	
def choose_network_interfaces():
	""" return SELECTED NETWORK INTERFACE NAME"""
	lst=show_network_interfaces()
	adapter_number=len(lst)

	choose=input("\nYour select: ")
	print("\n")
	for i in range(1,adapter_number+1):
		if choose == str(i):
			return lst[i-1]

def get_local_ip():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.connect(("8.8.8.8", 80))
	localIP=(sock.getsockname()[0])
	sock.close()
	return localIP
