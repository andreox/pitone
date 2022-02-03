std = []
for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    std.append( [name,score] )


for i in range( len(std) ) :
    for j in range( i ) :

        if ( std[i][1] < std[j][1] ) :
            tmp = std[i]
            std[i] = std[j]
            std[j] = tmp

i = 0
while ( (std[i][1] == std[i+1][1]) and ( i < len(std)-1) ) :
    i += 1

#print i
std = std[(i+1):]
#print std

i = 0
p = 1
while ( ( i < len(std)-1) and (std[i][1] == std[i+1][1])) :
    p += 1
    i += 1

ans = std[0:p]
ans.sort()

for i in range ( len(ans) ) :
    print ans[i][0]
