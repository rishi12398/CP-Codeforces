x,y=raw_input().split()
n = input()
x = int(x)
y = int(y)
z = (10**9+7)
l=[0,x,y,y-x,-x,-y,x-y]
if n <= 6:
    ans = l[n]%z

if n > 6:
    if n%6==0:
        ans = l[6]%z
    else:
        n = n%6
        ans = l[n]%z

print ans
