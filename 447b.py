s = raw_input()
k = input()
#w={"a":[0,0],"b":[0,1],"c":[0,2],"d":[0,3],"e":[0,4],"f":[0,5],"g":[0,6],"h":[0,7],"i":[0,8],"j":[0,9],"k":[0,10],"l":[0,11],"m":[0,12],"n":[0,13],"o":[0,14],"p":[0,15],"q":[0,16],"r":[0,17],"s":[0,18],"t":[0,19],"u":[0,20],"v":[0,21],"w":[0,22],"x":[0,23],"y":[0,24],"z":[0,25]}
l = map(int,raw_input().split())
list_s=list(s)
max = max(l)
sum=0
for i in range(len(list_s)):
    #print l[ord(list_s[i])-97]
    sum = sum + l[ord(list_s[i])-97]*(i+1)
#print sum
i=0
while i<k:
    sum = sum + max*(i+len(list_s)+1)
    #print sum
    i+=1

print sum
