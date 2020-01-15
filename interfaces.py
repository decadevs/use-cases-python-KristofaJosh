# Document 1 use case of an interface in python
# That is define an interface using the abstract base class module
# Add at least 3 entities that can implement the interface in a way that make sense.


from abc import ABC, abstractmethod


class Connectors(ABC):

    @abstractmethod
    def usb_three(self):
        pass

    @abstractmethod
    def usb_two(self):
        pass

    @abstractmethod
    def response(self):
        pass


class Usb(Connectors):
    def __init__(self, type):
        self.supported = ['A', 'B', 'C']
        self.type = type

    def usb_three(self):
        print('supports 3.0')

    def usb_two(self):
        print('supports 2.0')

    def response(self):
        if self.type in self.supported:
            if self.type.lower() == 'a':
                self.usb_two()
            if self.type.lower() == 'b':
                self.usb_two()
                self.usb_three()
            if self.type.lower() == 'c':
                self.usb_two()
                self.usb_three()


class Keyboard(Connectors):
    def usb_three(self):
        print('This keyboard does not support this port')

    def usb_two(self):
        print('connected')

    def response(self, val):
        print(f'letter entered {ord(val)}')


class Mouse(Connectors):
    def usb_three(self):
        print('not supported')

    def usb_two(self):
        print('supported')

    def response(self, r=False, l=False):
        if r:
            print('right button clicked')
        if l:
            print('left button clicked')

t = Usb('B')
t.response()
u = Keyboard()
u.response('R')
v = Mouse()
v.response(False,1)



