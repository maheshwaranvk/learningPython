#https://drive.google.com/open?id=1h0IwFXjzMDV8UzkYRZmjc4dCVK2i6Ea7&usp=drive_fs
class CreditCardPayment:

    def processPayment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PaypalPayment:
    def processPayment(self, amount):
        print(f"Processing paypal payment of {amount}")

class BankTransferPayment:
    def processPayment(self, amount):
        print(f"Processing bank transfer of {amount}")
        
def makePayment(paymentMethod, amount):
    paymentMethod.processPayment(amount)

if __name__=="__main__":
    makePayment(PaypalPayment(), 3003)
    makePayment(BankTransferPayment(), 1000)
    makePayment(CreditCardPayment(), 4000)