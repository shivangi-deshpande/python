from time import sleep
import threading

class Demo(threading.Thread):
    def __init__(self, tName, tID, tDelay):
        threading.Thread().__init__(self)
        self.tName, self.tID, self.tDelay = tName, tID, tDelay

    def run(self):
        print("Started....")
        self.print_thread(self.tName, self.tID, self.tDelay)
        print("Exiting....")

    def print_thread(self,name, id, delay):
        while True:
            sleep(2)
            for i in range(10):
                if i == 5:
                    break
                    # name.exit()

                else:
                    print(name)


thread1 = Demo("first", 1, 3)
thread2 = Demo("second", 2, 1)
thread3 = Demo("first", 3, 2)




thread1.start()
thread2.start()
thread3.start()
