# 완료

# 기대값 [4, 7, 12] / [True, False, True] -> 9
# 기대값 [1, 2, 3] / [False, False, True] -> 0
def solution(absolutes, signs):
    # signs가 True면 양수
    # signs가 False면 음수
    answer = 0

    for i in range(0, len(absolutes)):
        if not signs[i]:
            absolutes[i] *= -1
        answer += absolutes[i]
    
    return answer

test_absolutes_arr = [[4, 7, 12], [1, 2, 3]]
test_signs_arr = [[True, False, True], [False, False, True]]

for i in range(0, len(test_absolutes_arr)):
    solution(test_absolutes_arr[i], test_signs_arr[i])