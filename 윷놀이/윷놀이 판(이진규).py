 #윷놀이 판 생성
yut_board = [['-' for _ in range(5)] for _ in range(5)]

# 판에 좌표 설정
for x in range(5):
    for y in range(5):
        yut_board[x][y] = f'({x}, {y})'

# 이동 불가능한 좌표 설정
invalid_coordinates = [(1, 2), (2, 1), (3, 2), (2, 3)]

# 이동 불가능한 좌표 값을 변경
for coordinate in invalid_coordinates:
    x, y = coordinate
    yut_board[x][y] = '  X   '

# 판 출력
for x in yut_board:
    print(' '.join(x))