# Bank management

import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgen(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        nums = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)

        id = alpha + nums + spchar
        random.shuffle(id)

        return "".join(id)

    def createaccount(self):
        info = {
            "name": input("enter your name:- "),
            "age": int(input("enter your age:- ")),
            "email": input("enter your email-id:- "),
            "pin": int(input("enter the pin:- ")),
            "accountNo": Bank.__accountgen(),
            "balance": 0
        }

        if info['age'] < 18 and len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("enter your account number:- ")
        pin = int(input("enter your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found!")
        else:
            amount = int(input("how much you want to deposit:- "))

            if amount > 10000 or amount < 0:
                print("sorry the amount is too much, you can deposit below 10000 and above 0")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully!")

    def withdrawmoney(self):
        accnumber = input("enter your account number:- ")
        pin = int(input("enter your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found!")
        else:
            amount = int(input("how much you want to withdraw:- "))

            if userdata[0]['balance'] < amount:
                print("Insufficient balance")
            else:
                print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully!")

    def showdetails(self):
        accnumber = input("enter your account number:- ")
        pin = int(input("enter your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry,  no data found!")

        else:
            print("your information are \n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("enter your account number:- ")
        pin = int(input("enter your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry,  no data found!")
        else:
            print("you cannot change age, account number, balanace")
            print("Fill the details for change or leave it empty if no change ")

            newdata = {
                "name": input("enter new name or press enter for no change:- "),
                "email": input("enter new email-id or press enter for no change:- "),
                "pin": input("enter new pin or press enter to skip:- ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']

            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]

            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata["age"] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])
                for i in newdata:
                    if newdata[i] != userdata[0][i]:
                        userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")

    def deleteacc(self):
        accnumber = input("enter your account number:- ")
        pin = int(input("enter your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no such data exists")
        else:
            check = input("press y if you actually want to delete your account or press n:- ")

            if check == 'n' or check == 'N':
                print("continue")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account has been deleted successfully")
                Bank.__update()


user = Bank()

print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting the account")

check = int(input("enter your response: "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteacc()
