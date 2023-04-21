a = int(input())
b= input()
A=b.count('A')
D=b.count('D')
if A>D:
    print('Anton')
elif D>A:
    print('Danik')
else:
    print('Friendship')
