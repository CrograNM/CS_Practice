"""
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
"""

def solution(s):
    return ''.join(sorted(s, reverse=True))

# '구분자'.join(리스트) : 리스트를 구분자로 연결해 문자열로 변환해주는 함수 ( -> '_'.join(['A', 'B', 'C']) = 'A_B_C' )

s = "Zbcdeafg"
print(solution(s))