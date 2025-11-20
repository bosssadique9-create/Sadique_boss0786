from pathlib import Path
import json
import string
import random

class Bank:
    database = "database.json"
    data = []

    try:
        if Path(database).exists():
            with open(database)as fs:
                data = json.loads(fs.read())
        else:
            print("We have some issue")



    except Exception as err:
        print(f"an occoured {err}")

    @staticmethod
    def __update():
        with open(Bank.database, "w")as fs:
            fs.write(json.dumps(Bank.data))


    def __accountno():
        alpha = random.choices(string.ascii_letters, k=5)
        digits = random.choices(string.digits, k=5)
        id =alpha+digits
        random.shuffle(id)
        return"".join(id)







    def creataccount(self):
        d ={
            "name":input("Tell your name:"),
            "age":int(input("Tell your age:")),
            "email":input("Enter your email:"),
            "phone no":int(input("Tell your phone no :")),
            "pin code":int(input("Tell your pin code 6 digits:")),
            "account no":Bank.__accountno(),
            "balance":0

        }
        print(f"Please note down your account no : {d['account no']}")
        if d["age"] < 18 or len(str(d["pin code"]))!=6:
            print("Check your age and pin code")

        elif len(str(d["phone no"])) !=10:
            print("pls check your phone no")

        else:
            Bank.data.append(d)
            Bank.__update()


    def deposit_money(self):
        accNo = input("Enter your account no:")
        pin = int(input("Enter your pin:"))
        user_data =[i for i in Bank.data if i ["account no"]==accNo and i ["pin code"]==pin]

        if not user_data:
            print("user not found")

        else:
            amount = int(input("How much ammount do you want to diposit "))

            if amount <=0:
                print("your money is less then zero")

            elif amount >20000:
                print("your money is greter then 20k")


            else:
                user_data[0]["balance"]+=amount
                Bank.__update()
                print("your money has been successfully deposited")




    def withdrol_money(self):
        accNo = input("Enter your account no")
        pin = int(input("Enter your pin code:"))
        user_data = [i for i in Bank.data if i ['account no']and i ['pin code']==pin]

        if not user_data:
            print("user not found")

        else:
            amount = int(input("how much money do you want to withdrol"))


            if amount <=0:
                print("Invalid amount , your mony is less then zero")

            elif amount >10000:
                print("your amount is greter then 10k")

            else:
                if user_data[0]['balance'] < amount:
                    print(" in your account Money is requarid in withdrol balance")

                else:
                    user_data[0]['balance']-=amount
                    Bank.__update()
                    print("your mony has been successfully withdrol")





    def details(self):
        ccNo = input("Enter your account no")
        pin = int(input("Enter your pin code:"))
        user_data = [i for i in Bank.data if i ['account no']and i ['pin code']==pin]

        if not user_data:
            print("user not found")

        else:
            print("Your information is........")
            for i in user_data[0]:
                print(f"{i}:{user_data[0][i]}")


                




        







    

user = Bank()
print("press 1 creata an account:")
print("press 2 deposit money:")
print("press 3 for withdrol money:")
print("press 4 for details:")
print("press 5 update details:")
print("press 6 for delating account:")

check = int(input("Enter your choice:-"))
if check == 1:
    user.creataccount()

if check == 2:
    user.deposit_money()

if check == 3:
    user.withdrol_money()

if check == 4:
    user.details()
    