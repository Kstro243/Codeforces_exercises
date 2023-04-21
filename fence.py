s = input()
s = s.split()
a = input()
a = a.split()
re = 0
for ele in a:
    if int(ele)>int(s[1]):
        re+=2
    else:
        re+=1
print(re)
