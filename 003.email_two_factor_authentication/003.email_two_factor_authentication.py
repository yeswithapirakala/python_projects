#user input is email and password
#email should be in the form of xyz@domain.com
#password should be atleast 8 characters long
#while login it has to ask two step verificattion for random number if the password is correct
#then it has to print login successful
#otherwise it has to print login failed

#account details:
import random

account_details = {"hexley@gmail.com": "yeswitha1234"}


def login():
  while True:
    email = input("Enter your email: ")
    print()
    if "@" in email and "." in email:
      if email in account_details:
        password = input("Enter your password: ")
        print()
        if len(password) >= 8:
          if password == account_details[email]:
            randomno = random.randint(1000, 9999)
            print(randomno)
            verifyno = int(input("enter the two step verification number: \n"))
            if verifyno == randomno:
              print("login successful\n")
              break
            else:
              print("login failed \n")
          else:
            print("enter the correct password\n")
        else:
          print("login failed \n")
          print("password should be atleast 8 characters long \n")
      else:
        print("user not found \n")
        print("please enter the correct email \n")
    else:
      print("please check the email format \n")


login()
