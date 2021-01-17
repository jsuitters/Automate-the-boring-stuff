tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    widest = []
    for x in range(len(table)):
        n = 0
        q = 0
        for y in range(len(table[0])):
            if n < len(table[x][y]):
                n = len(table[x][y])
                z = y
        widest.append(table[x][z])

    for y in range(len(table[0])):
        for x in range(len(table)):
            offset = len(widest[x])
            print(table[x][y].rjust(offset) + " ", end="")
        print("")

print_table(tableData)
