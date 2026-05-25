import datetime as dt
import smtplib,random

# Sender credentials setup
my_email = "sarthakwrkonly@gmail.com"
password = ""

# --- Date Verification ---
# Retrieve the current date and find the weekday integer (0 = Monday, 6 = Sunday)
now =  dt.datetime.now()
weekday = now.weekday()

# Check if today is Sunday (index 6)
if weekday == 6:
    # Open the local text database of quotes and parse it into a list of lines
    with open(r"C:\sarthak\100-Projects-of-Python\Day-32-Send-Mail-SMTP\Motivational-Quote-Mail-Program\quotes.txt") as data_file:
        motivational_quotes = data_file.readlines()
        # Randomly select a single quote from the list
        random_quote = random.choice(motivational_quotes)
        
    # --- SMTP Connection and Mail Delivery ---
    # Establish a connection to the SMTP server for Gmail
    with smtplib.SMTP("smtp.gmail.com") as motivational_mail:
        motivational_mail.starttls()  # Secure the connection with TLS encryption
        motivational_mail.login(user=my_email, password=password)
        
        # Dispatch the weekly quote to the receiver address with a formatted subject line
        motivational_mail.sendmail(
            from_addr=my_email,
            to_addrs="sarthak.kamble@yahoo.com",
            msg=f"Subject:Sunday Motivational Quote. \n\n{random_quote}"
        )