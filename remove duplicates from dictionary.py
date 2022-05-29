y={'a':1,'b':22,'a':3,'c':22}
temp=[]
res=dict()
for key,val in y.items():
    if val not in temp:
        temp.append(val)
        res[key]=val
print(res)