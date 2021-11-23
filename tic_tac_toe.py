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
    print("\nFirst Player who starts is X, Enjoy & Have Fun! ;) \n")



def funkcja_podmiany_tablicy(player, player_coordinates, list):
    '''changing coordinates'''
    if player_coordinates == "A1":
        list[0][1] = player
    elif player_coordinates =="A2":
        list[0][2] = player
    elif player_coordinates == "A3":
        list[0][3] = player
    elif player_coordinates == "B1":
        list[1][1] = player
    elif player_coordinates == "B2":
        list[1][2] = player
    elif player_coordinates == "B3":
        list[1][3] = player
    elif player_coordinates == "C1":
        list[2][1] = player
    elif player_coordinates == "C2":
        list[2][2] = player
    elif player_coordinates == "C3":
        list[2][3] = player
    return list

def is_full(list):
    if "." in list:
        return False
    else:
        return True

def has_won(list):
    if ((list [0][1], list [0][2], list [0][3]) == ("x", "x", "x")) or ((list [0][1], list [0][2], list [0][3]) == ("o","o","o")):
        return True 
    elif ((list [1][1], list [1][2], list [1][3]) == ("x", "x", "x")) or ((list [1][1], list [1][2], list [1][3]) == ("o","o","o")):
        return True 
    elif ((list [2][1], list [2][2], list [2][3]) == ("x", "x", "x")) or ((list [2][1], list [2][2], list [2][3]) == ("o","o","o")):
        return True 
    elif ((list [0][1], list [1][1], list [2][1]) == ("x", "x", "x")) or ((list [0][1], list [1][1], list [2][1]) == ("o","o","o")):
        return True 
    elif ((list [0][2], list [1][2], list [2][2]) == ("x", "x", "x")) or ((list [0][2], list [1][2], list [2][2]) == ("o","o","o")):
        return True 
    elif ((list [0][3], list [1][3], list [2][3]) == ("x", "x", "x")) or ((list [0][3], list [1][3], list [2][3]) == ("o","o","o")):
        return True 
    elif ((list [0][1], list [1][2], list [2][3]) == ("x", "x", "x")) or ((list [0][1], list [1][2], list [2][3]) == ("o","o","o")):
        return True 
    elif ((list [0][3], list [1][2], list [2][1]) == ("x", "x", "x")) or ((list [0][3], list [1][2], list [2][1]) == ("o","o","o")):
        return True 
    else:
        return False

def check_move (list):
    while True:   
        player1_coordinates = (input ("choose your coordinates: ").upper())      
        if player1_coordinates == "QUIT":
            exit ()
        elif player1_coordinates == "A1":
            if list[0][1] == ".":
                return player1_coordinates 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates =="A2":
            if list[0][2] == ".":
                return player1_coordinates 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "A3":
            if list[0][3] == ".":
                return player1_coordinates 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "B1":
            if list[1][1] == ".":
                return player1_coordinates 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "B2":
            if list[1][2] == ".":
                return player1_coordinates 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "B3":
            if list[1][3] == ".":
                return player1_coordinates
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "C1":
            if list[2][1] == ".":
                return player1_coordinates
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "C2":
            if list[2][2] == ".":
                return player1_coordinates
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "C3":
            if list[2][3] == ".":
                return player1_coordinates
            else:
                print ("This place is taken!")
                continue 
        else:
            print ("The coordinates were entered in the wrong format")
            continue    

def drukowanie_listy(list):
    '''printing table'''
    head = [" ","1","2","3"]
    return(tabulate(list, headers=head, tablefmt="fancy_grid"))

def tictactoe_game(mode='HUMAN-HUMAN'):
    start()
    list = [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ]]
    while True:
        player1 = "x"
        player2 = "o"
        player_move = check_move(list)  #funkcja sprawdza czy koordynaty są zajęte oraz czy nie wychodzą poza tabelę. Zwraca True jeśli jest ok.
        list = funkcja_podmiany_tablicy(player1, player_move, list)
        print(drukowanie_listy(list))
        if has_won(list) == True:
            print("X has won!")
            exit()
        elif is_full(list) == True:
            print("it's a tie!")
            exit()
        else:
            pass
        player_move2 = check_move(list) #funkcja sprawdza czy koordynaty są zajęte oraz czy nie wychodzą poza tabelę. Zwraca True jeśli jest ok.
        list = funkcja_podmiany_tablicy(player2, player_move2, list)
        drukowanie_listy(list)
        if has_won(list) == True:
            print("O has won!")
            exit()
        elif is_full(list) == True:
            print("it's a tie!")
            exit()
        else:
            pass
        
def main_start():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_start()
