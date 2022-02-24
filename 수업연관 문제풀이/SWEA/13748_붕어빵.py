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


'''
교수님 버젼

def fun(n, m, k, lst):
    bucket = [0] * 10

    # 손님을 버켓에 등록
    for item in lst:
        bucket[item] -= 1

    # 누적합 구하면서 m초에 해당하는 인덱스에 도달하면 버켓의 값을 K개 증가
    # 버켓의 값을 확인하는데 음수면 꺼버리기
    
    for i in range(1, len(bucket)):
        bucket[i] += bucket[i-1]
        if (i%m) == 0:
            bucket[i] += K
        if bucket[i] < 0:
            return 'Impossible'
    return 'Possible'

'''