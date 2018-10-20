import psutil
from time import sleep
from os import system
class Network:
    def __init__(self):
        self.Data = psutil.net_io_counters()
        self.bytes_sent = self.Data.bytes_sent
        self.bytes_recv = self.Data.bytes_recv
        self.packets_sent = self.Data.packets_sent
        self.packets_recv = self.Data.packets_recv
        self.errin = self.Data.errin
        self.errout = self.Data.errout
        self.dropin = self.Data.dropin
        self.dropout = self.Data.dropout
    def show(self):

        showData = None
        while True:
             showData = psutil.net_io_counters()
             system("clear")
             print("Byte Sent = ",showData.bytes_sent,", Byte Recieved = ",showData.bytes_recv,", Packet Sent = ",showData.packets_sent,", Packet Recieved = ",showData.packets_recv)
             sleep(1)
        self.bytes_sent = showData.bytes_sent
        self.bytes_recv = showData.bytes_recv
        self.packets_sent = showData.packets_sent
        self.packets_recv = showData.packets_recv
        self.errin = showData.errin
        self.errout = showData.errout
        self.dropin = showData.dropin
        self.dropout = showData.dropout

    def showAll(self):
        showData = None
        while True:
            system("clear")
            showData = psutil.net_io_counters()
            print("Byte Sent = ", showData.bytes_sent, ", Byte Received = ", showData.bytes_recv, ", Packet Sent = ",showData.packets_sent, ", Packet Received = ", showData.packets_recv)
            print("Errors While Receiving = ", showData.errin, ", Errors While Sending = ", showData.errout)
            print("Incoming packets which were dropped = ", showData.dropin,", Outgoing packets which were dropped = ", showData.dropout)
            sleep(1)

        self.bytes_sent = showData.bytes_sent
        self.bytes_recv = showData.bytes_recv
        self.packets_sent = showData.packets_sent
        self.packets_recv = showData.packets_recv
        self.errin = showData.errin
        self.errout = showData.errout
        self.dropin = showData.dropin
        self.dropout = showData.dropout
        return


n = Network()
print()
n.showAll()



