number = int(input('Enter an positive number'))//10
rest = number % 10
while number > 0:
    if number % 10 > rest:
        rest = number%10
    number = number//10
print(rest)
