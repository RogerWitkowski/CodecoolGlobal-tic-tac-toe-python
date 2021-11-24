from tabulate import tabulate


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
    '''changing coordinates'''
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
    while True:
        thisdict = {
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
        player_coordinates = (input("choose your coordinates: ").upper())
        if player_coordinates == "QUIT":
            exit()
        elif player_coordinates not in thisdict:
            print("The coordinates were entered in the wrong format")
            continue
        elif thisdict[player_coordinates] == ".":
            return player_coordinates
        else:
            print("This place is taken!")


def list_print(list):
    '''printing table'''
    head = [" ", "1", "2", "3"]
    return(tabulate(list, headers=head, tablefmt="fancy_grid"))


def check_result(player, move, list):
    list = changing_table(player, move, list)
    print(list_print(list))
    if has_won(list) == True:
        print(f"{player} has won!")
        exit()
    elif is_full(list) == True:
        print("it's a tie!")
        exit()
    else:
        return None


def tictactoe_game(mode='HUMAN-HUMAN'):
    start()
    list = [['A', '.', '.', '.'], ['B', '.', '.', '.'], ['C', '.', '.', '.']]
    print(list_print(list))
    while True:
        player1 = "X"
        player2 = "O"
        # funkcja sprawdza czy koordynaty są zajęte oraz czy nie wychodzą poza tabelę. Zwraca True jeśli jest ok.
        player_move = check_move(list)
        # funckja podmienia index w liscie z "x" lub "o" i drukuje tabele. Sprawdza czy ktos wygral i czy jest jeszcze miejsce.
        check_result(player1, player_move, list)
        player2_move = check_move(list)
        check_result(player2, player2_move, list)


def main_start():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_start()
