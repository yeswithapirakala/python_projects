#online net banking app
#login page->accountno, pin
#balance ,withdrawal, deposit, history,transfer,exit
#balance->show balance
#withdrawal->withdraw amount and update balance
#deposit->deposit amount and update balance
#history->show transaction history
#transfer->transfer amount to another account
#exit->exit from the app
#using dictonary to store data
#using functions to perform operations
#using lock file to store data


#importing module 
import logging as lg
lg.basicConfig(filename="app.log",
          level=lg.DEBUG,
          format="%(asctime)s - %(levelname)s - %(message)s")

##account details
account_details ={123456789:1234}

#user details
user_details={123456789:["hexley",10000,"hexley@gmail.com"],
              987654321:["jeon",20000,"jeon@gmail.com"]}

#transaction details
transaction_details={123456789:[],
                     987654321:[]}

#operations5
#tuple is used because the operations are fixed
operations=(" 1.balance \n",
            "2.withdrawal\n",
            "3.deposit\n",
            "4.history\n",
            "5.transfer\n",
            "6.exit")

#checking user login
def check_login(account_no:int,pin_no:int):
  #check user account number
  if account_no in account_details:
    #pin validation
    if account_details[account_no]==pin_no:
      lg.info("user login successfull")
      return True
    else:
      lg.error("invalid pin number")
      return False
  else:
    lg.warning("invalid account number")
    return False


#balance enquiry
def balance_enquiry(account_no):
  lg.debug("user in balance enquiry page ")
  if account_no in user_details:
    amount = user_details[account_no][1]
    lg.info(f"Balance enquiry successful for account {account_no}, balance: {amount}")
    print(f"Your current balance is {amount}")
  else:
    lg.warning(f"User with account {account_no} not found")
    print("user not found")


#withdrawal
def withdrawal(account_no):
  lg.debug("user in withdrawal page")
  amount=user_details[account_no][1]
  withdrawal_amount=int(input("enter the amount to be withdrawn: "))
  if amount>=withdrawal_amount:
    user_details[account_no][1]-=withdrawal_amount
    lg.info("amount withdrawn successfully")
    print(f"{withdrawal_amount} amount withdrawn successfully and the current balance is {user_details[account_no][1]}")
  else: 
    lg.error("insufficient balance")
    print("insufficient balance")


#deposit
def deposit(account_no):
  lg.debug("user in deposit page")
  deposit_amount=int(input("enter the amount to be deposit: "))
  user_details[account_no][1]+=deposit_amount
  lg.info("amount deposited successfully")
  print(f"{deposit_amount} amount deposited successfully and the current balance is {user_details[account_no][1]}")


#history
def history(account_no:int):
  lg.debug("user in history page")
  print("function development is under processing")
  pass


#transfer
def transfer(account_no):
  lg.debug("user in transfer page")
  transfer_account_no=int(input("enter the account number to be transfered: "))
  transfer_amount=int(input("enter the amount to be transfered: "))
  current_balance=user_details[account_no][1]
  if transfer_account_no in user_details:
    if current_balance>=transfer_amount:
      user_details[account_no][1]-=transfer_amount
      user_details[transfer_account_no][1]+=transfer_amount
      lg.info("amount transfered successfully")
      print(f"{transfer_amount} amount transfered successfully and the current balance is {user_details[account_no][1]}")

    else:
      lg.error("insufficient balance")
      print("insufficient balance")  
  else:
    lg.warning("invalid account number")
    print("invalid account number")

#exit
def exit_fun():
  lg.debug("user in exit page")
  return True
  """print("function development is under processing")"""

#transction update in table
def transaction_update(account_no:int):
  lg.debug("user in transction page")
  print("function development is under processing")
  pass


#check operations
def chose_operation(account_no:int,choice:int):
  val=False
  if choice == 1:
    balance_enquiry(account_no=account_no)
  elif choice == 2:
    withdrawal(account_no=account_no)
  elif choice == 3:
    deposit(account_no=account_no)
  elif choice == 4:
    history(account_no=account_no)
  elif choice == 5:
    transfer(account_no=account_no)
  elif choice == 6:
    val=exit_fun()
  if val:
    return val
  else :
    lg.error("invalid choice")
    print("invalid choice \n please enter a valid choice between 1 to 6")


#main function 
if __name__=="__main__":
  lg.info("Welcome to online inquest banking")
  print("Welcome to online inquest banking")
  account_no=int(input("Please,Enter your account number: "))
  pin_no=int(input("please,Enter your pin number: "))
  lg.info(f"user entered account number {account_no} and pin number {pin_no}")
  while True:
    if check_login(account_no=account_no,pin_no=pin_no):
        #account_no (parameter) = account_no (value) from the function
        print(*operations)
        lg.info(*operations)
        choice=int(input("Enter the operation you want to perform:"))
        exit_fun_val=chose_operation(account_no=account_no,choice=choice)
        if exit_fun_val:
          lg.info("user exited from the application")
          print("Thank you for using our application")
          break
  else:
      lg.info(f"login failed for account number {account_no} and pin number{pin_no}")
      print("invalid account number or pin number")
