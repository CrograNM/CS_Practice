"""
2차원 행렬 arr1과 arr2를 입력받아,
arr1에 arr2를 곱한 결과를 반환하는 함수,
solution을 완성해주세요.
"""

def solution(arr1, arr2):
    N = len(arr1)
    M = len(arr2[0])
    answer = [[0]*M for _ in range(N)]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# return = [[15, 15], [15, 15], [15, 15]]

"""
 {A}         {B}
2 3 2       5 4 3
4 2 4   x   2 4 1   
3 1 4       3 1 1

행렬곱: A는 행마다 다음 열로, B는 열부터 다음 행으로 순서대로 요소 별 계산, 결과는 행 -> 열 순서로 차례대로 채워짐 (A순서)
"""
print(solution(arr1, arr2))