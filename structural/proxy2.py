from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def _get_account(self):
        self.account = self.card  # Assume card number is account number
        return self.account

    def _has_funds(self):
        print(f"Bank:: Checkin if Account {self._get_account} has funds")
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self._has_funds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False


class DebitCard(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.set_card(card)
        return self.bank.do_pay()


class You:

    def __init__(self):
        print("You:: Let's buy the denim shirt")
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print("You:: Wow! Denim shirt is Mine!")
        else:
            print("You:: I should earn more..")


you = You()
you.make_payment()
