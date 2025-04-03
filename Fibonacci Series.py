fs = [0, 1]
i = 2
n = int(input("Enter length of fibonacci series: "))
if n == 0:
    print([])
elif n == 1:
    print(fs[:1])
elif n == 2:
    print(fs[:2])
else:
    while i < n:
        s = fs[-1] + fs[-2]
        fs.append(s)
        i += 1
    print(fs)
