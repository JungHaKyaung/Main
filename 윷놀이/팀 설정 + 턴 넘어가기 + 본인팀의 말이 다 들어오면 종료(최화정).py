# 아직은 코드가 좀 이상함 
# 팀 이름 선택 가능, 팀에 몇 명 들어갈지 선택 가능, 어느팀부터 시작할지 (아마 랜덤으로) 선택 가능
# 윷 던질 때 무슨 팀이 던지고 있는지 표시함 
# 윷놀이 점수표 만들기

 
 
import random

# 윷놀이 판 정의
yut_board = {
    1: "도",
    2: "개",
    3: "걸",
    4: "윷",
    5: "모"
}

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
    for i in range(4):
        yut = random.randint(1, 2)
        yut_result.append(yut)
    return yut_result

# 윷의 결과를 해석하는 함수 정의
def interpret_yut(yut_result):
    back_do_count = 0
    for yut in yut_result:
        if yut == 1:
            back_do_count += 1
    if back_do_count == 0:
        if sum(yut_result) == 4:
            return "윷"
        elif sum(yut_result) == 5:
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

# 윷놀이 실행
num_teams = 2
num_players_per_team = int(input("한 팀에 몇 명이 들어갈지 입력하세요: "))
print("%d개의 팀이 있으며, 한 팀당 %d명씩 참가합니다!" % (num_teams, num_players_per_team))

teams = set_teams(num_teams, num_players_per_team)
current_team = int(input("먼저 시작할 팀을 선택하세요 (0 또는 1): "))

while True:
    current_team_name = teams[current_team]["name"]

    enter_button = input(f"{current_team_name} 팀의 차례입니다. Enter를 누르면 윷을 던집니다. (아무거나 입력하면 종료됩니다.)")

    if enter_button == "":
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

        teams[current_team]["score"] += 1

        current_team = next_turn(current_team, num_teams)

    else:
        print("게임이 종료되었습니다.")
        break
