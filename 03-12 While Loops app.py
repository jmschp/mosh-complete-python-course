# 12 - While Loops

number = 100
while number > 0:
    print(number)
    number = number // 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
