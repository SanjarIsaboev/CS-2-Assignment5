import pandas as pd

# User_1 csv
panda_user = pd.read_csv("User_1.csv")
user_id = panda_user["ID"]
user_username = panda_user["Username"]
user_psw = panda_user["PSW"]
user_question = panda_user["Question"]
user_answer = panda_user["Answer"]
user_list = {}
for i in range(len(user_id)):
    user_list[user_id[i]] = [user_username[i], user_psw[i], user_question[i], user_answer[i]]
print(user_list)

# USER_INFO_1
panda_info = pd.read_csv("User_info_1.csv")
info_id = panda_info["ID"]
info_name = panda_info["Name"]
info_surname = panda_info["Surname"]
info_age = panda_info["age"]
info_passport = panda_info["passport"]
info_address = panda_info["address"]
info_list = {}
for i in range(len(info_id)):
    info_list[info_id[i]] = [info_name[i], info_surname[i], info_age[i], info_passport[i], info_address[i]]
print(info_list)

print("Welcome!!!")
choosing = int(input("1-Login page. 2-Register page:    "))


def see_records(login_id):
    print("Name,     Surname,    Age,     Passport,    Address")
    print(info_list[login_id])


def change_password(username):
    print("Changing")
    q1 = "Your favourite football team?"
    q2 = "Your liked clothes brand?"
    q3 = "Your height?"
    q4 = "Your weight?"
    q5 = "Your favourite technical brand?"


def login():
    check = True
    counter = 5
    login_id = 0
    while check:
        username = input("Username:  ")
        password = input("Password:  ")
        for i in range(len(user_username)):
            if username == user_username[i] and password == user_psw[i]:
                login_id = user_id[i]
                check = False
                break
        if not check:
            print("Welcome you are in system now!!!")
            checking = True
            while checking:
                do_something = int(input("1-See my records. 2-Change password:  "))
                if do_something == 1:
                    see_records(login_id)
                    checking = False
                elif do_something == 2:
                    change_password(username)
                    checking = False
                else:
                    print("You entered neither 1 nor 2!!!")
        else:
            counter = counter - 1
            print(f"Invalid username or password!!! you have {counter} chance!!!")
            check = True
            if counter == 0:
                register()


def register():
    pass


if choosing == 1:
    login()
elif choosing == 2:
    register()
else:
    print("You entered neither 1 nor 2!!!")
