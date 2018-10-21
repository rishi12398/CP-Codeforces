def hash_oblix(l,ob,length,hash):
    i=1
    j=i+length
    z=0
    while i<j:
        ob = ob + (ord(l[i])-96)*(p**z)
        z+=1
        i+=1
        #print (ob)
    #print (ob)
    #print (j)
    if j > len(l)-1:
        return 0
    else:
        if j == len(l)-1:
            if int(ob) == hash:
                return ob
        else:
            while j<(len(l)-1):
                if int(ob) == hash:
                    return ob
                ob = ob-(ord(l[j-length])-96)
                ob = ob/p
                ob = ob + (ord(l[j])-96)*(p**(length-1))
                j+=1

    return 0

def hash_prefix(i,l,pv):
    pv = pv + (ord(l[i])-96)*(p**i)
    #pv = pv % m
    return pv

def hash_sufix(j,l,sv):
    sv = sv*p
    sv = sv + (ord(l[j])-96)
    #sv = sv % m
    return sv

s = input()
l = list(s)
pv = sv = 0
p = 3
i=k=0
j=len(l)-1
arr=[]
while i<(len(l)-1) and j>0:
    pv = hash_prefix(i,l,pv)
    sv = hash_sufix(j,l,sv)
    if pv == sv:
        k=i+1
        arr.append((k,pv))
    i+=1
    j-=1

#print (arr)
if len(arr)!=0:
    max = arr[len(arr)-1][1]
    ob = 0
    x1=0
    for i in range(len(arr)-1,-1,-1):
        ob = hash_oblix(l,ob,arr[i][0],arr[i][1])
        if ob!=0:
            x1 = arr[i][0]
            break
    #print (x1)
    if x1!=0:
        for x in range(0,x1):
            print(l[x],end="")
    else:
        print("Just a legend")
else:
    print("Just a legend")
