# n = 5
# arr = [2, 3, 6, 6, 5]
# arr.sort()  # [2, 3, 5, 6, 6]
# print(arr)

# second_mx = arr[0]
# mx = arr[1]


# for i in range(2, n):
#     if arr[i] > mx and arr[i] != mx:
#         second_mx = mx
#         mx = arr[i]
180

# print(second_mx)

Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number % 10
    Reverse = (Reverse * 10) + Reminder
    Number = Number // 10

print("\n Reverse of entered number is = %d" % Reverse)
