import math
with open("day08/day08-input.txt",'r') as f:
    data=[list(map(int,i.split(','))) for i in f.read().split()]
# print(data)

distbw=[]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if(i!=j):
            dist=math.sqrt((data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2+(data[i][2]-data[j][2])**2)
            distbw.append([i,j,dist])
distbw.sort(key=lambda inner: inner[2])
# print(distbw)

circuits=[[distbw[0][0],distbw[0][1]]]
for i in range(1000):
    newcircuit=[]
    box1,box2=distbw[i][0],distbw[i][1]
    print(box1, box2, distbw[i][2])
    for k in range(len(circuits)):
        if(box1 in circuits[k] and box2 in circuits[k]):
            break
        elif(box1 in circuits[k] or box2 in circuits[k]):
            flag=0
            for x in range(len(circuits)):
                if(x!=k and (box1 in circuits[x] or box2 in circuits[x])):
                    circuits[k].extend(circuits[x])
                    circuits.pop(x)
                    circuits[k]=list(set(circuits[k]))
                    flag=1
                    break
            if flag: break
        if(box1 in circuits[k]):
            circuits[k].append(box2)
            break
        elif(box2 in circuits[k]):
            circuits[k].append(box1)
            break
    else:
        circuits.append([box1,box2])
    print(circuits)


circuits.sort(key=len, reverse=True)
tot=1
for c in range(3):
    if c>=len(circuits): break
    tot*=len(circuits[c])
print(tot)