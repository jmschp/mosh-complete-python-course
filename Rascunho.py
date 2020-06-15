def print_formatted(number):
    for index in range(1, number + 1):
        decimal = str(index)
        octal = oct(index)
        hexadecimal = hex(index)
        binary = bin(index)
        space = len(bin(number)[2:])
        print("{} {} {} {}".format(decimal.rjust(space," "), octal[2:].rjust(space," "), hexadecimal[2:].upper().rjust(space," "), binary[2:].rjust(space," ")))


n = 17
print(bin(n))
print(len(bin(n)))
print_formatted(n)


#   1  1  1  1
#   2  2  2 10


# n = 17
# spacing = len(bin(n)[2:])

# for i in range(1,n+1):
#     print(str(i).rjust(spacing, ' '),oct(i)[2:].rjust(spacing, ' '),hex(i)[2:].upper().rjust(spacing, ' '),bin(i)[2:].rjust(spacing, ' '))

# def fun(N):
#     width = len(bin(N)) - 2
#     for i in range(1,N+1):
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width))

# n = 2
# fun(n)

# index = 2
# decimal = index
# octal = oct(index)
# hexadecimal = hex(index)
# binary = bin(index)
# print(type(decimal))
# print(type(octal))
# print(type(hexadecimal))
# print(type(binary))