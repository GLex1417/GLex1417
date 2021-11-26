seasons_dict_list = {'Winter':[12,1,2], 'Spring': [3,4,5], 'Summer': [6,7,8], 'Autumn': [9,10,11]}
month = int(input("Please enter a month number"))

for key in seasons_dict_list:
    for i in seasons_dict_list[key]:
        if month == i:
            print(key)