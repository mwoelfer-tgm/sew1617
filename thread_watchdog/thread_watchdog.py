from watchdog import Stoppable, WatchDog
import threading
import random
import queue
#import tkinter
import time

class Producer(threading.Thread, Stoppable):
    # Producer creates random numbers and puts them into the queue for the consumer to process them
    def __init__(self, queue):
        """
        Initializes every object of Producer

        :param queue: Queue where random number get put in
        """
        threading.Thread.__init__(self)
        self.running = True
        self.queue = queue

    def stopping(self):
        """
        Gets called by watchdog to set self.running to false

        :return: void
        """
        self.running = False

    def run(self):
        """
        Creates random numbers, puts them into the queue and also puts out which number was out into it. If the queue is full this method
        puts out an message!

        :return: void
        """
        #While the Thread wasn't stopped
        while self.running:
            #Create random number
            number = random.randint(0,254)
            #Put number into queue
            self.queue.put(number)
            print("Übergebene Nummer: %d" % number, "Anzahl vorhande Queue Elemente: %d" % self.queue.qsize())
            if self.queue.qsize() == self.queue.maxsize:
                #Special printing so the message is red (Pierre Rieger helped me with this)
                print("\033[91mQUEUE VOLL!!!!!\033[0m")

            #self.queue.join()
            """No sleep time and join because:
               If there was a sleep time then you wouldn't see how the queue always gets fuller and fuller and then more empty and more empty
               This effect is because the Producer and Consumer don't always work equally fast

               If sleeping time was active, the queue would always be either empty all the time or full all the time
            """
            #time.sleep(random.random())
class Consumer(threading.Thread,Stoppable):
    # Consumer takes numbers from the queue and puts them into the console
    def __init__(self, queue):
        """
        Initializes every object of Consumer

        :param queue: Queue where numbers get retrieven from
        """
        threading.Thread.__init__(self)
        self.running = True
        self.queue = queue

    def stopping(self):
        """
        Gets called by watchdog to set self.running to false

        :return: void
        """
        self.running = False

    def run(self):
        """
        This method receives the numbers from the queue and puts them out into the console. Also if the Queue was empty it'd put a message into the console also

        :return: void
        """
        #While the Thread wasn't stopped
        while self.running:
            # Receiver number from queue
            number = self.queue.get()
            print("Erhaltene Nummer: %d" % number, "Anzahl vorhande Queue Elemente: %d" % self.queue.qsize())
            #self.gt.set_rects(self.queue.qsize())
            if self.queue.qsize() == 0:
                # Put out message in blue (Also help from Pierre Rieger)
                print("\033[94mQUEUE LEER!!!!!\033[0m")

            self.queue.task_done()
            #Same reason as above why sleep isn't here
            #time.sleep(random.random())


#Idea was to create a GUI in another seperate Thread which also gets watched by the watchdog, but it didn't quite work out because
#Of the complications with local and global variables and generally Tkinter not working properly in another thread than the main thread!

# class guiThread(threading.Thread,Stoppable):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.__rects = []
#         self.running = True
#
#     def run(self):
#         root = tkinter.Tk()
#         self.canvas = tkinter.Canvas(root)
#         self.canvas.pack()
#         if not self.running:
#             root.quit()
#         root.mainloop()
#
#
#     def set_rects(self,amount):
#         if amount > len(self.__rects):
#             for r in range(len(self.__rects),amount):
#                 self.__rects.append(self.canvas.create_rectangle(r*10, 0, (r * 10) + 10, 10, fill="black", outline=""))
#         elif amount < len(self.__rects):
#             for r in range(amount,len(self.__rects))[::-1]:
#                 self.canvas.delete(self.__rects[r])
#                 self.__rects.pop(r)
#
#     def stopping(self):
#         self.running = False

if __name__ == '__main__':
    # gt = guiThread()
    # gt.start()


    #Declare the run_time
    run_time_in_seconds = 4
    threads = []
    queue = queue.Queue()
    queue.maxsize = 20
    #Create 2 Producer and 3 Consumer
    p1 = Producer(queue)
    c1 = Consumer(queue)
    p2 = Producer(queue)
    c2 = Consumer(queue)
    c3 = Consumer(queue)
    #Add them to the list
    threads.append(p1)
    threads.append(c1)
    threads.append(p2)
    threads.append(c2)
    threads.append(c3)
    #Initialize watchdog object
    w = WatchDog(run_time_in_seconds, *threads)
    w.start()
    #Start and wait for threads to finish
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    w.join()
    # gt.join()