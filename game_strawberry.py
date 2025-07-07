import time 
import random

def create_rhythm_sequences():
    """딸기 게임용 리듬 시퀀스를 생성합니다."""
    rhythm_list = []
    
    # 1~4번 패턴: 4박자 리듬
    for seq_num in range(1, 5):
        rhythm = ["X"] * 4
        for idx in range(seq_num):
            rhythm[3-idx] = "딸기"
        rhythm_list.append(rhythm)
    
    # 5~8번 패턴: 8박자 리듬  
    for seq_num in range(5, 9):
        rhythm = ["X"] * 8
        # 앞부분 4개는 모두 딸기
        for idx in range(4):
            rhythm[idx] = "딸기"
        # 뒷부분에 추가 딸기 배치
        for idx in range(seq_num - 4):
            rhythm[7-idx] = "딸기"
        rhythm_list.append(rhythm)
    
    return rhythm_list

def display_rhythm_with_timing(sequence):
    """리듬을 타이밍에 맞춰 화면에 표시합니다."""
    for item in sequence:
        print(item, end=' ', flush=True)
        time.sleep(0.3)
    print()

def get_mountain_pattern_indices():
    """산 모양(1~8,7~1) 인덱스 시퀀스를 반환합니다."""
    up = list(range(8))
    down = list(range(6, 0, -1))
    return up + down

def execute_strawberry_game(player_data, main_player):
    """딸기 게임 메인 실행 함수"""
    print("\n=== 🍓 딸기 게임 시작! ===")
    print("딸기가 좋아~ 딸기가 좋아~ 딸기! 딸기! 딸기!딸기!딸기\n")

    rhythm_sequences = create_rhythm_sequences()
    mountain_indices = get_mountain_pattern_indices()
    current_round = 0
    turn_index = 0
    player_count = len(player_data)
    mountain_length = len(mountain_indices)

    while True:
        # 산 모양 인덱스 사용
        pattern_idx = mountain_indices[current_round % mountain_length]
        active_player = player_data[turn_index % player_count]
        current_rhythm = rhythm_sequences[pattern_idx]
        correct_answer = ''.join(current_rhythm).lower()

        # 플레이어 입력 처리
        if active_player['name'] == main_player:
            player_input = input(f"{active_player['name']}님 차례!! 정확한 박자에 딸기를 입력해주세요 (예: 1번 - X X X 딸기): ").replace(" ", "").lower()
        else:
            # AI 플레이어 행동 결정 (90% 정답률)
            ai_success_rate = random.random()
            if ai_success_rate < 0.9:
                player_input = correct_answer
                print(f"{active_player['name']}님 차례: {player_input}")
            else:
                # AI가 실수하는 경우
                wrong_answer = list(correct_answer)
                if "딸기" in wrong_answer:
                    mistake_pos = wrong_answer.index("딸기")
                    wrong_answer[mistake_pos] = "x"
                else:
                    wrong_answer[0] = "딸기"
                player_input = ''.join(wrong_answer)
                print(f"{active_player['name']}님 차례: {player_input}")
            time.sleep(1)

        # 정답 체크
        if player_input != correct_answer:
            print("❌ 틀렸습니다! 정답은: ", end="")
            display_rhythm_with_timing(current_rhythm)
            print(f"{active_player['name']} 님은 하나 더 마신다!")
            
            # 게임 재시작 여부 확인
            restart_choice = input("딸기 게임을 처음부터 다시 할까요? (y/n): ").strip().lower()
            if restart_choice == "y":
                print("\n게임을 처음부터 다시 시작합니다!\n")
                current_round = 0
                turn_index = (turn_index + 1) % player_count  # 틀린 다음 사람부터 시작
                continue
            else:
                print("🍺 딸기 게임 종료!")
                return active_player['name']
        else:
            print(f"{active_player['name']} 정답!\n")

        current_round += 1
        turn_index += 1
