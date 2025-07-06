import random

def play_369_game(players, user_name):

    print("\n--- 🎲 369 게임을 시작합니다! ---")
    
    total_players = len(players)
    
    for number in range(1, 51):
        current_player_index = (number - 1) % total_players
        current_player = players[current_player_index]
        
        s_number = str(number)
        clap_count = s_number.count('3') + s_number.count('6') + s_number.count('9')
        correct_answer = "짝" * clap_count if clap_count > 0 else s_number

        if current_player['name'] == user_name:
            user_input = input(f"당신의 차례 | -> ")
            if user_input != correct_answer:
                print(f"\n땡! 틀렸습니다. 정답은 '{correct_answer}' 입니다.")
                print(f"누가 술을 마셔 ~ {user_name}이가 술을 마셔 ~")
                return user_name  
        else:
            print(f"{current_player['name']} : {correct_answer}")

    print("\n이 게임 누가했어 ~ 이 게임 누가했어 ~")
    print("사용자가 완벽하게 성공했으므로 컴퓨터가 대신 마십니다!")
    
    computer_players = [p for p in players if p['name'] != user_name]
    if not computer_players:
        return None 

    loser = random.choice(computer_players)
    print(f"누가 술을 마셔 ~ {loser['name']}이가 술을 마셔 ~")
    return loser['name'] 