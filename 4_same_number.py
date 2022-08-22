# 완료
def solution(arr): 
    answer = []

    #
    for i in arr:
        if (len(answer) == 0) or (answer[-1] != i):
            answer.append(i)
    return answer


test_arr = [[1, 1, 3, 3, 0, 1, 1], [4, 4, 4, 3, 3]]

for ar in test_arr:
    solution(ar)