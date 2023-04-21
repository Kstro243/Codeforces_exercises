s = input()
a = input()

for i in range(len(s)):
    if s[i] == a[-i-1]:
        f = 1
    else:
        f = 0
        break
if f == 1:
    print('YES')
else:
    print('NO')
