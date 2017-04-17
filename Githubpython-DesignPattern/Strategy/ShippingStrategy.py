from abc import ABCMeta,abstractmethod

class ShippingStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        '''Calculate shipping cost'''