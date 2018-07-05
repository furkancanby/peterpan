import  sys, time
import  threading
import  colorama

from    socket      import *
from    colorama    import init, Fore, Back, Style

BUFSIZE = 1024000

def usage():
    pass

def client():
    """
    #FOR INDEPENDENT USING

    if len(sys.argv)>4:
        ip = sys.argv[2]
        port=sys.argv[3]
        duration = sys.argv[4]
    else:
        usage()
        sys.exit()
    """
    ip      = input("Enter the IP adress: ")
    port    = input("Port: ")
    duration= input("Test duration: ")

    testdata = 'x' * (BUFSIZE-1) + '\n'
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)

    t2 = time.time()
    s.connect((ip, int(port)))
    t3 = time.time()
    i = 0

   
    tf_count = 0
    print()
    #count =None
    counted = 0

    t_time=time.time()
    sure=time.time()
    while 1:
        suan = time.time()
        
        if suan- sure >int(duration):
            break

        i = i+1
        #print(count-i," paket kaldı")
        s.send(bytearray(testdata,"utf-8"))
        
        tf_time = time.time()
        if tf_time- t_time > 0.5: 
            cnt = i-tf_count
            print ('Bandwidth:', round((BUFSIZE*cnt*0.001*0.001*8) / (tf_time-t_time), 3),)
            tf_count=i
            t_time = time.time()
        

    #data = s.recv(BUFSIZE)       
    s.shutdown(1)
    t4 = time.time()
    s.recv(BUFSIZE)

    t5 = time.time()

    print(Fore.LIGHTGREEN_EX +"\n\n[*] FINAL AVARAGE RESULTS: \n")
    #print (data.decode())
    print (Fore.LIGHTBLACK_EX + 'Ping:\t\t' + str( round( ((t3-t2)+(t5-t4)/2) *1000 ,2))   + " milisecons" + "(Server Answer)")
    print (Fore.LIGHTMAGENTA_EX + 'Elapsed time:\t'+ str(t4-t3))
    print (Fore.GREEN + 'Bandwidth:\t' + str(round((BUFSIZE*i*0.001*0.001*8) / (t4-t3), 3)),end="")
    print (Fore.GREEN + ' Mbit / sec.')

def server():
    """
    #FOR INDEPENDENT USING

    if len(sys.argv)>2:
        port=sys.argv[2]
    else:
        usage()
        sys.exit()
    """
    port = input ("Enter the port number to use speed test: ")

    testdata = 'x' * (BUFSIZE-1) + '\n'
    

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)
    print ('Server ready...')
    while 1:
        conn, (host, remoteport) = s.accept()
        while 1:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            del data
            
            print("SV-DONGU")
        conn.send(bytearray(testdata,"utf-8"))
        conn.close()
        print ('Done with', host, 'port', remoteport)

if __name__=="__main__":
    

    if len(sys.argv)>1:
        if sys.argv[1] =="-s" or sys.argv[1] =="--server":
            server()
        elif sys.argv[1] =="-c" or sys.argv[1] =="--client":
            client()
        else:
            usage()
        
    