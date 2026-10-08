balance = float(input("enter the balance: "))
amount = float(input("enter the amount to withdraw: "))
account_type = input("enter account type (savings/current): ")
transaction_type = input("enter transaction type (withdrawal/deposit): ")

if amount <= 0:
    print("not allowed")

elif transaction_type == "deposit":
    balance = balance + amount
    print("balance:")

elif transaction_type == "withdraw":
    if amount > balance:
        print("transaction not allowed")
    elif account_type == "savings" and balance < 1000:
        print("transaction not allowed")
    elif account_type == "current" and balance < 0:
        print("not allowed")
    else:
       # print("transaction allowed")
       balance = balance - amount
    print("new balance:", balance)