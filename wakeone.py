from wakeonlan import send_magic_packet
from secrets import MAC, BC_ADDR
import sys, getopt

if len(sys.argv) <= 1:
    exit()

class Main:
    def sendPacket(self):
        host = MAC[int(sys.argv[1])]
        #print(host)
        send_magic_packet(host, ip_address=BC_ADDR)
        return

app = Main()
app.sendPacket()