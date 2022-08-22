
# 설문 사전 순
# R - T, C - F, M - J, A - N
# Level : 1, 2, 3, 4, 5, 6, 7

def devider(types, point):
    result = ''
    if point > 4:
        result = types[1]
    elif point < 4:
        result = types[0]
    else:
        result = types[1]

def solution(survey, choice):
    surveyList = {'RT', 'CF', 'MJ', 'AN'}
    scoreList = [3, 2, 1, 0, 1, 2, 3]

    answer = ''
    
    for i in range(0, len(survey)):
        matched = survey[i] in surveyList
        if matched:
            print('score: ', survey[i], choice[i], scoreList[choice[i] - 1])
            answer += {survey[i]: scoreList[choice[i] - 1]}
        else :
            target = survey[i]
            # print(target[::-1] in surveyList)
            if(target[::-1] in surveyList):
                if 
                print('score reverse: ', survey[i], choice[i], scoreList[(7 - choice[i]) - 1])
            else:
                print('E')
        # print(choice[i])
        # print(scoreList[choice[i] - 1])
        # if choice[i] < 4:
        #     # answer += scoreList(survey[i][0])
        #     # print(scoreList(choice[i]))
        #     print(choice[i])
        # elif choice[i] > 4:
        #     # answer += scoreList(survey[i][1])
        #     print(scoreList(choice[i]))
        # else:
        #     # answer += scoreList(survey[i][0])
        #     print(scoreList(choice[i]))

    return answer



survey_arr = [["AN", "CF", "MJ", "RT", "NA"], ["TR", "RT", "TR"]]
choice_arr = [[5, 3, 2, 7, 5], [7, 1, 3]]

for idx in range(0, len(survey_arr)):
    # solution(size)
    print(solution(survey_arr[idx], choice_arr[idx]))