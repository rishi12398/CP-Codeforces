T = int(input())
ans = []
for t in range(T):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    #print (l)
    count = k
    for i in range(k,n):
        if l[i] == l[k-1]:
             count+=1
        else:
            break
    ans.append(count)

for a in ans:
    print (a)
