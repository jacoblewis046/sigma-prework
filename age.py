import datetime

current_date = datetime.datetime.now().date()

date = input("Enter the date you were born (DD-MM-YYY): ")
datelist = date.split("-")
dateobj = datetime.date(int(datelist[2]),int(datelist[1]),int(datelist[0]))

difference_in_date = current_date-dateobj

print(f"you are {round(difference_in_date.days/365.25)} years old")
