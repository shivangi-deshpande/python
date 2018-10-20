# import _thread
# import time
#
# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while True:
#       time.sleep(1)
#       count += 1
#       print ("%s: %s" % time.ctime(time.time()))
#
# def print_next( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
#
#
# # Create two threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_next, ("Thread_next", 2, ) )
# except:
#    print ("Error: unable to start thread")
#
# while 1:
#    pass