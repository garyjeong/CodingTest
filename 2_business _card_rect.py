# 완료
_arr = [[[60, 50], [30, 70], [60, 30], [80, 40]], [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]]

def solution(sizes):
    answer = 0

    x, y = [], []
    for i in sizes:
        if i[0] < i[1]:
            temp = i[0]
            i[0] = i[1]
            i[1] = temp
        x.append(i[0])
        y.append(i[1])

    answer = max(x) * max(y)
    return answer

for size in _arr:
    # solution(size)
    print(solution(size))