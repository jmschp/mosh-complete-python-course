# 03 Ternary Operator

age1 = 17
if age1 >= 18:
    print("Eligible")
else:
    print("Not eligible")

# Theres is a different cleaner way to write the same code, and achive the same result.
age2 = 20
message = "Eligible" if age2 >= 18 else "Not eligible"
print(message)
