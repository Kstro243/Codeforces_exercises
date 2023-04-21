s = input()
s = s.split()
a = input()
n = []

for i in range(int(s[1])):
    for j in range(int(s[0])):
        if j==int(s[0])-1:
            if a[j]=='G':
                if a[j-1]=='B':
                    continue
                else:
                    n.append('G')
            elif a[j]=='B':
                n.append('B')
        elif a[j]=='B' and a[j+1]=='G':
            n.append('G')
            n.append('B')
        elif a[j]=='G' and a[j-1]=='B' and j!=0:
            continue
        elif a[j]=='G':
            n.append('G')
        elif a[j]=='B':
            n.append('B')           
    a=n
    n=[]
print("".join(a))
        
