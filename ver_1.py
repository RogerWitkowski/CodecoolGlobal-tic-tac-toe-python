from tabulate import tabulate

# assign data
list = [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ] ]

# create header
head = [" ","1","2","3"]

# display table
print(tabulate(list, headers=head, tablefmt="fancy_grid"))

"""thisdict = {
  "A1": list [0][1],
  "A2": list [0][2],
  "A3": list [0][3],
  "B1": list [1][1],
  "B2": list [1][2],
  "B3": list [1][3],
  "C1": list [2][1],
  "C2": list [2][2],
  "C3": list [2][3]
}
user_choice = (thisdict[input ("choice position:")]).upper

list [user_choice] = "X"

print(tabulate(list, headers=head, tablefmt="fancy_grid"))
print (user_choice)"""

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
