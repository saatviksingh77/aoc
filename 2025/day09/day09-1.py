with open("day09/day09-input.txt","r") as f:
    data=[list(map(int,i.split(','))) for i in f.read().split()]
# print(data)

areabw=[]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        areabw.append([i,j,abs(data[i][0]-data[j][0]+1)*abs(data[i][1]-data[j][1]+1)])
areabw.sort(key=lambda inner: inner[2], reverse=True)
# print(areabw)
print(areabw[0][2])