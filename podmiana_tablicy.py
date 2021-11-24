def funkcja_podmiany_tablicy(player, player_move, list):
    '''changing coordinates'''
    if len(player_move) == 2:
        for i in range(len(player_move)):
            if player_move[0] == "A" or "B" or "C":
                return player_move[0]
            if player_move[1] == "1" or "2" or "3":
                return player_move[1]
    elif():
        print("Move looks like eg. A1")






    if player_move == "A1":
        list[0][1] = player
    elif player_move =="A2":
        list[0][2] = player
    elif player_move == "A3":
        list[0][3] = player
    elif player_move == "B1":
        list[1][1] = player
    elif player_move == "B2":
        list[1][2] = player
    elif player_move == "B3":
        list[1][3] = player
    elif player_move == "C1":
        list[2][1] = player
    elif player_move == "C2":
        list[2][2] = player
    elif player_move == "C3":
        list[2][3] = player
    return list