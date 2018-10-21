def find_sum_pair(l,sum,s):
    for i in range(len(l)):
        temp = sum - l[i]
        if temp>=0 and temp in s:
            print "pairs with given sum is :"+str(l[i])+" "+str(temp)
            break

l = map(int,raw_input().split())
sum = input()
s = set()
for i in range(len(l)):
    s.add(l[i])

find_sum_pair(l,sum,s)
