l=[3,4,"Ananya"]
print(l)
print(type(l))
print(l[0])
if "Ananya" in l:
    print("yes")
else:
    print("no")
    
print(l[:])
#python automatically puts before ":" 0 and after ":" len(Of the item you are accessing)
#negative idex means length of item -the no given
lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%3==0]
print(lst)