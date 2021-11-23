from tabulate import tabulate
def funkcja_podmiany_tablicy(player, player_coordinates, list):
    A1 = list[0][1]
    A2 = list[0][2]
    A3 = list[0][3]
    B1 = list[1][1]
    B2 = list[1][2]
    B3 = list[1][3]
    C1 = list[2][1]
    C2 = list[2][2]
    C3 = list[2][3]
    # print(a1, a2, a3)
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
#print(funkcja_podmiany_tablicy("x", "A1", [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ] ]))

def drukowanie_listy(list):
    head = [" ","1","2","3"]
    print(tabulate(list, headers=head, tablefmt="fancy_grid"))


def menu():
    a = funkcja_podmiany_tablicy("x", "A1", [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ] ])
    drukowanie_listy(a)
menu()
