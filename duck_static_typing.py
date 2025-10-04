# Duck typing in python objects are judged by their behaviour, not their type.
# Static typing in python objects are judged by their declared type, not just by behaviour.

# def add(a:int,b:int) -> int:
#     return a+b
# print(add(10,20))

class Creditcard():
    def pay(self,amount):
        print(F"Paid :{amount} using Credit card")

class Paypal():
    def pay(self,amount):
        print(F"Paid :{amount} using paypal")

def process_payment(payment_method,amount):
    if isinstance(payment_method,(Creditcard)):
        raise TypeError("Invailid payment method")
    payment_method.pay(amount)

cc=Creditcard()
pp=Paypal()
process_payment(pp,400)
process_payment(cc,700)
