import threading
from abc import ABCMeta, abstractmethod
import time
class Stoppable(metaclass=ABCMeta):
    """ A pure abstract class
    """
    @abstractmethod
    def stopping(self):
        """ This method is necessary to stop a thread in a more secure way
        """
        pass
class WatchDog(threading.Thread):
    """
    Class for stopping a ``Stoppable`` thread:
    """
    def __init__(self, stoptime, *threads):
        """
        Initializing our thread.
        :param stoptime: time in seconds to stop the given threads
        :param threads: tuple of threads
        """
        threading.Thread.__init__(self)
        self.stoptime = stoptime
        self.threads = threads
    def run(self):
        """
        wait the given time and stop the given threads
        """
        start = time.time()
        ende = start+self.stoptime
        # wait until end time is reached
        while time.time() < ende:
            # sleep not more than a second
            time.sleep(0.9)
        # stop all threads now!
        for t in self.threads:
            t.stopping()