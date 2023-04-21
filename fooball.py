s = input()
suma = 0
for i in range(len(s)-1):
    if suma == 6:
        break
    if s[i] == s[i+1]:
        suma+= 1
        
    else:
        suma = 0
if suma > 5:
    print('YES')
else:
    print('NO')
