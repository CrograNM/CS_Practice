"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

참가자 중에는 동명이인이 있을 수 있습니다.

participant	                                            completion	                                return
["leo", "kiki", "eden"]	                                ["eden", "kiki"]	                        "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	    ["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	                ["stanko", "ana", "mislav"]	                "mislav"
"""
from collections import Counter

def solution(participant, completion):
    answer = ''
    c1 = Counter(participant)
    c2 = Counter(completion)

    # c1에 있는 키가 c2에 없거나, c2의 밸류가 적은 경우 해당 키가 답임
    for key, value in c1.items():
        if key not in c2:
            answer = key
        elif value > c2[key]:
            answer = key
    return answer

def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)

    # print(answer)
    #
    # print(list(answer.keys())[0])

    key, value = answer.popitem()
    # print(key, value)
    
    return key

def solution3(participant, completion):
    # 카운터 쓰지 않고 Dict으로만 구현해보기
    p = dict()
    answer = ''

    # print(p)
    for part in participant:
        if part not in p:
            p[part] = 1
        else:
            p[part] += 1
    # print(p)
    for comp in completion:
        if comp in p:
            p[comp] -= 1
    # print(p)
    for key, val in p.items():
        if val > 0:
            answer = key

    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution3(participant, completion))
