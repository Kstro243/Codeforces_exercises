s = input()
a = []
for i in s.split():
    a.append(int(i))
c=0
for i in range(a[1]):
    if a[0]%10 != 0:
        a[0]=(a[0])-1
    else:
        a[0]=(a[0])/10
print(int(a[0]))
