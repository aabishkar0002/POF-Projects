# #--------------------Age Calculator--------------------------
# import datetime as d

# birth_year = int(input("Enter the year you were born => "))
# birth_month = int(input("Enter the month you were born => "))
# birth_day = int(input("Enter the day you were born => "))

# current_year  = d.datetime.now().year
# current_month = d.datetime.now().month
# current_day =  d.datetime.now().day

# calculate_year = current_year - birth_year
# calculate_month = current_month - birth_month
# calculate_day = current_day - birth_day

# print(f"=> You are {calculate_year} years, {calculate_month} months and {calculate_day} days old!")


#---------------------------Exam Counter---------------------------

import datetime as d

set_year = int(input("Enter Exam year : "))
set_month = int(input("Enter Exam month : "))
set_day = int(input("Enter Exam day : "))


set_Exam_date =  d.date(set_year,set_month,set_day)
print(f"Your Exam date: {set_Exam_date}")

#---------------------count down----------------

current_date = d.datetime.now()

remaining_year = current_date.year - set_year
remaining_months = current_date.month - set_month
remaining_days = current_date.day - set_day

#----------------Time Remaining-------------------------------------
print("...Remaining...\n")
print(f"Years{remaining_year} || Months:{abs(remaining_months)} || Days:{remaining_days}")