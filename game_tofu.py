import time
import random

def tofuGame(players_list, start_name):
    # players_list: list of dicts with keys 'name', 'limit', 'drinks'
    names = [player['name'] for player in players_list]
    total = len(names)

    # 안내 멘트
    print(f"{' '.join(names)} 순으로 시계방향으로 앉아주세요.")
    time.sleep(1.0)
    print("두부는 본인 기준으로 오른쪽으로 갈수록 증가합니다!")
    time.sleep(1.0)
    print("두부두부두부 으쌰으쌰으쌰으쌰 두~부두부두부 으쌰으쌰으쌰으쌰")

    # 시작 멤버를 지정된 사람으로 설정
    if start_name in names:
        current = names.index(start_name)
    else:
        current = 0
    print(f"시작은 {names[current]}!")

    # 첫 두부 입력
    while True:
        try:
            tofu = int(input('두부 몇 모? '))
            if 1 <= tofu <= 5:
                break
            print('1~5 사이의 숫자를 입력하세요.')
        except ValueError:
            print('숫자로 입력해주세요')

    # 게임 루프
    while True:
        if tofu == 1:
            current = (current + 2) % total
        elif tofu == 2:
            current = (current + 1) % total
        elif tofu == 3:
            print('두부는 네모! 두부는 네모! 네모! 네모! 네모네모네모!!')
            return names[current]
        elif tofu == 4:
            current = (current - 1) % total
        else:
            current = (current - 2) % total

        if names[current] != start_name:
            tofu = random.randint(1, 5)
            time.sleep(2.0)
            print(">> (입력 예시: 홍길동 4)", names[current], tofu)
            if tofu == 3:
                print("두부는 네모! 두부는 네모! 네모! 네모! 네모네모네모!!")
                return names[current]
            
        else:
            # 다음 입력: 플레이어 이름과 두부 수
            startTime = time.time()
            entry = input('>> (입력 예시: 홍길동 4) ').split()
            endTime = time.time()
            elapsed = endTime - startTime

            if elapsed > 3:
                print('너무 늦게 말했습니다!')
                return names[current]

            if len(entry) != 2:
                print('형식에 맞게 입력해주세요: (이름) (숫자)')
                continue
            try:
                tofu = int(entry[1])
                if tofu < 1 or tofu > 5:
                    print('1~5 사이의 숫자를 입력해주세요.')    
                    continue    
            except ValueError:
                print('두 번째 입력은 숫자여야 해요!')
                continue

