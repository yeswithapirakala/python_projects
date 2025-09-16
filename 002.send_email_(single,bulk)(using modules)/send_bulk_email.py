import send_single_email

#create bulk email sender
def bulkemailsend(emails:list, subject:str, body:str):
    for email in emails:
        #call single email
        send_single_email.singleemailsend(
            to_email=email,
            subject=subject,
            body=body
        )