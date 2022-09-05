def solution(s):
    answer = ''

    s = s.split(' ')

    for i in range(0, len(s)):
        s[i] = list(s[i])
        for j in range(0, len(s[i])):
            if (j % 2) == 0:
                s[i][j] = s[i][j].upper()
            else:
                s[i][j] = s[i][j].lower()
        s[i] = ''.join(s[i])
        
    answer = ' '.join(s)

    return answer

test_arr = ["try hello world"]

for ar in test_arr: 
    print(solution(ar))