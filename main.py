n = int(input("> "))
t1 = 0
t2 = 1
cont = 3
print ("{}, {},".format(t1, t2))
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print("{},".format(t3), end="")
