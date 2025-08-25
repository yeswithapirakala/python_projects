import send_single_email
import send_bulk_email


#main function
if __name__ == "__main__":
    print("Welcome to the email sender to python script")
    subject=input("Enter the subject of an email : ")
    body=input("Enter body of an email :")
    print("Select your operation \n 1.Single email sender \n 2.Bulk email sender")
    choice=int(input("Please,Selsect your operation:"))
    if choice == 1:
        email = input("Enter the recivers email : ")
        #function call
        send_single_email.singleemailsend(
            #module name :function name
            to_email= email,
            subject=subject,
            body=body
        )
    elif choice == 2:
        emails=list(map(str,input("Enter the emails seperated bu "," :").strip().split(",")))
        #bulk email sender dunction call
        send_bulk_email.bulkemailsend(
            emails=emails,
            subject=subject,
            body=body
        )
    else:
        print("please select the operation choice")


