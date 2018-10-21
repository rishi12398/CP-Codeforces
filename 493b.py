n = input()
player1=[]
sum1=0
sum2=0
player2=[]
for i in range(n):
    point = input()
    if point > 0:
        if i == n-1:
            last = "first"
        player1.append(point)
        sum1 = sum1 + point
    else:
        if i == n-1:
            last = "second"
        player2.append(-point)
        sum2 = sum2 - point

#print player1
#print player2
#print last
if sum1 > sum2:
    ans =  "first"
else:
    if sum2 > sum1:
        ans =  "second"
    else:
        if sum1 == sum2:
            for i in range(len(player1)):
                if player1[i] > player2[i]:
                    ans =  "first"
                    break
                else:
                    if player2[i] > player1[i]:
                        ans =  "second"
                        break
                    else:
                        if player1[i] == player2[i]:
                            ans = last


print ans
