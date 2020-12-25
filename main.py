from wakeonlan import send_magic_packet
from secrets import MAC, NAMES, BC_ADDR

class stupidity:
    def Wake(self, sel):
        send_magic_packet(MAC[sel], ip_address = BC_ADDR)
    
    def PrintOptions(self):
        print("Select computer to wake up")
        for x in range(len(MAC)):
            index = x + 1
            print(str(index) + ": " + NAMES[x])
        sel = input("Selection: ")
        output = int(sel) - 1
        #print(output)
        return output



app = stupidity()
selection = app.PrintOptions()
app.Wake(selection)