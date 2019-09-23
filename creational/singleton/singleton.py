class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(f'Object s {s} is created')

s1 = Singleton()
print(f'Object s1 {s1} is created')
