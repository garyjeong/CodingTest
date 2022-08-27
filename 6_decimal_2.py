from itertools import combinations 
def check(a, b, c): 
    total = a + b + c

    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A: 
        if check(i[0], i[1], i[2]): answer += 1
        
    return answer

test_arr = [[1,2,3,4], [1,2,7,6,4], [1, 4, 5, 6, 2, 3], [1, 9, 3, 2, 8, 7, 6, 5, 4]]

for ar in test_arr:
    print(solution(ar))
