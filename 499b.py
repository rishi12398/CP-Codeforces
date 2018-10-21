n,m = raw_input().split()
n = int(n)
m = int(m)
d={}

for i in range(m):
    word1,word2 = raw_input().split()
    d[word1] = word2

lect = map(str,raw_input().split())
for i in range(len(lect)):
    if len(lect[i]) > len(d[lect[i]]):
        lect[i] = d[lect[i]]


print " ".join(lect)
