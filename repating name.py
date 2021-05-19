n=input()
d={}
for i in n:
    if i not in d.keys():
       d[i]=1
    else:
        d[i]+=1
g=0
p=0
for k,v in d.items():
    if v>g:
        p=k
        g=v
print(p)
