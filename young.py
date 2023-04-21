n=int(input())
a=[]
for i in range(n):
    d=[]
    b=input()
    c=b.split()
    for num in c:
        d.append(int(num))
    a.append(d)
f=0
for i in range(3):
    suma = 0
    for j in range(n):
        suma += a[j][i]
    if suma!=0 :
        f = 1
if f==1 :
    print('NO')
else:
    print('YES')
