import random

# 윷놀이 판 정의
yut_board = {
    0: "시작",
    1: "도",
    2: "개",
    3: "걸",
    4: "윷",
    5: "모",
    6: "도착"
}

player_positions = [[0, 0, 0] for _ in range(2)]  # 플레이어 위치 


# 팀 설정
def set_teams(num_teams, num_players_per_team):
    teams = {}
    for i in range(num_teams):
        team_name = input("팀 이름을 입력하세요: ")
        teams[i] = {"name": team_name, "score": 0, "horse_count": num_players_per_team}
    return teams


# 턴 넘어가기
def next_turn(current_team, num_teams):
    current_team = (current_team + 1) % num_teams
    return current_team


# 윷을 던지는 함수 정의
def throw_yut():
    yut_result = []
    for _ in range(4):
        yut = random.randint(1, 2)
        yut_result.append(yut)
    return yut_result


# 윷의 결과를 해석하는 함수 정의
def interpret_yut(yut_result):
    back_do_count = yut_result.count(1)
    if back_do_count == 0:
        if sum(yut_result) == 8:
            return "윷"
        elif sum(yut_result) == 9:
            return "모"
        else:
            return yut_board[sum(yut_result)]
    elif back_do_count == 1:
        return "걸"
    elif back_do_count == 2:
        return "개"
    elif back_do_count == 3:
        return "도"
    else:
        return "잘못된 결과입니다."


def move_piece(current_team, piece_index):
    current_position = player_positions[current_team][piece_index]

    if current_position == len(yut_board) - 1:
        return  # 이미 도착지점에 도착한 경우, 움직이지 않습니다.

    yut_interpret = interpret_yut(yut_result)
    next_position = current_position + int(yut_interpret != "도착")  # 도착지점이 아닌 경우에만 이동
    current_cell = yut_board[current_position]
    player_positions[current_team][piece_index] = next_position
    next_cell = yut_board[next_position]

    print(f"[{teams[current_team]['name']} 팀 말 {piece_index+1}] {current_cell}에서 {next_cell}로 이동했습니다.")

    # 도착지점에 도착한 경우
    if next_position == len(yut_board) - 1:
        print(f"[{teams[current_team]['name']} 팀 말 {piece_index+1}] 도착!")
        teams[current_team]["score"] += 1


# 윷놀이 실행
num_teams = 2
num_players_per_team = int(input("한 팀에 몇 명이 들어갈지 입력하세요: "))
print("%d개의 팀이 있으며, 한 팀당 %d명씩 참가합니다!" % (num_teams, num_players_per_team))

teams = set_teams(num_teams, num_players_per_team)

current_team = int(input("먼저 시작할 팀을 선택하세요 (0 또는 1): "))
print()

while True:
    current_team_name = teams[current_team]["name"]

    enter_button = input(f"{current_team_name} 팀의 차례입니다. Enter를 누르면 윷을 던집니다. (아무거나 입력하면 종료됩니다.)")

    if enter_button != "":
        print("게임이 종료되었습니다.")
        break

    yut_result = throw_yut()
    print("윷의 결과:", yut_result)
    yut_interpret = interpret_yut(yut_result)
    print("해석 결과:", yut_interpret)

    if yut_interpret == "잘못된 결과입니다.":
        break
    elif yut_interpret == "도":
        print("한 바퀴 돌았습니다!")
    elif yut_interpret == "모":
        print("한 바퀴 돌았으며, 한 번 더 던집니다.")

    moveable_pieces = [i for i, position in enumerate(player_positions[current_team]) if position < len(yut_board) - 1]

    if not moveable_pieces:
        print("움직일 말이 없습니다.")
        continue

    print("이동 가능한 말:", ", ".join([f"말 {i+1}" for i in moveable_pieces]))

    piece_index = -1
    while piece_index not in moveable_pieces:
        piece_index = int(input("이동할 말 번호를 선택하세요: ")) - 1

    move_piece(current_team, piece_index)

    # 모든 말이 도착한 경우
    if all(position == len(yut_board) - 1 for position in player_positions[current_team]):
        print(f"[{teams[current_team]['name']}] 모든 말이 도착!")

    current_team = next_turn(current_team, num_teams)
    
