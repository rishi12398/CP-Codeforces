
def to_binary_list(integer,n):
        base = '{'+'0'+':'+'0'+str(n)+'b'+'}'
        #print base
        l = list(base.format(integer))
        #print l
        return l

n,m,k = raw_input().split()
n = int(n)
m = int(m)
k = int(k)
l=[]
for i in range(0,m+1):
    army = input()
    l.append(army)


friend = 0
fedor_binary_list = to_binary_list(l[m],n)

for i in range(0,m):
    diffrence = 0
    l1 = to_binary_list(l[i],n)
    for j in range(len(l1)):
        if l1[j] != fedor_binary_list[j]:
            diffrence = diffrence + 1

    #print diffrence
    if diffrence <= k:
        friend = friend + 1

print friend
