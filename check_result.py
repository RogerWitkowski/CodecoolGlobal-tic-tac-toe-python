def check_result(player, move, list):
    list = funkcja_podmiany_tablicy(player, move, list)
    print(drukowanie_listy(list))
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
    list = [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ]]
    print(drukowanie_listy(list))
    while True:
        player1 = "x"
        player2 = "o"
        player_move = check_move(list)  #funkcja sprawdza czy koordynaty są zajęte oraz czy nie wychodzą poza tabelę. Zwraca True jeśli jest ok.
        check_result(player1, player_move, list)
        player_move2 = check_move(list) #funkcja sprawdza czy koordynaty są zajęte oraz czy nie wychodzą poza tabelę. Zwraca True jeśli jest ok.
        check_result(player2, player_move2, list)