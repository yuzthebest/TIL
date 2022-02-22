import sys
sys.stdin = open("input.txt")

def bubble_sort(L):

    for i in range(len(L)):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    sort_time = bubble_sort(time)

    produce_fish = 0
    taken_fish = 0
    for t in sort_time:
        if M > t:
            break
        else:
            produce_fish = (t//M) * K
            if produce_fish - taken_fish >= 1:
                taken_fish += 1
            else:
                break

    if taken_fish == N:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
