from tabulate import tabulate

# assign data
list = [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ] ]

# create header
head = [" ","1","2","3"]

# display table
print(tabulate(list, headers=head, tablefmt="fancy_grid"))


thisdict = {
  "A1": list [0][1],
  "A2": list [0][2],
  "A3": list [0][3],
  "B1": list [1][0],
  "B2": list [1][1],
  "B3": list [1][2],
  "C1": list [2][0],
  "C2": list [2][1],
  "C3": list [2][2]
}
user_choice = thisdict[input ("choice position:")]
user_choice = "x"
print(tabulate(list, headers=head, tablefmt="fancy_grid"))

print (input)
