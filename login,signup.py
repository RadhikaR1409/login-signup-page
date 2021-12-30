
import json
import os
import re

def pasword(password):
    if len(password)>=6 or len(password)<=16:
        if re.findall("[@#$%&*~!^()_+=:;<>?/\|,.]",password):
            if re.findall("[0-9]",password):
                if re.findall("[a-zA-Z]",password):
                    return True
                else:
                    print("password must contain an alphabet:")
                    password=input("enter password again:")
                    pasword(password)
            else:
                print("password must contain atleast one digit:")
                password=input("enter password again:")
                pasword(password)
        else:
            print("password must contain a special character:")
            password=input("enter password again:")
            pasword(password)
    else:
        print("password length must be greater than 6 and less than 16:")
        password=input("enter password again:")
        pasword(password)


def second_pasword(password,password2):
    if password==password2:
        print("password is correct:")
    else:
        print("password does not match.enter the password again:")
        password2=input("enter the password again:")
        second_pasword()

log_sign=input("whethe you want to login or signup:")
file=os.path.exists("usersignin.json")
if file==False:
    if log_sign=="signup":
        name=input("enter username:")
        password=input("enter password:")
        pasword(password)

        password2=input("confirm the password:")
        second_pasword()
        print("congratulatoins",name,"you are signup successfully..")
        print("please enter some more details:>")
        birthdate=input("enter your date of birth:")
        description=input("say something about you:")
        hobbies=input("what is your hobby:")
        gender=input("male or female:")

        lis1=[]
        lis1=[name,password,birthdate,description,hobbies,gender]
        inner_dict={}
        inner_dict["username"]=name
        inner_dict["password"]=password
        inner_dict["DOB"]=birthdate
        inner_dict["description"]=description
        inner_dict["hobby"]=hobbies
        inner_dict["gender"]=gender

        main_list=[]
        main_list.append(inner_dict) 

        with open("usersignin.json","a") as f:
            json.dump(main_list,f,indent=2)

    else:
        login_id=input("enter username:")
        password=input("enter pssword:")
        print("this username doesn't exist..")


elif file==True:
    if log_sign=="signup":
        user_name=input("enter your name:")
        open_file=open("usersignin.json","r")
        read=open_file.read()
        if user_name in read:
            print("this name already exists..","\n","use another username:")
        else:
            pasword1=input("enter your password:")
            pasword(pasword1)
            password3=input("confirm password:")
            if pasword1==password3:
                print("you are signed in successfully..")
                print("please enter some more details:>")
                birthdate=input("enter your date of birth:")
                description=input("say something about you:")
                hobbies=input("what is your hobby:")
                gender=input("male or female:")

                lis1=[]
                lis1=[user_name,pasword1,birthdate,description,hobbies,gender]
                inner_dict={}
                inner_dict["username"]=user_name
                inner_dict["password"]=pasword1
                inner_dict["DOB"]=birthdate
                inner_dict["description"]=description
                inner_dict["hobby"]=hobbies
                inner_dict["gender"]=gender

                main_list=[]
                main_list.append(inner_dict) 

                with open("usersignin.json","r") as f:
                    data=json.load(f)
                    data.append(main_list)
                    with open("usersignin.json","w") as fb:
                        json.dump(data,fb,indent=2)

            else:
                print("user id or password is wrong.")


    elif log_sign=="login":
        login_id=input("enter username:")
        pswrd=input("enter password:")
        with open("usersignin.json",'r') as fn:
            data=json.load(fn)
            for i in data:
                if i["username"]==login_id:
                    print("you are logged in successfully..")
                else:
                    print("invalid password or id")
                    break


else:
    print("please select valid response either login or sign up:")









