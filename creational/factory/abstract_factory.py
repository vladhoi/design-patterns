from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NonVegPizza(metaclass=ABCMeta):

    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):

    def prepare(self):
        print(f"Prepare {type(self).__name__}")


class ChickenPizza(NonVegPizza):

    def serve(self, VegPizza):
        print(f"{type(self).__name__} is served with Chicken \
              on {type(VegPizza).__name__}")


class MexicanVegPizza(VegPizza):

    def prepare(self):
        print(f"Prepare {type(self).__name__}")


class HamPizza(NonVegPizza):

    def serve(self, VegPizza):
        print(f"{type(self).__name__} is served with Ham \
              on {type(VegPizza).__name__}")


class PizzaStore:

    def __init__(self):
        pass

    def make_pizzas(self):

        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


pizza = PizzaStore()
pizza.make_pizzas()
