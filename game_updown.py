import random
import time

# 색상 변수 정의
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'

def drink_animation():
    

    """술마시는 애니메이션"""
    drink_frames = [
        " ( ^_^)／  🍺",   # 잔을 듦
        " ( ^_^ )つ🍺",   # 입에 가까이
        " ( >_<)つ🍺",    # 마시는 중
        " ( ^o^)／   ( )", # 다 마심
        " ( @o@)／   ( )", # 취함
        " ( -_-)／   ( )", # 멍~
        " ( ^_^)／  🍺",   # 다시 잔을 듦
        " ( ^_^ )つ🍺",   # 반복
        " ( >_<)つ🍺",
        " ( ^o^)／   ( )",
        " ( @o@)／   ( )",
        " ( -_-)／   ( )"
    ]
    for _ in range(2):
        for frame in drink_frames:
            print(f"\r{frame}", end="", flush=True)
            time.sleep(0.25)
    print()

def congrats_animation():
    """정답 맞췄을 때 축하 애니메이션"""
    frames = [
        " ( ^o^)/★",
        " ( ^o^)/☆",
        " ( ^o^)/✨",
        " ( ^o^)/🎉",
        " ( ^o^)/",
        " ( ^o^)/✨",
        " ( ^o^)/☆",
        " ( ^o^)/★",
        " ( ^o^)/🎉"
    ]
    for _ in range(2):
        for frame in frames:
            print(f"\r{frame}", end="", flush=True)
            time.sleep(0.18)
            
def updown_game(players_list, name):
    INTRO = f"""
    {CYAN}{BOLD}
 _   _ ____  ____   _____        ___   _ 
| | | |  _ \|  _ \ / _ \ \      / / \ | |
| | | | |_) | | | | | | \ \ /\ / /|  \| |
| |_| |  __/| |_| | |_| |\ V  V / | |\  |
 \___/|_|   |____/ \___/  \_/\_/  |_| \_|

    {RESET}
    """
    print(INTRO)
    print('⬆️ 이번에는 업다운 게임 ⬇️')
    print(f'{CYAN}==============================================={RESET}')
    print('❗️ 기회는 모두 합쳐서 10번 ❗️')
    print('✅ 1 - 100사이의 숫자야') 
    print('🔺 업은 더 큰 숫자, 🔻 다운은 더 작은 숫자')

    number = random.randint(1, 100)
    count = 0
    current_player_index = 0
    wrong_player = None  # 틀린 사람 저장

    while count < 10:
            # 모든 플레이어가 순서대로 게임함
            current_player = players_list[current_player_index % len(players_list)]
            
            # 모든 차례에서 동일한 순서로 출력
            print(f'{CYAN}==============================================={RESET}')
            time.sleep(0.3)
            print(f'💡 {YELLOW}{count + 1}번째 시도야{RESET}')
            time.sleep(0.5)
            print(f'\n👤 {current_player["name"]} 차례야!')
            time.sleep(0.5)
            
            # 내차례는 직접 입력, 다른 사람들은 자동
            if current_player["name"] == name:
                try:
                    guess = int(input(f'🔢 숫자를 맞혀봐 ▶ '))
                    count += 1

                    # 정답 체크 (내 차례)
                    if guess < number:
                        print(f'{RED}🔺 업! 더 큰 숫자라구{RESET}')
                        time.sleep(0.7)
                    elif guess > number:
                        print(f'{RED}🔻 다운! 더 작은 숫자야{RESET}')
                        time.sleep(0.7)
                    else: 
                        print(f'{RED}==============================================={RESET}')
                        print(f'{GREEN} {current_player["name"]} 정답이야! 🎉{RESET}')
                        congrats_animation()
                        
                        return None 

                    current_player_index += 1
                except ValueError:
                    print(f'{RED}❌ 숫자를 말해줘야해!{RESET}')
                    time.sleep(0.5)
                    continue
            else:
                # 다른 사람들은 한 번씩 처리 (자동 출력)
                guess = random.randint(1, 100)
                print(f'🔢 {current_player["name"]}: {guess}')
                time.sleep(0.7)
                count += 1

                if guess < number:
                    print(f'{RED}🔺 업! 더 큰 숫자라구{RESET}')
                    time.sleep(0.7)
                elif guess > number:
                    print(f'{RED}🔻 다운! 더 작은 숫자야{RESET}')
                    time.sleep(0.7)
                else: 
                    print(f'{RED}==============================================={RESET}')
                    print(f'{GREEN} {current_player["name"]} 정답이야! 🎉{RESET}')
                    congrats_animation()
                    
                    return None 

                time.sleep(0.3)
                current_player_index += 1
            
            if count >= 10:
                break

    print(f'{CYAN}==============================================={RESET}')
    print(f'{RED}💀 모두 틀려서 기회가 끝났어 💀{RESET}')
    print(f"{GREEN}정답은 {number}!{RESET}")
    print(f'{RED}==============================================={RESET}')
    
    # 10번 기회가 끝나면 마지막에 게임을 진행한 사람이 틀린 사람
    last_player = players_list[(current_player_index - 1) % len(players_list)]
    print(f"{BOLD} 🍺 술이 들어간다 쭉쭉~쭉쭉 {last_player['name']} 원샷~! 🍺{RESET}")
    drink_animation()
    return last_player["name"]




