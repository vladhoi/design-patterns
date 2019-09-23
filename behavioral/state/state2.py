from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def do_this(self):
        pass


class StartState(State):

    def do_this(self):
        print("TV is Switching ON...")


class StopState(State):

    def do_this(self):
        print("TV is Switching OFF...")


class TVContext(State):

    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def do_this(self):
        self.state.do_this()


context = TVContext()
context.get_state()

start = StartState()
stop = StopState()

context.set_state(stop)
context.do_this()
