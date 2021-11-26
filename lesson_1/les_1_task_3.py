print("Please enter any number")
n = int(input())
if n==0:
    print(0)
elif n<=0:
    abs_n = n*-1
    nn = str(abs_n) + str(abs_n)
    nnn = str(abs_n) + str(abs_n) + str(abs_n)
    print(int(abs_n) + int(nn) + int(nnn))
else:
    nn = str(n) + str(n)
    nnn = str(n) + str(n) + str(n)
    print(int(n)+int(nn)+int(nnn))
