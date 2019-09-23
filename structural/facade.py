class EventManager(object):

    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier(object):

    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def _is_avaliable(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def book_hotel(self):
        if self._is_avaliable():
            print("Registered the Booking\n\n")


class Florist(object):

    def __init__(self):
        print("Flower Decorations for the Event? --")

    def set_flower_requirements(self):
        print("Carnations, Roses and Roses would be used as Decorations\n\n")


class Caterer(object):

    def __init__(self):
        print("Food Arrangements for the Event --")

    def set_cuisine(self):
        print("Chinese and Continental Cuisine to be served\n\n")


class Musician(object):

    def __init__(self):
        print("Musician Arrangements for the Marriage --")

    def set_music_type(self):
        print("Jazz and Classical will be played\n\n")


class You(object):

    def __init__(self):
        print("You:: Whoa! Marrige Arrangements??!!!")

    def ask_event_manager(self):
        print("You:: Let's contanct the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done!")


you = You()
you.ask_event_manager()
