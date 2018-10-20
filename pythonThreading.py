# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.ID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, self.counter, 5)
#       print ("Exiting " + self.name)
#
# def print_time(threadName, delay, counter):
#    while counter:
#       if exitFlag:
#         pass
#         # threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("Exiting Main Thread")


import threading
from time import sleep


class Demo(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.delay = delay

    def run(self):
        # self.print_data(self.threadName)
        i = 0
        while True:
            print(i, " ")
            sleep(self.delay)
            i += 1
            if i == 7:
                break

    def print_data(self, name):
        i = 0
        while True:
            print(i, " ", name)
            sleep(2)
            i += 1
            if i == 7:
                break


t1 = Demo("first", 1)

t2 = Demo("second", 2)

t1.start()
t2.start()
t1.join()
t2.join()
