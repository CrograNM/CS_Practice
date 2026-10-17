"""
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

예를 들어 코니가 가진 옷이 아래와 같고,
오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면
다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

종류	        이름
얼굴	        동그란 안경, 검정 선글라스
상의	        파란색 티셔츠
하의	        청바지
겉옷	        긴 코트

코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다.
예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나,
혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
코니는 하루에 최소 한 개의 의상은 입습니다.

코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때
서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

"""

import itertools

def solution(clothes):
    # clothes = [의상 이름, 종류]의 배열
    # 종류를 키로, 종류에 해당하는 의상 이름의 집합을 밸류로 하는 dict?
    """
    headgear: yellow hat, green turban      2개
    eyewear: blue sunglasses                1개
                                            --> 종류 1개 : 3
                                                종류 2개 : 2*1
                                                총 조합 : 5

    모든 경우의 수
        yellow hat
        green turban
        blue sunglasses
        yellow hat + blue sunglasses
        green turban + blue sunglasses

    = 1~N의 종류 개수 조합 내에서 의상을 1개씩 조합

    dict_clothes = {종류1: (의상1, 의상2 ,...), 종류2: ...}
    총 조합 = dict_clothes 순회

    종류 1개만 판단 - 총 의상 개수
    종류 2개만 판단 - 종류1개수*종류2개수, ..., 이런식으로 곱하기 횟수 2번
    --> 종류별 개수만 있으면 되나?

    dict_clothes = {종류1: 개수, 종류2: 개수, ...}
    """
    dict_clothes = dict()
    for cloth, cloth_type in clothes:
        if cloth_type not in dict_clothes:
            dict_clothes[cloth_type] = 1
        else:
            dict_clothes[cloth_type] += 1

    print(len(dict_clothes))

    answer = 0
    return answer


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))