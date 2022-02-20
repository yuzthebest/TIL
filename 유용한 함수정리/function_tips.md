# 함수정리



1. **print**

   1차원 리스트 요소 프린트

   list = ['사과', '바나나', '복숭아']

   > 사과 바나나 복숭아로 프린팅하기
   >
   > ```
   > for l in list:
   > 	print(l, end=' ')
   > ```
   >
   > ```
   > print(' '.join(list))
   > 
   > * 여기서 유의사항은 join은 str만 할 수 있음!
   > 따라서 만약 리스트에 [1,2,'banana']
   > 이렇게 str아닌 값이 있을경우는
   > 
   > print(' '.join(map(str, list)))
   > 로 바꿔주기
   > ```
   >
   > 



2. 전치행렬 만들기

   A = [[1,2,3],[4,5,6]]

   a = [list(map(list, zip(*A)))]

​	zip함수
​		first= [1,2,3]
​		second = ['사과','바나나','포도']

​	zip(first, second)

​	