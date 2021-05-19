def word_reverse(st):
    d=st.split()
    for i in range (len(d)):
        d[i]=d[i][::-1]
        return " ".join(d)
   

st=input()
st=word_reverse(st)
print(st)
