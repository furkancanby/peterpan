
import  socket
import  colorama
import  threading

from    colorama            import init, Fore, Back, Style



MAX_PORT_RANGE = 65536

#  P O R T   S C A N N I N G   F U N C  T I O N S  #

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
