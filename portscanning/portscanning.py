
from socket import *
from termcolor import colored
from threading import *
import optparse
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET Using Ipv4 and SOck Stream for TCP packets in order to perform connection
socket.setdefaulttimeout(0.1)

def setoption():
    parser = optparse.OptionParser("Program Usage : -H <target host> -p <target port>")
    parser.add_option("-H", dest="targetHost", type="string", help="Specify the target host:")
    parser.add_option("-p", dest="targetPort", type="string", help="Specify target ports seperated by comma")
    options,args = parser.parse_args()
    targetHost = options.targetHost()
    targetPort = str(options.targetPort()).split(",")

    if targetHost == None or targetPort[0] == None:
        print(parser.usage)
        sys.exit(0)
    else:
        print("sCanning")
        
def simpleportscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[!!]Port %d is closed" % (port),"red"))
    else:
        print(colored("[+]Port %d is Open" % (port),"green"))

if __name__ == "__main__":
    for port in range(100):
        simpleportscanner(port)
