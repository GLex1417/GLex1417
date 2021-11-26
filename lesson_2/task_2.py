in_data = input("Please enter values using comma")
my_arr = in_data.split(",")
i = 0
k = 1
if len(my_arr) % 2 == 0:
    while k < len(my_arr):
        my_arr[i], my_arr[k] = my_arr[k], my_arr[i]
        i = i+2
        k = k+2
    print(my_arr)
else:
    while k < len(my_arr) -1:
        my_arr[i], my_arr[k] = my_arr[k], my_arr[i]
        i = i+2
        k = k+2
    print(my_arr)

