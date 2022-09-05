from cgi import test


def solution(num):
    answer = ''

    if (num % 2) == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer


test_arr = [3, 4, 5, 6, 7]

for ar in test_arr:
    print(solution(ar))