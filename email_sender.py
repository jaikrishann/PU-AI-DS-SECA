import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    #receiver mail 
    receiver_mail = input("enter the receiver mail")

    #mail credentials 
    sender_email = "jaikrishan2001@gmail.com"
    password = "yxre ddho mlam afim"

    #login 
    server.login(sender_email,password=password)

    #send mail
    subject = input("enter the subject :- ")
    body = input("Enter the body here :- ")
    message = f"Subject : {subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("maild sent successfully")
except Exception as e:
    print(e)