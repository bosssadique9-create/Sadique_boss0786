from pathlib import Path
import json
import string
import random


class Bank:
    database ="database.json"
    data =[]

    try:
        if Path(database).exists():

            with open(database)as fs:   
                data = json.loads(fs.read())
        else:
            print("we have some issue")

    except Exception as err:
        print(f"an occoure {err}")



    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))        

    def __accountnumber():
        alpha = random.choices(string.ascii_letters , k=4)
        digits = random.choices(string.digits,k=4)
        id = alpha+digits
        random.shuffle(id)
        return"".join(id)
        
    
    
    
    def deposite_money(self):
        accNo = input("Enter your account no")
        pin = int(input("Enter your pin code:"))
        user_data =[i for i in Bank.data if i ['account no']==accNo and i["pin code"] ==pin]
        

        if not user_data:
            print("user not found")
        else:
            amount = int(input("Enter amount to be deposited"))

            if amount <= 0:
                print("Invalid amount")
            elif amount > 10000:
                    print("Greafter than 10000")

            else:
                user_data[0]['blance'] +=amount
                Bank.__update()
                print("Amount creadited ")






   
    def withdrol(self):
        accNo = input("Enter your account no")
        pin = int(input("Enter your pin:"))


        user_data =[i for i in Bank.data if i ['account no']==accNo and i["pin code"] ==pin]
        

        if not user_data:
            print("user not found")
        else:
            amount = int(input("Enter amount to be withdraw"))

            if amount <= 0:
                print("Invalid amount")
            elif amount > 10000:
                print("Greafter than 10000")
            
            else:
                if user_data[0]['blance'] < amount:
                    print("in your account not required  blance for withdrawl")


                else:
                    user_data[0]['blance'] -=amount
                    Bank.__update()
                    print("Amount creadit")             

    def detail(self):
        accNo = input("Enter your account no")
        pin = int(input("Enter your pin:"))
        user_data =[i for i in Bank.data if i ['account no']==accNo and i["pin code"] ==pin]

        if not user_data:
            print("No such for data found")
        else:
            print("your information is..")
            for i in user_data[0]:
                print(f"{i} : {user_data [0] [i]} ")

    

    
    def update_detils(self):
        accNo = input("Enter your account no")
        pin = int(input("Enter your pin:"))
        user_data =[i for i in Bank.data if i ['account no']==accNo and i["pin code"] ==pin]

        if not user_data:
            print("No such for data found")

        else:
            print("YOu cannot change Account number")
            print("Now update your details and skip it if you don't want to update")

            #name,email,phon,pin

        new_data ={
            "Name":input("Tell your name:"),
            "phone no":input("Tell your phone no:"),
            "email":input("Enter your Email:"),
            "pin code":input("Tell your pin code:")

        }
        #Handling the skipped value
        for i in new_data:
            if new_data[i]=="":
                new_data[i]=user_data[0][i]

        for i in new_data:
            if new_data[i] == user_data[0][i]:
                continue
            else:
                if new_data[i] in ["phone no","pin code"]:
                    user_data[0][i] = int(new_data[i])
                else:
                    user_data[0][i] = new_data[i]
                

        Bank.__update()
        print("Data updated")





    def Delate(self):
        accNo = input("Enter your account no")
        pin = int(input("Enter your pin:"))
        user_data = [i for i in Bank.data if i ['account no']== accNo and i["pin code"] == pin]
        

        if not user_data:
            print("No such for data found")

        else:

            for i in Bank.data:
                if i ['account no']== accNo and i ['pin code']==pin:
                    Bank.data.remove(i)
                    Bank.__update()
                    print("Data deleted successfully")
            # check = input("press y acctuly or press n delate your account")

            # if check == "n" or check == "N":
            #     print("bye pass")
                
            # else:
            #     index = Bank.data.index(user_data[0])
            #     Bank.data.pop(index)
            #     print("account delate successfully")
            #     Bank.__update()

        







    def creataccount(self):
        d ={
            "Name":input("Tell your name:"),
            "age":int(input("Tell your age:")),
            "phone no":int(input("Tell your phone no:" )),
            "pin code":int(input("Tell your pin code:")),
            "email":input("Enter your Email :"),
            "account no":Bank.__accountnumber(),
            "blance":0

            

        }
        print("plese note down your account number")
        if d ["age"] < 18 or len(str(d["pin code"]))!=4:
            print("check your pin code and age")
        
        elif len(str(d ["phone no"]))!=10:
            print("check your pin code")

        else:
            Bank.data.append(d)
            Bank.__update()


        

user = Bank()
print("press 1 for creat an account:")
print("press 2 for deposit money:")
print("press 3 for withdrol money:")
print("press 4 for detail :")
print("press 5 for update details:")
print("press for 6 delating account:")

check = int(input("Enter your choice:"))

if check == 1:
    user.creataccount()

if check == 2:
    user.deposite_money()

if check == 3:
        user.withdrol()

if check ==4:
    user.detail()


if check == 5:
    user.update_detils()


if check == 6:
    user.Delate()











