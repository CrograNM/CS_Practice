# 코딩 테스트 학습 전략 (Python)

이 폴더는 대회나 시험 일정과 관계없이 코딩 테스트를 연습할 때마다 계속 쓰는 공간이다.
기본 흐름은 **파이썬 복습 → 유형별 문제 풀이 → 실전 연습** 3단계이고, 공백기가 길었으면 1단계부터 다시 시작한다.

- 문제 풀이: [프로그래머스 코딩테스트 연습](https://school.programmers.co.kr/learn/challenges?order=recent)

---

## 0. 폴더 구조와 규칙

```
CS_Practice/
├── Python_Review/     # 1단계: 문법·모듈 복습용 짧은 문제와 연습 코드
├── Coding_Test_Prep/  # 2~3단계: 유형별 문제, 기출, 모의고사
│   ├── 01_구현/
│   ├── 02_문자열/
│   ├── 03_해시/
│   ├── ...
│   └── 99_기출/
└── _Docs/             # 학습 전략, 오답 노트, 치트시트 등 문서
```

- **파일 이름**: 문제 이름 그대로 짓는다 (예: `K번째수.py`). 다시 풀었으면 `K번째수_2.py`처럼 번호를 붙여서 처음 풀이와 비교할 수 있게 한다.
- **파일 첫 줄 주석**: 출처, 레벨, 날짜, 걸린 시간, 혼자 풀었는지를 적는다.
  ```python
  # 프로그래머스 Lv.1 | 2026-10-07 | 12분 | 혼자 풀이 O
  ```
- **커밋**: 하루 단위로, 메시지에 유형을 적는다 (예: `해시: 폰켓몬, 의상`).

---

## 1단계. 파이썬 복습

1년 넘게 쉬었거나 감이 떨어졌을 때 1~2일 정도 한다. 문법을 외우는 게 목표가 아니라 **손이 다시 기억하게 만드는 것**이 목표다.

### 1-1. 기본 문법
- [x] 슬라이싱, 정렬: `sorted(arr, key=lambda x: (x[1], x[0]))`, `reverse=True`
- [x] 문자열 ↔ 리스트: `split()`, `''.join(lst)`, `list(s)`
- [x] 리스트 컴프리헨션 (직접 쓰는 것보다 **읽을 줄 아는 게** 더 중요하다)
- [x] 2차원 리스트
  ```python
  board = [[0] * m for _ in range(n)]   # O
  board = [[0] * m] * n                 # X: 모든 행이 같은 리스트를 가리킨다
  ```
- [ ] `zip`, `enumerate`, `map`, `any`/`all`, `divmod`, `ord`/`chr`

### 1-2. 자주 쓰는 모듈
| 모듈 | 핵심 | 쓰는 곳 |
|---|---|---|
| `collections.deque` | `append`, `popleft` O(1) | 큐, BFS |
| `collections.Counter` | 개수 세기, `most_common()` | 해시 |
| `collections.defaultdict` | 기본값 있는 dict | 그래프 인접 리스트, 그룹핑 |
| `heapq` | `heappush`, `heappop` (최소 힙) | 우선순위 큐, 다익스트라 |
| `itertools` | `permutations`, `combinations`, `product` | 완전탐색 |
| `bisect` | `bisect_left`, `bisect_right` | 정렬된 리스트에서 이분탐색 |

- 최대 힙이 필요하면 `-x`를 넣는다.
- 재귀를 깊게 써야 하면 `sys.setrecursionlimit(10**6)`을 설정한다 (가능하면 반복문이나 BFS로 바꾼다).

### 1-3. 복습 문제 (프로그래머스)
문제당 5~10분을 목표로 풀고, 오른쪽에 적힌 구문을 써서 푸는 데 집중한다.

**리스트, 슬라이싱, 정렬**
- [x] K번째수 (Lv.1): 슬라이싱과 `sorted`
- [x] 문자열 내 마음대로 정렬하기 (Lv.1): `sorted(key=lambda)`
- [x] 문자열 내림차순으로 배치하기 (Lv.1): `sorted(reverse=True)`와 `join`

**2차원 리스트**
- [x] 행렬의 덧셈 (Lv.1): 2차원 리스트 생성과 순회
- [x] 행렬의 곱셈 (Lv.2): 3중 반복문, 리스트 컴프리헨션

**문자열 처리**
- [ ] 숫자 문자열과 영단어 (Lv.1): `replace`와 딕셔너리
- [ ] 대충 만든 자판 (Lv.1): 딕셔너리, `min`, 순회

**딕셔너리, 집합, Counter**
- [ ] 폰켓몬 (Lv.1): `set`
- [ ] 완주하지 못한 선수 (Lv.1): `Counter` 또는 딕셔너리
- [ ] 의상 (Lv.2): `defaultdict`, 경우의 수

**collections, heapq, itertools**
- [ ] 같은 숫자는 싫어 (Lv.1): 스택
- [ ] 기능개발 (Lv.2): `deque`
- [ ] 더 맵게 (Lv.2): `heapq`
- [ ] 두 개 뽑아서 더하기 (Lv.1): `combinations`, `set`
- [ ] 소수 찾기 (Lv.2): `permutations`

---

## 2단계. 유형별 문제 풀이

출제 비중이 높은 순서로 정리했다. 한 유형당 **Lv.1 1~2문제 → Lv.2 2~3문제**를 풀고 다음 유형으로 넘어간다.
각 유형마다 **언제 떠올리는지**, **핵심 구문**, **추천 문제**(프로그래머스) 순서로 적었다.

### 2-1. 구현·시뮬레이션
문제에 적힌 규칙을 그대로 코드로 옮기는 유형으로, 출제 비중이 가장 크다. 격자 위를 이동하는 문제가 많다.
코드를 쓰기 전에 **주석으로 단계부터 적는 습관**이 제일 중요하다.

```python
# 방향 배열: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = 5, 5     # 격자 크기 (n행 m열)
x, y = 0, 0
for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    # 격자 범위를 벗어나면 건너뛴다
    if 0 <= nx < n and 0 <= ny < m:
        print(nx, ny)

# 방향을 문자로 받을 때는 dict가 편하다
move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
ddx, ddy = move['E']
```

추천 문제: 공원 산책, 키패드 누르기, 방문 길이

### 2-2. 문자열
문자열은 수정할 수 없어서 바꿀 일이 많으면 **리스트로 바꿔서 작업한 뒤 `join`으로 합친다**.

```python
s = "Hello World"

s[::-1]                 # 뒤집기: 'dlroW olleH'
s.lower(), s.upper()    # 소문자, 대문자로 바꾸기
s.split()               # 공백 기준으로 나누기: ['Hello', 'World']
s.replace("l", "")      # 'l'을 모두 지우기: 'Heo Word'
s.isdigit(), s.isalpha()  # 전부 숫자인지, 전부 문자인지

# 문자 ↔ 아스키 코드
ord('a')    # 97
chr(97)     # 'a'
ord('c') - ord('a')     # 알파벳 순서 번호: 2

# 한 글자씩 바꾸고 다시 합치기
chars = list(s)
chars[0] = 'J'
result = ''.join(chars) # 'Jello World'
```

추천 문제: 숫자 문자열과 영단어, 대충 만든 자판, 신고 결과 받기

### 2-3. 해시 (dict, set, Counter)
"이 값이 있나?", "몇 개 있나?"를 빠르게(O(1)) 확인할 때 쓴다.
리스트에서 `in`으로 찾으면 O(N)이라 반복문 안에서 쓰면 시간 초과가 날 수 있다.

```python
from collections import Counter, defaultdict

# 개수 세기: 직접 하는 방법
count = {}
for name in ['a', 'b', 'a']:
    count[name] = count.get(name, 0) + 1    # {'a': 2, 'b': 1}

# 개수 세기: Counter
c = Counter(['a', 'b', 'a'])    # Counter({'a': 2, 'b': 1})
c.most_common(1)                # 가장 많은 것: [('a', 2)]
Counter(['a', 'b', 'a']) - Counter(['a', 'b'])  # 빼기: Counter({'a': 1})

# 중복 제거, 존재 확인
unique = set([1, 2, 2, 3])      # {1, 2, 3}
2 in unique                     # True (O(1))

# 같은 종류끼리 묶기
groups = defaultdict(list)
for name, kind in [['hat', 'head'], ['cap', 'head']]:
    groups[kind].append(name)   # {'head': ['hat', 'cap']}
```

추천 문제: 폰켓몬, 완주하지 못한 선수, 의상

### 2-4. 스택·큐
- **스택(나중에 넣은 것을 먼저 꺼냄)**: 괄호 짝 맞추기, "직전 값과 비교하기"
- **큐(먼저 넣은 것을 먼저 꺼냄)**: 순서대로 처리하기, BFS

```python
from collections import deque

# 스택: 리스트 그대로 쓴다
stack = []
stack.append(1)     # 넣기
stack.append(2)
stack[-1]           # 맨 위 확인: 2
stack.pop()         # 꺼내기: 2

# 괄호 검사 예시
def is_valid(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:       # 꺼낼 게 없으면 짝이 안 맞음
                return False
            stack.pop()
    return len(stack) == 0

# 큐: deque를 쓴다 (list.pop(0)은 O(N)이라 느리다)
q = deque([1, 2, 3])
q.append(4)         # 뒤에 넣기
q.popleft()         # 앞에서 꺼내기: 1
```

추천 문제: 같은 숫자는 싫어, 올바른 괄호, 기능개발

### 2-5. 정렬
정렬해 두면 문제가 쉬워지는 경우가 많다. **정렬 기준을 `key`로 정하는 법**만 알면 대부분 해결된다.

```python
arr = [3, 1, 2]
sorted(arr)                 # 새 리스트 반환: [1, 2, 3]
sorted(arr, reverse=True)   # 내림차순: [3, 2, 1]
arr.sort()                  # 원본을 정렬 (반환값 None)

words = ["banana", "kiwi", "apple"]
sorted(words, key=len)      # 길이순: ['kiwi', 'apple', 'banana']

# 기준 여러 개: 튜플로 쓰면 앞에서부터 차례로 비교한다
people = [("kim", 25), ("lee", 20), ("park", 25)]
sorted(people, key=lambda p: (-p[1], p[0]))
# 나이 내림차순, 같으면 이름 오름차순
# [('kim', 25), ('park', 25), ('lee', 20)]
```

추천 문제: 가장 큰 수, H-Index

### 2-6. 완전탐색
**입력이 작으면 가능한 경우를 전부 해본다.** 순열·조합은 itertools로 만든다.

```python
from itertools import permutations, combinations, product

nums = [1, 2, 3]
list(combinations(nums, 2))     # 순서 상관없이 2개: [(1, 2), (1, 3), (2, 3)]
list(permutations(nums, 2))     # 순서 있게 2개: (1, 2), (2, 1), ... 6개
list(product([0, 1], repeat=2)) # 중복 허용: [(0, 0), (0, 1), (1, 0), (1, 1)]

# 예: 두 수를 뽑아 더한 값을 중복 없이 정렬
answer = sorted(set(a + b for a, b in combinations(nums, 2)))

# 소수 판별: 제곱근까지만 확인한다
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

추천 문제: 두 개 뽑아서 더하기, 소수 찾기, 피로도

### 2-7. BFS·DFS
- **BFS**: 최단 거리를 구할 때 (deque 사용)
- **DFS**: 모든 경우를 끝까지 탐색할 때, 연결된 덩어리를 셀 때 (재귀 사용)

```python
from collections import deque

# BFS: 격자에서 (0, 0) → (n-1, m-1) 최단 거리
def bfs(maps):
    n, m = len(maps), len(maps[0])
    dist = [[-1] * m for _ in range(n)]  # -1이면 아직 방문 안 함
    dist[0][0] = 1
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1   # 큐에 넣을 때 방문 처리
                    q.append((nx, ny))
    return dist[n-1][m-1]

# DFS: 숫자마다 +/-를 붙여서 target을 만드는 경우의 수
def dfs(numbers, target, idx, total):
    if idx == len(numbers):             # 끝까지 왔으면
        return 1 if total == target else 0
    return (dfs(numbers, target, idx + 1, total + numbers[idx]) +
            dfs(numbers, target, idx + 1, total - numbers[idx]))

# 그래프: 인접 리스트 만들기
graph = [[] for _ in range(n)]
for a, b in [[0, 1], [1, 2]]:
    graph[a].append(b)
    graph[b].append(a)
```

추천 문제: 타겟 넘버, 게임 맵 최단거리, 네트워크

### 2-8. 그리디
**매 순간 가장 좋아 보이는 것을 고른다.** 대부분 "정렬한 뒤 앞이나 뒤에서부터 고르기" 형태다.
풀기 전에 "지금 최선이 전체 최선인가?"를 반례로 확인한다.

```python
# 예: 무게 제한 limit인 보트에 최대 2명씩 태울 때 필요한 보트 수
def boats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    count = 0
    while left <= right:
        # 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있으면 태운다
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1          # 무거운 사람은 항상 태운다
        count += 1
    return count
```

추천 문제: 체육복, 구명보트, 큰 수 만들기

### 2-9. 힙 (heapq)
**매번 최솟값이나 최댓값을 꺼내야 할 때** 쓴다. 매번 정렬하면 느리고, 힙은 넣고 빼는 데 O(log N)이다.

```python
import heapq

h = [5, 1, 3]
heapq.heapify(h)        # 리스트를 힙으로 바꾸기
heapq.heappush(h, 2)    # 넣기
heapq.heappop(h)        # 가장 작은 값 꺼내기: 1
h[0]                    # 가장 작은 값 확인만 (꺼내지 않음)

# 최대 힙: 음수로 넣고, 꺼낼 때 다시 음수로
max_h = []
heapq.heappush(max_h, -5)
-heapq.heappop(max_h)   # 5

# 튜플을 넣으면 첫 번째 값 기준으로 정렬된다
heapq.heappush(h, (3, 'task'))
```

추천 문제: 더 맵게, 디스크 컨트롤러

### 2-10. 이분탐색
- 정렬된 리스트에서 값을 빠르게 찾을 때
- **"답을 x로 정하면 조건을 만족하나?"**를 검사하면서 x의 범위를 반씩 줄여 나갈 때 (매개변수 탐색)

```python
from bisect import bisect_left, bisect_right

arr = [1, 2, 2, 2, 5]
bisect_left(arr, 2)     # 2가 처음 들어갈 위치: 1
bisect_right(arr, 2)    # 2가 마지막으로 들어갈 위치 다음: 4
bisect_right(arr, 2) - bisect_left(arr, 2)  # 2의 개수: 3

# 매개변수 탐색: 조건을 만족하는 가장 작은 답 찾기
def search(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(mid):   # mid로 가능하면 더 작은 쪽도 확인
            hi = mid
        else:               # 불가능하면 더 큰 쪽으로
            lo = mid + 1
    return lo
```

추천 문제: 입국심사, 퍼즐 게임 챌린지

### 2-11. DP (동적 계획법)
**작은 문제의 답을 저장해 두고 큰 문제에 재사용한다.**
코드보다 먼저 "dp[i]는 무엇인가?"와 점화식을 **말로 적는 것**이 핵심이다.

```python
# 예: 계단을 1칸 또는 2칸씩 오를 때 n번째 칸까지 가는 방법의 수
# dp[i] = i번째 칸까지 가는 방법의 수
# dp[i] = dp[i-1] + dp[i-2]
def stairs(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 2차원 DP: 격자에서 오른쪽, 아래로만 가는 경로 수
def paths(n, m):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1    # 첫 행과 첫 열은 가는 방법이 하나뿐
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]
```

추천 문제: 정수 삼각형, 등굣길

### 입력 크기로 알고리즘 고르기
| N | 허용 복잡도 | 떠올릴 것 |
|---|---|---|
| ~10 | O(N!) | 순열 완전탐색 |
| ~20 | O(2ⁿ) | 부분집합, 비트마스크 |
| ~500 | O(N³) | 3중 반복 |
| ~5,000 | O(N²) | 2중 반복 |
| ~100,000 이상 | O(N log N) 이하 | 정렬, 힙, 이분탐색, 해시, 투 포인터 |

---

## 3단계. 실전 연습

- **기출**: 프로그래머스에서 "PCCP 기출문제"나 "카카오" 기출을 검색해서 푼다.
- **시간 재기**: 실제 시험처럼 정해진 시간 안에 여러 문제를 한 번에 푼다.
- **목표 설정**: 첫 문제(가장 쉬운 문제)는 반드시 맞히고, 그다음 문제에서 부분 점수라도 챙긴다.

### 시험 당일 체크리스트
- [ ] 전체 문제를 먼저 훑어보고 쉬운 문제부터 푼다.
- [ ] 문제가 길면 주석으로 단계를 먼저 적고 코드를 쓴다.
- [ ] 입력 크기를 확인한다. 10만 이상이면 O(N²)를 피한다.
- [ ] 한 문제에 30분 넘게 막히면 다른 문제로 넘어갔다가 돌아온다.
- [ ] 제출 전에 엣지 케이스(빈 입력, 최솟값, 최댓값, 원소 1개)를 확인한다.
- [ ] 전날에는 새 문제를 풀지 말고 틀렸던 문제를 다시 보고, 충분히 잔다.

---

## 문제 풀이 루틴

1. **읽기 (3~5분)**: 입출력 형식, 제한 조건, 예제를 손으로 따라가 본다.
2. **설계 (5분)**: 유형을 판단하고 시간 복잡도를 확인한 뒤 주석으로 풀이 단계를 적는다.
3. **구현**: 주석 단계대로 코드를 채운다.
4. **검증**: 예제를 돌려보고 엣지 케이스를 직접 넣어본다.
5. **막혔을 때**: **20분** 넘게 진전이 없으면 풀이를 본다. 단, 그대로 베끼지 말고 이해한 뒤 **보지 않고 다시 짠다**.
6. **정리**: 다른 사람 풀이 중 더 파이썬다운 코드를 하나 보고, 배울 점이 있으면 주석으로 남긴다.

---

## 복습 주기

- 풀이를 보고 푼 문제는 **다음 날** 다시 푼다.
- 그래도 막힌 문제는 **1주 뒤**에 한 번 더 푼다.
- 반복해서 틀리는 패턴은 `_Docs/오답노트.md`에 한 줄씩 기록한다.
  ```
  - 2026-10-08 | 의상 | 조합 공식 (각 종류 개수 + 1)을 곱하고 1 빼기를 떠올리지 못함
  ```

---

## 일정 기록

시험이나 대회가 생길 때마다 여기에 계획을 추가하고, 끝나면 결과와 느낀 점을 남긴다.

### PCCP (2026-10-18, 일)
하루 2~3문제를 푼다.

| 날짜 | 주제 | 문제 |
|---|---|---|
| 10/7 (수) | 정렬·슬라이싱, 2차원 리스트 | K번째수, 문자열 내 마음대로 정렬하기, 행렬의 덧셈 |
| 10/8 (목) | 해시 | 폰켓몬, 완주하지 못한 선수, 의상 |
| 10/9 (금) | 스택·큐 | 같은 숫자는 싫어, 올바른 괄호, 기능개발 |
| 10/10 (토) | 힙·완전탐색 | 더 맵게, 두 개 뽑아서 더하기, 소수 찾기 |
| 10/11 (일) | 문자열·구현 | 숫자 문자열과 영단어, 대충 만든 자판, 신고 결과 받기 |
| 10/12 (월) | 시뮬레이션 | 공원 산책, 키패드 누르기, 방문 길이 |
| 10/13 (화) | BFS·DFS | 타겟 넘버, 게임 맵 최단거리, 네트워크 |
| 10/14 (수) | 그리디 | 체육복, 구명보트, 큰 수 만들기 |
| 10/15 (목) | PCCP 기출 ① | 붕대 감기, 동영상 재생기 |
| 10/16 (금) | PCCP 기출 ② | 석유 시추, 퍼즐 게임 챌린지 |
| 10/17 (토) | 마무리 | 틀렸던 문제 다시 풀기, 일찍 자기 |

- 목표: 전체의 절반 정도를 풀어 적당한 점수를 받는다.
- 시험 시간과 문항 수는 공지로 확인한다.
- 일정이 밀리면 10/12나 10/14를 줄이고, 기출(10/15~16)은 지킨다.
- 결과: _(시험 후 작성)_
