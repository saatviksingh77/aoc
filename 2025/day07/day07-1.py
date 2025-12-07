with open("day07/day07-input.txt","r") as f:
    data=[i for i in f.read().split()]

splitted=0
indexlist=[data[0].find('S')]
for i in range(2,len(data),2):
    newlist=[]
    for j in indexlist:
        if j<len(data[i]) and data[i][j]=='^':
            splitted+=1
            newlist.append(j-1)
            newlist.append(j+1)
        else:newlist.append(j)
        # print(newlist)
    indexlist=list(set(newlist))
    # print(indexlist)
print(splitted)