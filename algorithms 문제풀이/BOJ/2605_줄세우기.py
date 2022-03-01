import sys
sys.stdin = open("input.txt")

N = int(input())

nums = list(map(int, input().split()))
new_list = []

for i in range(len(nums)):
    if nums[i] == 0:
        new_list.append(i+1)
    else:
        new_list.insert(i-nums[i], i+1)

print(' '.join(map(str, new_list)))