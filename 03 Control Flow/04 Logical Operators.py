# 04 Logical Operators
# and
# or
# not

income = 2000
good_credit = True

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

income = 2000
good_credit = True

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

income = 2000
good_credit = True
student = False

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


income = 5000
good_credit = True
student = True

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
