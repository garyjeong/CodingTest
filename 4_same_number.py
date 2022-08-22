# 완료

# 기대값 [1,1,3,3,0,1,1] -> [1,3,0,1]
# 기대값 [4,4,4,3,3] -> [4,3] 
def solution(arr): 
    # 단순히 중복제거를 하게 되면 첫번 째 기대값과는 다르게 나온다.
    # 조건은 단순히 근접한 중복 숫자만 제거하면 된다.
    answer = []

    for i in arr:
        # answer에 arr의 요소를 넣되 
        # answer은 처음에 비어있으므로 1개는 넣고 시작
        # 이후 answer의 마지막 요소와 arr의 가져올 요소를 비교한다.
        if (len(answer) == 0) or (answer[-1] != i):
            answer.append(i)
    return answer


test_arr = [[1, 1, 3, 3, 0, 1, 1], [4, 4, 4, 3, 3]]

for ar in test_arr:
    solution(ar)