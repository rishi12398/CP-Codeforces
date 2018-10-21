n = input()
l = list(n)
#print (l)
count_4 = 0
count_7 = 0
for i in range(len(l)):
    l[i] = int(l[i])
    if l[i]==4:
        count_4+=1
    if l[i]==7:
        count_7+=1

if count_4 is 0 and count_7 is 0:
    print ("-1")
else:
    if count_4 >= count_7:
        print ("4")
    else:
        print("7")
