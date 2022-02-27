import sys
sys.stdin = open("input.txt")


def get_max(N):

    mid = (N // 2) + 1
    max = 0
    max_i = 0
    for i in range(mid, N+1):
        stack = []
        stack.append(N)
        stack.append(i)
        while stack[-2] - stack[-1] >= 0:
            stack.append(stack[-2] - stack[-1])
        if len(stack) > max:
            max = len(stack)
            max_i = i
    return max, max_i



T = int(input())
max, max_i = get_max(T)
stack =[]
stack.append(T)
stack.append(max_i)
while stack[-2] - stack[-1] >= 0:
    stack.append(stack[-2] - stack[-1])
print(f'{max}')
print(' '.join(map(str,stack)))
