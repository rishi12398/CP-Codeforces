s=input()
l = list(s)
i=max=k=0
j=len(l)-1
exist = False
while i<(len(l)-1) and j>0:
    hp = hash("".join(l[:i+1]))
    if hp < 0:
        hp = -hp
    hs = hash("".join(l[j:]))
    if hs < 0:
        hs = -hs
    #print (hs,hp)
    if hs == hp and hs > max:
        #print ("#")
        max = hs
        k = i
        exist = True
    i+=1
    j-=1
print (k)
print (max)
#print (hash("".join(l[0:k+1])))
#print (hash("fix"))
if exist is True:
    print(hash("".join(l[6:9])))
    i=1
    j=k+i+1
    while j<(len(l)-1):

        ob = hash("".join(l[i:j]))
        if ob < 0:
            ob = -ob
        print(i,j,ob)

        if ob == max:
            print ("".join(l[:k+1]))
            break
        i+=1
        j+=1
else:
    print("Just a legend")
