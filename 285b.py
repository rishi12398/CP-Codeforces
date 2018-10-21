n,s,t = raw_input().split()
n = int(n)
s = int(s)
t = int(t)

l1 = map(int,raw_input().split())
l=[]
l.append(0)
for i in range(len(l1)):
    l.append(l1[i])
#print l
temp = s
ans = 0
count = 0
i = s
while(1):
    if i == t:
        ans = ans
        break
    else:
        if i == l[i]:
            ans = -1
            break
        else:
            if temp == i and count ==1:
                ans = -1
                break
            else:
                i = l[i]
                ans += 1
                count = 1

print ans
