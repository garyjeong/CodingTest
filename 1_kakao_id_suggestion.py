# 완료
import re

def solution(new_id):
    answer = new_id
    # 소문자로 치환
    answer = answer.lower()
    # 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 조건 제외하고 공백 치환
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    # 마침표(.) 중복 문자열 마침표(.) 한 개로 치환
    answer = re.sub('\.+', '.', answer)
    # 마침표(.) 문자열 첫 번째 또는 마지막 제거
    answer = re.sub('^[.]|[.]$', '', answer)
    # 문자열이 빈 문자열이면 a를 대입
    if len(answer) == 0:
        answer = 'a'
    # 문자열의 길이가 15자 초과이면 문자열 자름
    if len(answer) > 0:
        answer = answer[:15]
    # 문자열 15자리 자른 후 마침표(.) 문자열 첫 번째 또는 마지막 제거
    answer = re.sub('^[.]|[.]$', '', answer)

    while len(answer) < 3:
        answer += answer[-1]

    return answer

test_arr = [
    "...!@BaT#*..y.abcdefghijklm",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p",
    "iuf!@",
    "!@#!@#",
    "..3..3..3.....3..4.",
    "...........",
    "_-_-_abc_-_-",
    "..abc'29-=",
    "...,,,,===+++무무무/vb",
    ".1.112...3.124..#$%^&*().",
    ".!@#!@#BVI...USBL......VIb......abdVNVN.[]",
    "!@#!@$....!@#!@#!"]

for ar in arr_str:
    print(solution(ar))
