import sys
from collections import deque
sys.stdin = open("input.txt")



M, D = map(int, input().split())
d = deque()
visited = [0] * 100001

d.append(M)

while d:
    me = d.popleft()
    if me == D:
        print(visited[me])
        break
    else:
        for i in [me+1, me-1, 2*me]:
            if 0<= i <=100000 and visited[i] == 0:
                visited[i] = visited[me] + 1
                d.append(i)

