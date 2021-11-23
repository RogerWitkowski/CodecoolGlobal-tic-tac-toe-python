def tictactoe_game(mode='HUMAN-HUMAN'):
    menu()
    list = [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ]]
    while True:
        player1 = "x"
        player2 = "o"
        while check_move != True:
            player1_coordinates = input("Choose coordinates: ")
            check_move(player1_coordinates) #funkcja sprawdza czy koordynaty są zajęte oraz czy nie wychodzą poza tabelę. Zwraca True jeśli jest ok.
        list = funkcja_podmiany_tablicy(player1, player1_coordinates, list)
        funkcja_print_tabela(list)
        if has_won(list) == True:
            print("X has won!")
            exit()
        elif is_full(list) == True:
            print("it's a tie!")
            exit()
        else:
            pass
        while check_move != True:
            player2_coordinates = input("Choose coordinates: ")
            check_move(player2_coordinates) #funkcja sprawdza czy koordynaty są zajęte oraz czy nie wychodzą poza tabelę. Zwraca True jeśli jest ok.
        list = funkcja_podmiany_tablicy(player2, player2_coordinates, list)
        funkcja_print_tabela(list)
        if has_won(list) == True:
            print("O has won!")
            exit()
        elif is_full(list) == True:
            print("it's a tie!")
            exit()
        else:
            pass
        


    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
