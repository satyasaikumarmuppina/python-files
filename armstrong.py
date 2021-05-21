num=int(input())
s=0
t=num
while num>0:
    d=num%10
    s+=d**3
    num//=10

if t==s:
    print(t,"is armstrong number")
else:
    print(t,"is not armstrong number")
