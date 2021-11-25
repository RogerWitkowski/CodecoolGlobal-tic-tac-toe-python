from tabulate import tabulate
import random
import copy
import time


def start():
    logo = """ _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ \\
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|
                                        """
    print(logo)


def letter_to_number(letter):
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2


def changing_table(player, player_move, list):
    if len(player_move) == 2:
        row = int(player_move[1])
        column = letter_to_number(player_move[0])
        list[column][row] = player
        return list


def is_full(list):
    if list[0].count(".") > 0 or list[1].count(".") > 0 or list[2].count(".") > 0:
        return False
    else:
        return True


def has_won(list):
    for i in range(len(list)):
        if (list[i][1], list[i][2], list[i][3]) in [("X", "X", "X"), ("O", "O", "O")]:
            return True
    for i in range(1, len(list)+1):
        if (list[0][i], list[1][i], list[2][i]) in [("X", "X", "X"), ("O", "O", "O")]:
            return True
    if (list[0][1], list[1][2], list[2][3]) in [("X", "X", "X"), ("O", "O", "O")]:
        return True
    elif (list[0][3], list[1][2], list[2][1]) in [("X", "X", "X"), ("O", "O", "O")]:
        return True
    else:
        return False


def check_move(list):
    move_dict = {
        "A1": list[0][1],
        "A2": list[0][2],
        "A3": list[0][3],
        "B1": list[1][1],
        "B2": list[1][2],
        "B3": list[1][3],
        "C1": list[2][1],
        "C2": list[2][2],
        "C3": list[2][3]
    }
    while True:
        player_coordinates = (input("choose your coordinates: ").upper())
        if player_coordinates == "QUIT":
            exit()
        elif player_coordinates not in move_dict:
            print("The coordinates were entered in the wrong format")
            continue
        elif move_dict[player_coordinates] == ".":
            return player_coordinates
        else:
            print("This place is taken!")


def list_print(list):
    head = [" ", "1", "2", "3"]
    return(tabulate(list, headers=head, tablefmt="fancy_grid"))


def check_result(player, move, list):
    list = changing_table(player, move, list)
    print(list_print(list))
    if has_won(list) == True:
        print(f"{player} has won!")
        exit()
    elif is_full(list) == True:
        print("It's a tie!")
        exit()
    else:
        return None


def check_move_ai(list, possible_ai_move):
    while True:
        move_dict = {
            "A1": list[0][1],
            "A2": list[0][2],
            "A3": list[0][3],
            "B1": list[1][1],
            "B2": list[1][2],
            "B3": list[1][3],
            "C1": list[2][1],
            "C2": list[2][2],
            "C3": list[2][3]
        }
        if move_dict[possible_ai_move] == ".":
            return True
        else:
            return False


def get_list_copy(list):
    new_list = copy.deepcopy(list)
    return new_list


def changing_table_ai(computer_letter, possible_ai_move, copy):
    row = int(possible_ai_move[1])
    column = letter_to_number(possible_ai_move[0])
    copy[column][row] = computer_letter
    return copy


def choose_random_move_from_list(list, movesList):
    possible_moves = []
    for i in movesList:
        if check_move_ai(list, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(list, computer_letter):
    table = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'
    for i in table:
        copy = get_list_copy(list)
        if check_move_ai(copy, i):
            changing_table_ai(computer_letter, i, copy)
            if has_won(copy):
                return i
    for i in table:
        copy = get_list_copy(list)
        if check_move_ai(copy, i):
            changing_table_ai(player_letter, i, copy)
            if has_won(copy):
                return i

    if check_move_ai(list, "B2"):
        return "B2"

    move = choose_random_move_from_list(list, ("A1", "A3", "C1", "C3"))
    if move != None:
        return move

    return choose_random_move_from_list(list, ["A2", "B1", "B3", "C2"])


def tictactoe_game(mode):
    start()
    list = [['A', '.', '.', '.'], ['B', '.', '.', '.'], ['C', '.', '.', '.']]
    print(list_print(list))
    if mode == 'HUMAN-HUMAN':
        while True:
            player1 = "X"
            player2 = "O"
            player_move = check_move(list)
            check_result(player1, player_move, list)
            player2_move = check_move(list)
            check_result(player2, player2_move, list)
    elif mode == 'AI-HUMAN':
        while True:
            computer_letter = "X"
            player2 = "O"
            computer_move = get_computer_move(list, computer_letter)
            check_result(computer_letter, computer_move, list)
            player2_move = check_move(list)
            check_result(player2, player2_move, list)
    elif mode == 'HUMAN-AI':
        while True:
            computer_letter = "X"
            player2 = "O"
            player2_move = check_move(list)
            check_result(player2, player2_move, list)
            computer_move = get_computer_move(list, computer_letter)
            check_result(computer_letter, computer_move, list)
    elif mode == 'AI-AI':
        while True:
            delay_seconds = 1
            computer_letter = "X"
            computer_letter2 = "O"
            computer_move = get_computer_move(list, computer_letter)
            check_result(computer_letter, computer_move, list)
            time.sleep(delay_seconds)
            computer_move = get_computer_move(list, computer_letter2)
            check_result(computer_letter2, computer_move, list)
            time.sleep(delay_seconds)


def main_start():
    tictactoe_game('HUMAN-AI')


if __name__ == '__main__':
    main_start()
