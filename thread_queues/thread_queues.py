import queue
import threading
import os


def ist_primzahl(number):
    """
    :param number: The number to be checked if it is prime

    :return: True or False depending if the argument given is a prime number

    """
    for i in range(2, number):
        #If the number can be divided through another number which is not itself or 0 or 1 the method return False
        if number % i == 0:
            return False
    #In any other case it returns True
    return True

class E1(threading.Thread):
    """
    Producer 1 which searches for prime numbers and puts the in the queue
    """
    def __init__(self, queue):
        """
        :param queue: Producer and Consumer "communicate" via the queue, Producer puts data in the queue and the Consumer fetches data from it
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Checks for prime number and puts them into the queue

        :return: void
        """
        number = 0
        while True:
            number += 1
            if(ist_primzahl(number)):
                self.queue.put(number)
            self.queue.join()
            # The thread has to be stopped because a user input is needed
            if number > 100:
                break
class E2(threading.Thread):
    """
    Producer 2 which gets input data from the user and either puts input into the queue or exits the programm
    """
    def __init__(self, queue):
        """
        :param queue: Seperate Queue, which also is there for communication between Producer and Consumer
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Gets User Input and either exits the Programm or puts the input into the queue

        :return: void
        """
        while True:
            eingabe = input("Geben sie entweder eine Zahl welche überprüft werden soll oder 'exit' zum Beenden ")
            if eingabe == 'exit':
                break
            else:
                try:
                    eingabe = int(eingabe)
                    break
                except ValueError:
                    raise ValueError("Bitte eine Zahl oder 'exit' angeben!")
                self.queue.put(eingabe)

class V1(threading.Thread):
    """
    Consumer 1 which gets data from the queue and then puts it out to the console and writes it into a file
    """
    def __init__(self, queue):
        """
        :param queue: Producer puts data into the queue, and Consumer fetches data from it
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Get data from queue, put it out to the console and write it into the file

        :return: void
        """
        while True:
            number = self.queue.get()
            print("Empfänger empfing Zahl: %d" % number)
            f = open('file.txt', 'a')
            f.write(str(number)+"\n")
            f.close()
            self.queue.task_done()
            #The thread has to be stopped because a user input is needed
            if number > 100:
                break

class V2(threading.Thread):
    """
    Consumer 2 which gets data from the Queue and checks if it was a prime number
    """
    def __init__(self, queue):
        """
        :param queue: Fetch data from the queue
        """
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        Fetch data from queue and check if it is a prime number

        :return: void
        """
        while True:
            #If the Producer got terminated, this Thread should get terminated too
            #Not sure if works, but in theory it should
            if not t3.is_alive():
                print("Producer was terminated")
                break
            number = self.queue.get()
            if ist_primzahl(number):
                print("Die Zahl %d ist eine Primzahl" % number)
            else:
                print("Die Zahl %d ist keine Primzahl" % number)


if __name__ == '__main__':
    #Only there if the program gets tested more than once to "clear" the file
    #os.remove("file.txt")
    #Instanciate queue for prime numbers
    queue1 = queue.Queue()
    #Instanciate Producer and Consumer 1, start them and wait for them to finish
    t1 = E1(queue1)
    t2 = V1(queue1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    #Instanciate queue for user input
    queue2 = queue.Queue()
    #Instanciate Producer and Consumer2, start them and wait for them to finish
    t3 = E2(queue2)
    t4 = V2(queue2)
    t3.start()
    t4.start()
    t3.join()
    t4.join()