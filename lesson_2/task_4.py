u_input = input("Please enter some text")
my_arr = u_input.split()
i = 1
for item in my_arr:
    if len(item) >10:
        print(i, item[:10])
        i += 1
    else:
        print(i, item)
        i += 1
