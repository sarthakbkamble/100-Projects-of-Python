import datetime as dt
import smtplib,random

my_email = "sarthakwrkonly@gmail.com"
password = "sgcg cecm pyaa fwuk"

now =  dt.datetime.now()
weekday = now.weekday()

if weekday ==6:
    with open(r"C:\sarthak\100-Projects-of-Python\Day-32-Send-Mail-SMTP\Motivational-Quote-Mail-Program\quotes.txt") as data_file:
        motivational_quotes = data_file.readlines()
        random_quote = random.choice(motivational_quotes)
        
    with smtplib.SMTP("smtp.gmail.com") as motivational_mail:
        motivational_mail.starttls()
        motivational_mail.login(user=my_email,password=password)
        
        motivational_mail.sendmail(from_addr=my_email,to_addrs="sarthak.kamble@yahoo.com",
                                msg=f"Subject:Sunday Motivational Quote. \n\n{random_quote}")
