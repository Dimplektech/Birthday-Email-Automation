
import random
import  pandas
import datetime
import smtplib


# Create connection to send email
my_email = "dimple.temp27@gmail.com"
password = "ijtp nazs bupm prmt"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)

# get Today's date
now = datetime.datetime.now()
birth_day = now.day
birth_month = now.month


print(birth_day)
print(birth_month)

# Read Text file
file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
with open(file_path,"r") as letter_file:
    letter = letter_file.read()

# Convert birthday.csv into csv
data = pandas.read_csv("birthdays.csv")
birthday_list = data.to_dict(orient ="records")

# Check if anyone's birthday today.
for dic in birthday_list:
   # print(type(dic["month"]))
    if dic["month"] == birth_month and dic["day"] == birth_day:

        rec_email = dic["email"]
        updated_letter = letter.replace("[NAME]", dic["name"])
        connection.sendmail(from_addr=my_email,to_addrs= rec_email,msg=f"Subject:Happy Birthday!!\n\n{updated_letter}")
        print("Message has been sent!!")


connection.close()

