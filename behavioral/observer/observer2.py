from abc import ABCMeta, abstractmethod


class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class NewsPublisher:

    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self):
        return self._subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self._subscribers]

    def notify_subscribers(self):
        for sub in self._subscribers:
            sub.update()

    def add_news(self, news):
        self._latest_news = news

    def get_news(self):
        return "Got news: ", self._latest_news


class SMSSubscriber:

    def __init__(self, publisher):
        self.pulisher = publisher
        self.pulisher.attach(self)

    def update(self):
        print(type(self).__name__, self.pulisher.get_news())


class EmailSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == "__main__":
    news_publisher = NewsPublisher()

    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)

    print(f"\nSubscribers: {news_publisher.subscribers()}")

    news_publisher.add_news("Hello there!")
    news_publisher.notify_subscribers()

    print(f"\nDetached: {type(news_publisher.detach()).__name__}")
    print(f"\nSubscribers: {news_publisher.subscribers()}")

    news_publisher.add_news("My second news!")
    news_publisher.notify_subscribers()
