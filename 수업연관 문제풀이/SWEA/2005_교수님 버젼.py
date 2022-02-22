
T = int(input())

def use_stack():
    pass

for tc in range(1, T+1):

    N = int(input())

    frame = [[] for _ in range(N)]
    frame[0].append(1)

    for i in range(1, N):
        stack = frame[i-1]
        frame[i].append[1]
        for j in range(1, i):
            num = stack.pop() + stack[-1]
            frame[i]. append(num)
        frame[i]. append(1)