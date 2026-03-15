class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


init_PIN_code, init_balance, age = input().split(", ")
init_balance = int(init_balance)
age = int(age)

while True:
    command = input()
    if command == "End":
        break

    transfer = command.split("#")
    if transfer[0] == "Send Money":
        money = int(transfer[1])
        PIN_code = transfer[2]

        if money > init_balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if PIN_code != init_PIN_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {(init_balance - money):.2f} money left in the bank account")

    elif transfer[0] == "Receive Money":
        money = int(transfer[1])
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        print(f"{(money / 2):.2f} money went straight into the bank account")
