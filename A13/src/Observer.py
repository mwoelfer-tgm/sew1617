from abc import ABCMeta, abstractmethod

# simple Observer class to be implemented by the 'Client'
# src: http://www.giantflyingsaucer.com/blog/?p=5117
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass