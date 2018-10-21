n,m = input().split()
n = int(n)
m = int(m)

l = list(map(int,input().split()))
l.sort()
earn = 0
for i in range(len(l)):
    if m==0:
        break
    else:
        if l[i]<=0:
            earn = earn-l[i]
            m-=1
        else:
            break

print (earn)
