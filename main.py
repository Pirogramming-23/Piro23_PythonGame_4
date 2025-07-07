import time
import random
import game_369
import game_updown
import game_tofu
import game_strawberry
import game_metro

drinkMax = 0  # name의 치사량
name = ""  # 이름
friends = {"은서": 2, "하연": 4, "연서": 8, "예진": 8, "헌도": 6}  # 함께 할 친구들 dict
friendsNum = 0  # 친구 명수
GameMembers = {}  # 함께 게임을 진행할 친구들 dict
startMember = ""    # 게임 번호를 고르는 사람
gameNum = 0     # 선택한 게임 번호
drinkNow = {}   # 이름 : 현재까지 마신 양 dict
drunkFriend = ""    # 치사량이 0인 사람
ifContinue = ""     # 게임 지속 여부
loseMember = ""    # 게임에서 진 사람

def gameStart() :
    global GameMembers, gameNum, loseMember, name, drinkNow
    startMember = random.choice(list(GameMembers.keys()))
    while True :
        try :
            gameNum = int(input(f"{startMember}(이)가~ 좋아하는~ 랜덤~게임~! 랜덤~게임! 무슨~게임? : "))
            if 1<= gameNum <=5 :
                break
            else :
                print("1~5 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    time.sleep(1.0)
    print(f"{startMember} 님이 게임을 선택하셨습니다!🤩")

    print("""
    ____________________________________________________________________________________________________________________
    ____________________________________________________________________________________________________________________
    
      _   _ _               _____
     | \ | (_)             / ____|
     |  \| |_  ___ ___    | |  __  __ _ _ __ ___   ___
     | .   | |/ __/ _ \   | | |_ |/ _` | '_ ` _ \ / _
     | |\  | | (_|  __/   | |__| | (_| | | | | | |  __/
     |_| \_|_|\___\___|    \_____|\__,_|_| |_| |_|\___|
     
    ____________________________________________________________________________________________________________________
    ____________________________________________________________________________________________________________________
    """)
    time.sleep(1.0)

    if gameNum == 1 :
        players_list = []
        for player_name in GameMembers:
            players_list.append({
                'name': player_name,
                'limit': GameMembers[player_name],
                'drinks': drinkNow[player_name]
            })

        loser_name = game_369.play_369_game(players_list, name)

        if loser_name:
            loseMember = loser_name  
            drinkNow[loseMember] += 1 
            print(f"\n결과: {loseMember}님이 벌주 당첨! (현재 {drinkNow[loseMember]}잔)")
        else:
            print("\n결과: 이번 라운드는 무승부입니다!")

    elif gameNum == 2 :
        players_list = []
        for player_name in GameMembers:
            players_list.append({
                'name': player_name,
                'limit': GameMembers[player_name],
                'drinks': drinkNow[player_name]
            })

        loser_name = game_updown.updown_game(players_list, name)

        if loser_name:
            loseMember = loser_name  
            drinkNow[loseMember] += 1 
            print(f"\n결과: {loseMember}님이 벌주 당첨! (현재 {drinkNow[loseMember]}잔)")
        else:
            print("\n결과: 이번 라운드는 무승부입니다!")
            
    elif gameNum == 3 :
        players_list = []
        for player_name in GameMembers:
            players_list.append({
                'name': player_name,
                'limit': GameMembers[player_name],
                'drinks': drinkNow[player_name]
            })

        loser_name = game_tofu.tofuGame(players_list, name)

        if loser_name:
            loseMember = loser_name  
            drinkNow[loseMember] += 1 
            print(f"\n결과: {loseMember}님이 벌주 당첨! (현재 {drinkNow[loseMember]}잔)")
        else:
            print("\n결과: 이번 라운드는 무승부입니다!")

    elif gameNum == 4 :
        players_list = []
        for player_name in GameMembers:
            players_list.append({
                'name': player_name,
                'limit': GameMembers[player_name],
                'drinks': drinkNow[player_name]
            })

        loser_name = game_strawberry.execute_strawberry_game(players_list, name)

        if loser_name:
            loseMember = loser_name  
            drinkNow[loseMember] += 1 
            print(f"\n결과: {loseMember}님이 벌주 당첨! (현재 {drinkNow[loseMember]}잔)")
        else:
            print("\n결과: 이번 라운드는 무승부입니다!")

    elif gameNum == 5 :
        players_list = []
        for player_name in GameMembers:
            players_list.append({
                'name': player_name,
                'limit': GameMembers[player_name],
                'drinks': drinkNow[player_name]
            })

        loser_name = game_metro.metroGame(players_list, name)

        if loser_name:
            loseMember = loser_name
            drinkNow[loseMember] += 1
            print(f"\n결과: {loseMember}님이 벌주 당첨! (현재 {drinkNow[loseMember]}잔)")
        else:
            print("\n결과: 이번 라운드는 무승부입니다!")
            
    time.sleep(1.0)
    gameContinue()

def gameContinue() :
    global drunkFriend, ifContinue
    for key in GameMembers.keys():
        remaining_drinks = GameMembers[key] - drinkNow[key]
        print(f"{key}은(는) 지금까지 {drinkNow[key]}🍺! 치사량까지 {remaining_drinks}잔 남음")
        
        # '현재 마신 양'이 '최대 주량'보다 크거나 같아지면 게임 종료
        if drinkNow[key] >= GameMembers[key]:
            drunkFriend = key  # 전사한 친구의 이름을 기록
            break # 더 이상 확인할 필요 없으므로 반복문 탈출

    time.sleep(1.0)

    if drunkFriend:
        print(f"""
        ________________________________________________________________________________________________________________
        ________________________________________________________________________________________________________________
        
          ____    _    __  __ _____     _____   __     __ ______  _____  
         / ___|  / \  |  \/  | ____|  / _____ \ \ \   / /|  ____|| ____ |
        | |  _  / _ \ | |\/| |  _|    | |   | |  \ \ / / |  _|  |  |__| |_ 
        | |_| |/ ___ \| |  | | |___   | |___| |   \ V /  | |___ |  |____  |
         \____/_/   \_\_|  |_|_____|   \_____/     \_/   |_____||__|    |_|
         
         _______________________________________________________________________________________________________________
         _______________________________________________________________________________________________________________
         
        {drunkFriend}가 전사했습니다... 꿈나라에서는 편히 쉬시길...zzz
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
        time.sleep(1.0)
        print("""
                                        🍺 다음에 술 마시면 또 불러주세요~ 안녕! 🍺
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
        return

    print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  🍺 오늘의 Alchol GAME 🍺  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                        🍺 1. 369 게임
                                                        🍺 2. 업다운 게임
                                                        🍺 3. 두부 게임
                                                        🍺 4. 딸기 게임
                                                        🍺 5. 지하철 게임
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
    time.sleep(1.0)
    ifContinue = input("술게임 진행 중! 다른 사람의 턴입니다. 그만하고 싶으면 'exit'를, 계속하고 싶으면 아무거나 입력해 주세요! : ")
    if ifContinue != "exit" :
        gameStart()

## 게임 시작 ##

time.sleep(1.0)
print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    _      _       ____  _   _     U  ___ u  _   _     U  ___ u   _            ____      _      __  __  U _____ u
U  /"\  u |"|   U /"___||'| |'|     \/"_ \/ |'| |'|     \/"_ \/  |"|        U /"___|uU  /"\  uU|' \/ '|u\| ___"|/
 \/ _ \/U | | u /| | u /| |_| |\    | | | |/| |_| |\    | | | |U | | u      \| |  _ / \/ _ \/ \| |\/| |/ |  _|"
 / ___ \ \| |/__ | |/__U|  _  |u.-,_| |_| |U|  _  |u.-,_| |_| | \| |/__      | |_| |  / ___ \  | |  | |  | |___
/_/   \_\ |_____| \____||_| |_|  \_)-\___/  |_| |_|  \_)-\___/   |_____|      \____| /_/   \_\ |_|  |_|  |_____|
 \    >> //  \ _// \ //   \       \    //   \       \     //  \       _)(|_   \    >><<,-,,-.   <<   >>
(__)  (__|")("_|__)(__|_") ("_)      (__)  (_") ("_)     (__)   (_")("_)     (__)__) (__)  (__)(./  \.) (__) (__)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ใ(^▽^ )ว ใ(^▽^ )ว             🍾🍺🍻🥂안주 먹을🍗 시간이⏰ 없어요❌ 마시면서 배우는 술게임🍾🍺🍻🥂             ใ(^▽^ )วใ(^▽^ )ว
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
time.sleep(1.0)
q = input("게임을 진행할까요? (y/n) : ")
if q == "y" :
    time.sleep(1.0)
    name = input("오늘 거하게 취해볼 당신의 이름은? : ")
    time.sleep(1.0)

    print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍺 소주 기준 당신의 주량은? 🍺~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                    🍺 1. 소주 반 병 (2잔)
                                                    🍺 2. 소주 반 병에서 한병 (4잔)
                                                    🍺 3. 소주 한병에서 한병 반 (6잔)
                                                    🍺 4. 소주 한병 반에서 두병 (8잔)
                                                    🍺 5. 소주 두병 이상 (10잔)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
    time.sleep(1.0)
    while True:
        try:
            drinkMax = int(input("당신의 치사량(주량)은 얼마만큼인가요?(1~5를 선택해주세요.) : "))
            if 1 <= drinkMax <= 5:
                break
            else:
                print("1~5 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

    GameMembers[name] = drinkMax * 2
    drinkNow[name] = 0
    time.sleep(1.0)

    while True:
        try:
            friendsNum = int(input("함께 취할 친구들은 얼마나 필요하신가요? (최대 3명까지 초대할 수 있어요!) : "))
            if 1 <= friendsNum <= 3:
                break
            else:
                print("1~3 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

    while True :
        randomMember = random.choice(list(friends.keys()))
        if randomMember in GameMembers.keys() :
            continue
        GameMembers[randomMember] = friends[randomMember]
        drinkNow[randomMember] = 0
        print(f"오늘 함께 취할 친구는 {randomMember}입니다! (치사량 : {GameMembers[randomMember]})")
        if len(drinkNow) == friendsNum+1 :
            break

    time.sleep(1.0)

    print(f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
    for key, value in GameMembers.items():
        print(f"{key}은(는) 지금까지 {drinkNow[key]}🍺! 치사량까지 {value}")

    time.sleep(1.0)

    print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  🍺 오늘의 Alchol GAME 🍺  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                    🍺 1. 369 게임
                                                    🍺 2. 업다운 게임
                                                    🍺 3. 두부 게임
                                                    🍺 4. 딸기 게임
                                                    🍺 5. 지하철 게임
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

    time.sleep(1.0)
    gameStart()