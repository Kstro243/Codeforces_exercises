s = str(int(input())+1)
a=1
n=[]
while True:
    for i in range(len(s)-1):
        if int(s[i])==int(s[i+1]):
            a=0
            break
        elif int(s[i])!=int(s[i+1]) and ((int(s[i]) in n) or (int(s[i+1]) in n)):
            a=0
            continue
        else:
            a=1
            n.append(int(s[i]))  
    n=[]
 
    if a==1:
        break
    s = str(int(s)+1)
print(s)
    
