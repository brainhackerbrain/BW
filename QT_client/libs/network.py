import socket
import time



def ping_port(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

def scan_port(iplist,port=3389):
	res=[]
	for ip in iplist:
		res.append([ip,port,ping_port(ip,port),int(time.time())])
	return (res)




print (scan_port(['192.168.0.1','192.168.0.2']))
