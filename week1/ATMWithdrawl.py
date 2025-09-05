expectedAmount = int(input("Enter the amount you want to withdraw: "))
if (expectedAmount % 100 == 0):
    print("Please collect your cash")
else:
    print("Please enter the amount in multiples of 100")