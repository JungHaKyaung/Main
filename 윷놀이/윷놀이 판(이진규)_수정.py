# 가로 세로 6칸에 대각선 7칸이어야되는데 가로세로 대각선 모두 5칸이어서 수정함.
# 근데 말 이동을 수정하기 불편해보임

#윷놀이 판 생성
yut_board = [['-' for _ in range(7)] for _ in range(9)]
  
  
# 판에 좌표 설정
for x in range(9):
    for y in range(7): 
        yut_board[x][y] = f'({x}, {y})'

# 이동 불가능한 좌표 설정
invalid_coordinates = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,3),(7,3),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),
                       (2,2),(2,3),(2,4),(3,1),(3,3),(3,5),(4,0),(4,1),(4,2),(4,4),(4,5),(4,6),(5,1),(5,3),(5,5),(6,2),
                       (6,3),(6,4)]
 
# 이동 불가능한 좌표 값을 변경
for coordinate in invalid_coordinates:
    x, y = coordinate
    yut_board[x][y] = '      '

# 판 출력
for x in yut_board: 
    print(' '.join(x))
 
 
