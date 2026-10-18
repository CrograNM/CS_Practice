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
from itertools import permutations


def solution(clothes):
    """
    --> 종류별로 '안 입는다' 를 선택지에 추가한다
        --> headgear: yellow_hat, green_turban, 안 입음.   선택지 3개
        --> eyewear: blue_sunglasses, 안 입음.             선택지 2개
        --> 3*2 = 6, 하지만 최소 한개는 입어야 하므로 모두 안입는 선택지 -1 = '5'
    """
    dict_clothes = dict()
    for cloth, cloth_type in clothes:
        if cloth_type not in dict_clothes:
            dict_clothes[cloth_type] = 1
        else:
            dict_clothes[cloth_type] += 1

    # print(len(dict_clothes))
    answer = 1
    for count in dict_clothes.values():
        answer *= (count + 1)

    # 전부 안 입는 경우 1가지를 뺀다
    return answer - 1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))