def remove_optimal_char(count_array):
    count_odd = 0
    count_even = 0
    count = 0
    players = ["First","Second"]
    for i in range(len(count_array)):
        if count_array[i]%2==0 and count_array[i]!=0:
            count_even+=1
        else:
            if count_array[i]%2!=0 and count_array[i]!=0:
                count_odd+=1

    #print count_even
    #print count_odd
    if count_odd == 0 or count_odd == 1:
        return count
    else:
        count = count_even
        count_odd = count_odd + count_even
        count = count + count_odd
    #print count
    return count

"""

def can_form_palindrome(count_array):
    count_odd=0
    for i in range(len(count_array)):
        if count_odd > 1:
            return False
        if count_array[i]%2 != 0:
            #print count_odd
            count_odd+=1

    return True
"""
s = raw_input()
count_array = [0]*26

for i in range(len(s)):
    count_array[ord(s[i])-97]+=1

#print count_array
count = remove_optimal_char(count_array)
if count % 2 == 0 and count !=0:
    print "Second"
else:
    print "First"
