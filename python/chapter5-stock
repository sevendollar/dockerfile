ta = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dog', 'cats', 'moose', 'goose']]


def printable(tableData, symbol=' '):
    tmp = ''
    max_word = [0] * len(tableData)
    for line in range(len(tableData)):

        for word in range(len(tableData[line])):
            if max_word[line] < int(len(tableData[line][word])):
                max_word[line] = len(tableData[line][word])
    for x in range(len(tableData[-1])):
        for y in range(len(max_word)):
            tmp = tmp + ' ' + tableData[y][x].rjust(max_word[y], symbol)
        tmp += '\n'
    print(tmp)

printable(tableData)
