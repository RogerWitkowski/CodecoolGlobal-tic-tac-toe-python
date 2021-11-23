list = [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ]]
def check_move (list):
    while True:   
        player1_coordinates = (input ("choose your coordinates: ").upper())      
        if player1_coordinates == "QUIT":
            exit ()
        elif player1_coordinates == "A1":
            if list[0][1] == ".":
                break 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates =="A2":
            if list[0][2] == ".":
                break 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "A3":
            if list[0][3] == ".":
                break 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "B1":
            if list[1][1] == ".":
                break 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "B2":
            if list[1][2] == ".":
                break 
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "B3":
            if list[1][3] == ".":
                break
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "C1":
            if list[2][1] == ".":
                break
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "C2":
            if list[2][2] == ".":
                break
            else:
                print ("This place is taken!")
                continue 
        elif player1_coordinates == "C3":
            if list[2][3] == ".":
                break
            else:
                print ("This place is taken!")
                continue 
        else:
            print ("The coordinates were entered in the wrong format")
            continue    
check_move (list)