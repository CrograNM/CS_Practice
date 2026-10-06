
# N * M Size
n = 4
m = 3
array = [[0] * m for _ in range(n)]
array[1][2] = 3
print(array)

# N * M * L Size
n = 4
m = 3
l = 2
array = [[[0] * l for _ in range(m)] for _ in range(n)]
array[0][0][1] = 1
print(array)
