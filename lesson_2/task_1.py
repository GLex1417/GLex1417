my_arr = [1, "one", 2, "two", [1,2,3], 3, "three", True, 1.25, {'name': "Alex", 'age': 32}]
i=0

print("Types using While cycle")
while i<len(my_arr):
    print(type(my_arr[i]))
    i = i+1

print("Types using For cycle")
for item in my_arr:
    print(type(item))