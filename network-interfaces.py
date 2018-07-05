import 	wmi

def network_interfaces():
	""" return SELECTED NETWORK INTERFACE NAME"""
	c=wmi.WMI()
	qry = "select Name from Win32_NetworkAdapter where NetEnabled=True and NetConnectionStatus=2"
	lst = [o.Name for o in c.query(qry)]
	i=1
	print(Fore.CYAN+"\nSelect a network interface: ")
	for adapter in lst:
		print(Fore.YELLOW+"["+str(i)+"]"+adapter)
		i+=1

	adapter_number=i
	choose=input("\nYour select: ")

	for i in range(1,adapter_number+1):
		if choose == str(i):
			return lst[i-1]