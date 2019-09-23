class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Current: ", self, "=> switched to the new state",
                  state.name)
            self.__class__ = state
        else:
            print("Current: ", self, "=> switching to ", state.name,
                  " is not possible")

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ['on']


class On(ComputerState):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ['on']


class Suspend(ComputerState):
    name = "suspend"
    allowed = ['on']


class Computer(object):

    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == "__main__":
    computer = Computer()
    computer.change(On)
    computer.change(Off)
    computer.change(On)
    computer.change(Suspend)
    computer.change(Hibernate)
    computer.change(On)
    computer.change(Off)
