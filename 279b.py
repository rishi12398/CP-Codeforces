n,t = raw_input().split()
n = int(n)
t = int(t)
l = map(int,raw_input().split())
sum = 0
for i in range(len(l)):
    sum = sum+l[i]
print sum

i=0
j=len(l)-1
while( sum >= t):
        if l[i] > l[j]:
            sum = sum - l[i]
            i+=1
        else:
            sum = sum - l[j]
            j-=1

print j-i+1
