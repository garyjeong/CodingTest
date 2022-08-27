
from itertools import combinations

# 기대값 [1,2,3,4] -> 1
# 기대값 [1,2,7,6,4] -> 4
def solution(nums: list):
    # 소수의 정의 : 양의 약수가 1과 자신뿐인 2개로 구성된 자연수
    # 즉, 나누었을 때 1과 자기 자신으로만 나눌 수 있는 자연수
    answer = 0

    # combinations를 사용해서 중복되지 않는 조합을 구함
    # combinations([배열 또는 리스트], [조합의 갯수])
    temp = list(combinations(nums, 3))

    # 각 조합별 탐색
    for (a, b, c) in temp:
        # 합계
        total = a + b + c

        # 나머지 연산이 성공한 갯수를 저장할 변수
        temp = 0

        for i in range(2, total): 
            # 나머지 연산 성공
            if total % i == 0: 
                temp += 1
                break

        # 합계의 미만의 수 중 나머지 연산이 성공하지 않으면 소수
        if temp == 0:
            answer += 1

    return answer

test_arr = [[1,2,3,4], [1,2,7,6,4], [1, 4, 5, 6, 2, 3], [1, 9, 3, 2, 8, 7, 6, 5, 4]]

for ar in test_arr:
    print(solution(ar))
