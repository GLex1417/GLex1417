my_list = [9, 7, 4, 3, 3, 1]
print(f"Current list is: \n{my_list}")
u_input = int(input("Please enter the number"))

for i in range(len(my_list)):
    if my_list[i] == u_input:
        my_list.insert(i + 1, u_input)
        break
    elif my_list[i] > u_input > my_list[i + 1]:
        my_list.insert(i + 1, u_input)
        break
    elif my_list[0] < u_input:
        my_list.insert(0, u_input)
print(my_list)

