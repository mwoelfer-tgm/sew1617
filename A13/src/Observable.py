# simple Observable class which gets implemented by the 'Verlag'
# src: http://www.giantflyingsaucer.com/blog/?p=5117
class Observable(object):
    def __init__(self):
        self.observers = []

    def register(self, observer):
        """
        Add an observer to the list of Observed objects
        :param observer: Observer to be added
        :return: None
        """
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        """
        Remove an observer from the list of observed objects
        :param observer: Observer to be removed
        :return: None
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        """
        Remove all observed objects
        :return: None
        """
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        """
        Updates all observed Objects
        :param args: arguments for update
        :param kwargs: keyword arguments for update
        :return:
        """
        for observer in self.observers:
            observer.update(*args, **kwargs)