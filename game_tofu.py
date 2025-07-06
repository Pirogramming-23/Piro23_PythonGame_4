import time

def tofuGame(players):
    total_players = len(players)
    if total_players == 2:
        print(f"{players[0]} {players[1]}순으로 시계방향으로 앉아주세요.")
    elif total_players == 3:
        print(f"{players[0]} {players[1]} {players[2]}순으로 시계방향으로 앉아주세요.")
    else:
        print(f"{players[0]} {players[1]} {players[2]} {players[3]}순으로 시계방향으로 앉아주세요.")

    time.sleep(1.0)
    print("두부는 오른쪽으로 갈수록 증가합니다!")
    time.sleep(1.0)
    print("두부두부두부 으쌰으쌰으쌰으쌰 두~부두부두부 으쌰으쌰으쌰으쌰")

    current_player = 0

    print(f'시작은 {players[0]}!')
    while True:
        try:
            tofu_count = int(input('두부 몇 모?'))
            if 1 <= tofu_count <= 5:
                break
            else:
                print('1~5 사이의 숫자를 입력하세요.')
        except ValueError:
            print('숫자로 입력해주세요')

    while True:
        if tofu_count == 1:
            current_player = (current_player + 2) % total_players
        elif tofu_count == 2:
            current_player = (current_player + 1) % total_players
        elif tofu_count == 3:
            print('두부는 네모! 두부는 네모! 네모! 네모! 네모네모네모!!')
            return current_player
        elif tofu_count == 4:
            current_player = (current_player - 1 + total_players) % total_players
        else:
            current_player = (current_player - 2 + total_players) % total_players

        player, tofu_count = input('>> (입력 예시: (본인 이름) 4)').split() # 예외 처리 더하기
        tofu_count = int(tofu_count)

        if player != players[current_player]:
            print(f"둘이 한잔해~ 둘이 한잔해~ {player}, {players[current_player]}")
            return current_player
        # 3초 안에 입력이 없으면 
        
tofuGame(["지원", "지은", "재혁", "종현"])