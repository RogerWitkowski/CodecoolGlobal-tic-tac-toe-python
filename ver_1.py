from tabulate import tabulate


# assign data
list = [['A', '.','.','.' ],['B','.','.','.' ],['C', '.','.','.' ] ]

# create header
head = [" ","1","2","3"]

# display table
print(tabulate(list, headers=head, tablefmt="fancy_grid"))