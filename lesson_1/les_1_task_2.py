print("Please enter any seconds quantity")
seconds = int(input())
if seconds > 0:
    minutes = seconds//60%60
    hours = seconds//60//60
    seconds1 = seconds%60%60%60
    if hours <10:
        hours = str(0) + str(hours)
    else:
        hours = hours
    if minutes < 10:
        minutes = str(0) + str(minutes)
    else:
        minutes = minutes
    if seconds1 < 10:
        seconds1 = str(0) + str(seconds1)
    else:
        seconds1 = seconds1

    print(f"{hours}:{minutes}:{seconds1}")
else:
    print("You wrote a negative number")


