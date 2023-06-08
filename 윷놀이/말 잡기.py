# 말 잡기 함수
def catching_a_horse(yut_py, yut_px, teams, current_team):
    catching_a_horse = None
    for team in teams.values():
        if team["name"] != teams[current_team]["name"]:
            for i in range(team["horse_count"]):
                if (team["horses"][i]["y"] == yut_py) and (team["horses"][i]["x"] == yut_px):
                    catching_a_horse = (team["name"], i)  
                    break   
            if catching_a_horse: 
                break  
    return catching_a_horse  
   
            
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

   

 
         

