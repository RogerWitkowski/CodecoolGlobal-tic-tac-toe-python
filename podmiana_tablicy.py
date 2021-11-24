def letter_to_number(letter):
    if letter ==  "A":
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