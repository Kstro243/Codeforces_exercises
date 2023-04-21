s = int(input())
a = 0
c = 0
for i in range(s):
    b=input()
    b=b.split()
    a=a-int(b[0])
    a=a+int(b[1])
    if a>c:
        c = a
print(c)
