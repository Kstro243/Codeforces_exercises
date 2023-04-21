s = input()
a = int(s.count('0'))+int(s.count('1'))+int(s.count('2'))+int(s.count('3'))+int(s.count('5'))+int(s.count('6'))+int(s.count('8'))+int(s.count('9'))
b = str(s.count('4')+s.count('7'))
d = s.count('4')
e = s.count('7')
g = str(len(b))
z = int(g.count('0'))+int(g.count('1'))+int(g.count('2'))+int(g.count('3'))+int(g.count('5'))+int(g.count('6'))+int(g.count('8'))+int(g.count('9'))
c = int(b.count('0'))+int(b.count('1'))+int(b.count('2'))+int(b.count('3'))+int(b.count('5'))+int(b.count('6'))+int(b.count('8'))+int(b.count('9'))
if a>0 and z==0:
    print('YES')
elif int(b)>0 and c==0:
    print('YES')
else:
    print('NO')
