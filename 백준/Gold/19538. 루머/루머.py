from collections import deque
n=int(input())
people=[]
for i in range(n):
    t=list(map(int,input().split()))
    t.pop()
    people.append(t)
people.insert(0,[])
m=int(input())
start=list(map(int,input().split()))

time=[-1]*(n+1)
for i in start:
    time[i]=0

start=deque(start)
que=deque([])
while(start):
    index=start.popleft()
    temp=people[index]
    move=[]
    for i in temp:
        count=0
        if time[i]!=-1:
            continue 
        leng=len(people[i])
        for j in range(leng):
            if time[people[i][j]]!=-1:
                count+=1
        if leng>count*2:
            continue
        que.append(i)
    if not start:
        while(que):
            tmp=que.popleft()
            time[tmp]=time[index]+1
            start.append(tmp)

time.remove(time[0])
print(*time)