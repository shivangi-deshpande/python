"""
Based on recipe at
http://code.activestate.com/recipes/82965-threads-tkinter-and-asynchronous-io/
Created by Jacob Hallen, AB Strakt, Sweden. 2001-10-17
"""
import tkinter
import time
import threading
import random
import queue


class GuiPart:
    def __init__(self, master, queue):
        self.queue = queue

        self.myContainer1 = tkinter.Frame(master)
        self.myContainer1.pack()
        self.button1 = tkinter.Button(self.myContainer1)
        self.button1.configure(text="Link Active", background="red", width=20)
        self.button1.pack(side=tkinter.TOP)

        self.button2 = tkinter.Button(self.myContainer1)
        self.button2.configure(text="Bilge Level High", background="gray", width=20)
        self.button2.pack(side=tkinter.TOP)

        self.button6 = tkinter.Button(self.myContainer1)
        self.button6.configure(text="Temperature=", background="gray", width=20)
        self.button6.pack(side=tkinter.TOP)

    def processIncoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do what it says
                if msg[0] == 0:
                    self.button1["background"] = "red"
                    self.button2["background"] = "gray"
                    self.button6["background"] = "gray"
                else:
                    self.button1["background"] = "green"
                    if msg[1] == 0:
                        self.button2["background"] = "red"
                    else:
                        self.button2["background"] = "green"
                    self.button6["text"] = "Temperature=" + str(msg[2]) + " C"
                    self.button6["background"] = "green"
            except queue.Empty:
                pass


class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """

    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI. We spawn a new thread for the worker.
        """
        self.master = master

        # Create the queue
        self.queue = queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(100, self.periodicCall)

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select()'.
        One important thing to remember is that the thread has to yield
        control.
        """
        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following 2 lines with the real
            # thing.
            time.sleep(2 + 2 * rand.random())
            msg = [rand.randint(0, 1), rand.randint(0, 1), rand.randint(15, 25)]
            self.queue.put(msg)

    def endApplication(self):
        self.running = 0


rand = random.Random()
root = tkinter.Tk()

client = ThreadedClient(root)
root.mainloop()