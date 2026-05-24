import smtplib
import datetime as dt
import pandas,random

# Email credentials configuration placeholders
my_mail = "sarthakwrkonly@gmail.com"
password = ""

# --- Date Retrieval ---
# Fetch the current local system timestamp to match against birthday records
now = dt.datetime.now()
current_month = now.month
current_day = now.weekday()

# Paths to the text templates for generating randomized birthday wishes
list_of_location_of_letters = [r"C:\sarthak\100-Projects-of-Python\Day-32-Send-Mail-SMTP\Automated-Birthday-Wisher-Project\letter_templates\letter_1.txt",
                               r"C:\sarthak\100-Projects-of-Python\Day-32-Send-Mail-SMTP\Automated-Birthday-Wisher-Project\letter_templates\letter_2 (1).txt",
                               r"C:\sarthak\100-Projects-of-Python\Day-32-Send-Mail-SMTP\Automated-Birthday-Wisher-Project\letter_templates\letter_3 (1).txt"
                               ]

def write_a_letter(birthday_person_name,letter=random.choice(list_of_location_of_letters)):
    """Opens a letter template, swaps the [NAME] placeholder with the recipient's name, and returns the message."""
    with open(letter) as data_file:
        data = data_file.read()

    # Perform a string replacement on the target placeholder key
    letter_with_name = data.replace("[NAME]",birthday_person_name) 
    return letter_with_name       

# --- CSV Data Processing ---
# Load the birthdays database into a Pandas DataFrame and convert the rows to a list of dicts
csv_birthday_data = r"C:\sarthak\100-Projects-of-Python\Day-32-Send-Mail-SMTP\Automated-Birthday-Wisher-Project\birthdays.csv"
birthday_data_df = pandas.read_csv(csv_birthday_data)
list_of_dict_of_data = birthday_data_df.to_dict(orient="records")

# --- Birthday Match Validation and Mailing ---
# Iterate over each database entry to see if anyone has a birthday matching the current date
for num in range(0,len(list_of_dict_of_data)):
    if list_of_dict_of_data[num]["month"] == current_month and list_of_dict_of_data[num]["day"]==current_day:
        its_a_birthday = list_of_dict_of_data[num]
        
        # Build the custom greeting letter using the template selector function
        birthday_letter = write_a_letter(birthday_person_name=its_a_birthday["name"])
        
        # Connect to Gmail's SMTP port, secure the pipeline, log in, and dispatch the mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # Encrypt the connection stream using Transport Layer Security
            connection.login(user=my_mail,password=password)
            connection.sendmail(from_addr=my_mail,to_addrs=its_a_birthday["email"],
                                msg=f"Subject:Happy Birthday {its_a_birthday['name']} \n\n{birthday_letter}")