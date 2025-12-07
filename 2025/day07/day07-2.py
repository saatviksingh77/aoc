'''
###### recursive approach, DFS, uses memoization (ie cache) ########
'''

from functools import cache
with open("day07/day07-input.txt","r") as f:
    grid=[list(line.strip()) for line in f]

S=[(r,c) for r,row in enumerate(grid) for c,char in enumerate(row) if char=='S'][0]
#enumerate gives u index with the item at the same time while going thru an iterable

@cache #stores values to use again without having to solve again
def solve(r,c):
    if r>=len(grid): return 1
    if grid[r][c]=='.' or grid[r][c]=='S':
        return solve(r+1,c)
    elif grid[r][c]=='^':
        return solve(r,c-1) + solve(r,c+1)
print(solve(*S))



'''
---- modified version of part-1
######## collections counter approach ########
'''

from collections import Counter
with open("day07/day07-input.txt",'r') as f:
    data=[i for i in f.read().split()]

timeline_counts=Counter({data[0].find('S'):1})

for i in range(2,len(data),2):
    new_counts=Counter()
    for col, num_timelines in timeline_counts.items():
        if col<len(data[i]) and data[i][col]=='^':
            new_counts[col-1]+=num_timelines
            new_counts[col+1]+=num_timelines
        else:
            new_counts[col]+=num_timelines  
    timeline_counts=new_counts
#instead of set logic, taking all the active beams at given index into account
print(sum(timeline_counts.values()))