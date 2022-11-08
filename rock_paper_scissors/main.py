# making a rock, paper, scissors game

# player inputs a choice
# computer randomly selects a choice
# game returns output

# rock beats scissors
# scissors beats paper
# paper beats rock

import random

battle_map = {
    # dict is 'role': 'defeated_by'
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}


class Roll:
    """
    """
    def __init__(self, type, battle_map, roll=None) -> None:
        self.type = type
        self.roll_map = battle_map

    def defeated_by(self):
        return self.roll_map[type]


    #  would there be a single class for all rolls?


class Player:
    """
    """
    def __init__(self, name) -> None:
        self.name = name


def get_players_name():
    return input('Enter your name: ')

def main():
    print('rock, paper, scissors is about to begin!')
    name = get_players_name()

    player_1 = Player(name)
    player_2 = Player('cpu')

    game_loop(player_1, player_2)
    # print header
    # roll 3 times
    # print result

    # create a function for looping the game which includes the players, displays the results and displays the winner


def game_loop(player_1, player_2, n_games=3):
    count = 0
    running_score = []
    while count < n_games:
        count += 1
        
        print(f'players: {player_1.name} & {player_2.name}')

        # fix the control flow of error handling later
        while True:
            try:
                player_role = input(f'{player_1.name}, make your roll: ')
                player_role in battle_map.values()
            except ValueError:
                print('Sorry, I didnt understand that')
            else:
                break
        if player_role in battle_map.values():
            print(f'Successfully chosen {player_role}')
        else:
            print('Please select a valid role from {battle_map.values()}')
        
        player1_roll = Roll(
            type=player_role,
            battle_map=battle_map
        )
        print(f'{player_1.name} rolls {player1_roll.type}')
        player2_roll = Roll(
            random.choice(list(battle_map.values())),
            battle_map=battle_map
        )
        print(f'{player_2.name} rolls {player2_roll.type}')

        winner = None
        if player1_roll.type == player2_roll.type:
            pass
        elif battle_map[player1_roll.type] == player2_roll.type:
            winner = player_2.name
        else:
            winner = player_1.name    
        
        if winner == None:
            print('game is tied')
        else:
            print(f'{winner} wins')

    running_score.append(winner)
    print(f'overall winner is {max(set(running_score), key=running_score.count)}')


if __name__ == "__main__":
    main()
