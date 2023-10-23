#a python program to print a spiral matrix based on user input no. of rows = n

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(0)
    matrix.append(row)

top = 0
bottom = n-1
left = 0
right = m-1
count = 1

while True:
    if left > right:
        break

    for i in range(left, right+1):
        matrix[top][i] = count
        count += 1
    top += 1

    if top > bottom:
        break

    for i in range(top, bottom+1):
        matrix[i][right] = count
        count += 1
    right -= 1

    if left > right:
        break

    for i in range(right, left-1, -1):
        matrix[bottom][i] = count
        count += 1
    bottom -= 1

    if top > bottom:
        break

    for i in range(bottom, top-1, -1):
        matrix[i][left] = count
        count += 1
    left += 1

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="\t")
    print()
