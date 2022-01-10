import smtplib
import random
import pandas
with open("quotes.txt") as file:
    quote_l = file.readlines()

quote = quote_l[random.randint(1,102)]
df = pandas.read_csv("receiver.csv")

for i in  range(len(df["name"])):
    to_name = df.at[i, "name"]
    to_email = df.at[i, "email"] 
    to_quote = quote

    #sending mail
    my_email = "120.koshanqari@gmail.com"
    my_password = "thermokapassword"

    connection = smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls() 
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject: Quote of the day\n\n Hi {to_name}, this is Quote of the day \n{to_quote}")
    connection.close()

    print("Email Sent")