def no_of_moments(p_list,q_list,l,r,moments=0):
    temp = 9999
    for i in range(l,r+1):
        for j in p_list:
            for k in q_list:
                if (k[1]+i) < j[0] or (k[0]+i) > j[1]:
                    pass
                else:
                    #print "i "+str(i)
                    if i!=temp:
                        moments = moments+1
                        temp = i



    return moments


p,q,l,r = raw_input().split()
p = int(p)
q = int(q)
l = int(l)
r= int(r)
p_list = []
q_list = []
for i in range(p):
    l1 = map(int,raw_input().split())
    p_list.append(l1)

for i in range(q):
    l1 = map(int,raw_input().split())
    q_list.append(l1)

#print p_list
#print q_list
print no_of_moments(p_list,q_list,l,r)
