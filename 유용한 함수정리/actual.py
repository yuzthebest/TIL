# 1. 프린트하기
example = [1, '바나나', '복숭아']

print(' '.join(map(str, example)))

# 2. 전치행렬만들기

A = [[1,2,3], [4,5,6]]
a = list(map(list, zip(*A)))
print(a)

first= [1,2,3]
second = ['사과','바나나','포도']

t = list(zip(first, second))
print(t)