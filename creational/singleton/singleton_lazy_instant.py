class Singleton:
    _instance = None

    def __init__(self):
        if not Singleton._instance:
            print(" __init__ method called..")
        else:
            print(f"Instance already created: {self.get_instance()}")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton()
        return cls._instance


s = Singleton()  # class initialized, but object not created
print(f"Object {Singleton.get_instance()} is created")  # Object gets created
s1 = Singleton()  # instance already created
