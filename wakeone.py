from wakeonlan import send_magic_packet
from secrets import MAC
import sys, getopt

if len(sys.argv) <= 1:
    exit()

class Main:
    def sendPacket(self):
        host = MAC[int(sys.argv[1])]
        send_magic_packet(host)
        return

app = Main()
app.sendPacket()