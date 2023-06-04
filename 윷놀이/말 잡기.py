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
