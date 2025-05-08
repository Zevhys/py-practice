"""
! Category: Easy
Todo: 1. Create a base class named Notification that has a method send_notification() with a message parameter, 2. Implement 3 subclasses of Notification: ‣EmailNotification, ‣SMSNotification, ‣PushNotification, 3. Each subclass must override the send_notification() method with a different implementation that displays the method of sending the notification according to its type, 4. Create a function named send_all_notifications() that takes a list of notifications and a message, then sends the message through all types of notifications in the list.
"""


class Notification:
    def send_notification(self):
        pass


class EmailNotification(Notification):
    def send_notification(self):
        return "email: weekend Promo! 50% discount for all products"


class SMSNotification(Notification):
    def send_notification(self):
        return "sms: weekend Promo! 50% discount for all products"


class PushNotification(Notification):
    def send_notification(self):
        return "push: weekend Promo! 50% discount for all products\n"


def send_all_notifications(notification_objects):
    for notification in notification_objects:
        print(notification.send_notification())


email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

print("send all notification:")
send_all_notifications([email, sms, push])

"""
! Category: Medium
Todo: 1. Create a base class named Payment that has a method process_payment() to process payments. This method must be overridden by the subclasses, 2. Implement 3 subclasses: ‣BankTransferPayment, ‣CreditCardPayment, ‣EwalletPayment, 3. Each subclass must implement the process_payment() method in a different way: ‣BankTransferPayment prints: "Payment via bank transfer has been successfully processed", ‣CreditCardPayment prints: "Payment via credit card has been successfully processed", ‣EwalletPayment prints: "Payment via e-wallet has been successfully processed", 4. Create a function named process_all_payments() that takes a list of payment objects and processes all the payments using the concept of polymorphism.
"""


class Payment:
    def process_payment(self):
        pass


class BankTransferPayment(Payment):
    def process_payment(self):
        return "Payment via bank transfer has been successfully processed"


class CreditCardPayment(Payment):
    def process_payment(self):
        return "Payment via credit card has been successfully processed"


class EwalletPayment(Payment):
    def process_payment(self):
        return "Payment via e-wallet has been successfully processed"


def process_all_payments(payment_objects):
    for payment in payment_objects:
        print(payment.process_payment())


bank = BankTransferPayment()
credit = CreditCardPayment()
ewallet = EwalletPayment()

process_all_payments([bank, credit, ewallet])
