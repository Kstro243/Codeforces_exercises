s = input()
may = 0
minu = 0

for letra in s:
    if letra.isupper():
        may+=1
    else:
        minu+=1
if may > minu:
    print(s.upper())
else:
    print(s.lower())
              
