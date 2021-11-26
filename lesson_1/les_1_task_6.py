starting = int(input("How many km does he ran first day?"))
aim = int(input("Please enter the required distance in km"))
day = 1
while starting < aim:
    starting = starting * 1.1
    day = day + 1
print(day)

