import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))

    stack = []
    stack2 = []
    for i in range(N):
         if i < (N-1)//2 + 1:
            stack.append(cards[i])
         else:
            stack2.append(cards[i])

    perfect_shuffle = []
    for i in range(N):
        if i == 0:
            perfect_shuffle.append(stack[0])
        elif i % 2 == 0:
            perfect_shuffle.append(stack[i//2])
        else:
            perfect_shuffle.append(stack2[i//2])

    print(f'#{tc}', ' '.join(map(str, perfect_shuffle)))