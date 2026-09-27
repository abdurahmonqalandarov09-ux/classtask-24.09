# test 1
# 
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         print(f"{self.name} makes sound")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         print(f"{self.name}: Woof")

# class Cat(Animal):
#     def sound(self):
#         print(f"{self.name}: Meow")

# class Bird(Animal):
#     def sound(self):
#         print(f"{self.name}: Tweet")



# dog = Dog("Rex")
# cat = Cat("Momo")
# bird = Bird("Kesha")

# animals = [dog, cat, bird]

# for i in animals:
#     i.sound()


# test 2

# from cmath import *
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self, r):
#         print("Circle:", pi * (r**2))

# class Rectangle(Shape):
#     def area(self, w, h):
#         print("Rectangle:", w*h)

# class Square(Shape):
#     def area(self, s):
#         print("Square:", s**2)

# circle = Circle()
# rectangle = Rectangle()
# square = Square()

# circle.area(5)
# rectangle.area(4,5)
# square.area(3)



# test 3

# class EmailSender:
#     def send(self, message):
#         print(f"Email: {message}")

# class SMSSender:
#     def send(self, message):
#         print(f"SMS: {message}")

# class TelegramSender:
#     def send(self, message):
#         print(f"Telegram: {message}")

# def notify(sender, message):
#     print(sender.send(message))

# message = input()

# email = EmailSender()
# sms = SMSSender()
# telegram = TelegramSender()

# notify(email,message)
# notify(sms,message)
# notify(telegram,message)


# test 4

# from abc import *
# class Notification(ABC):
#     @abstractclassmethod
#     def send(self, message, recipient):
#         self.message = message
#         self.recipent = recipient
#         pass

# class EmailNotification(Notification):
#     def __init__(self):
#         super().__init__()
#     def send(self, message, recipient):
#         self.message = message
#         self.recipent = recipient
#         print(f"Send email to {self.recipent}: {self.message}")

# class SMSNotification(Notification):
#     def __init__(self):
#         super().__init__()
#     def send(self, message, recipient):
#             self.message = message
#             self.recipent = recipient
#             print(f"Send SMS to {self.recipent}: {self.message}")


# email = EmailNotification()
# sms = SMSNotification()

# email.send("Hello", "user@mail.com")
# sms.send("Hello", "+992900001122")


# test 5

# class Calculator:
#     def add(self, *numbers):
#         if len(numbers) >= 2 and len(numbers) <= 4:
#             return sum(numbers)
#         return "Invalid number of arguments"

# test = [
#     (5,),
#     (5, 10),
#     (1, 2, 3),
#     (1, 2, 3, 4),
#     (1, 2, 3, 4, 5)
#     ]


# c = Calculator()

# for numbers in test:
#     print(c.add(*numbers))


# test 6
# from abc import ABC, abstractclassmethod
# class PaymentMethod(ABC):
#     @abstractclassmethod
#     def pay(self, amount):
#         pass

#     @abstractclassmethod
#     def refund(self, amount):
#         pass


# class CardPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             return f"Card payment: {amount}"
#         return "Invalid amount"
#     def refund(self, amount):
#         if amount > 0:
#             return f"Card refund: {amount}"
#         return  "Invalid amount"

# class CashPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             return f"Cash payment: {amount}"
#         return "Invalid amount"
#     def refund(self, amount):
#         if amount > 0:
#             return f"Cash refund: {amount}"
#         return f"Invalid amount" 

# class CryptoPayment(PaymentMethod):
#     def pay(self, amount):
#         if amount > 0:
#             return f"Cryptopayment: {amount}"
#         return "Invalid amount"
#     def refund(self, amount):
#         if amount > 0:
#             return f"Crypto refund: {amount}"
#         return "Invalid amount"

# payment = input()
# method, amount = payment.split()
# amount = int(amount)

# match method:
#     case "card":
#         method = CardPayment()
#     case "cash":
#         method = CashPayment()
#     case "crypto":
#         method = PaymentMethod()

# def process_payment(method, amount):
#     return f"{method}: {amount}"


# pay = process_payment("card", 250)
# pay1 = process_payment("cash", 100)
# pay2 = process_payment("crypto", 75)

# print(pay)
# print(pay1)
# print(pay2)



# test 7

# from abc import ABC, abstractclassmethod

# class Exporter(ABC):
#     @classmethod
#     def export(self, data):
#         pass

# class CSVEexporter(Exporter):
#     def export(self, data):
        