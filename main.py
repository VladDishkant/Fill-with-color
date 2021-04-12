

"""Parsing data
    @params data -> our data from file

    @return fieldSize, coords, field -> where:
                                            fieldSize - size field Width and Height,
                                            coords - start point for filling,
                                            field - our field which we must filling"""


def parser(data):
    fieldSize = []
    coords = []
    field = []

    for row in range(len(data)):
        if row == 0:
            fieldSize = data[row].split(' ')
            fieldSize = list(map(int, filter(lambda x: x.isdigit(), fieldSize)))
            if len(fieldSize) != 2:
                try:
                    raise IOError('Field size must be 2 integers space separated!')
                except IOError:
                    print('Has been exception with point out SIZE OF FIELD!')
                    raise
        elif row == 1:
            coords = data[row].split(' ')
            coords = list(map(int, filter(lambda x: x.isdigit(), coords)))
            if len(coords) != 2:
                try:
                    raise IOError('Coords size must be 2 integers space separated!')
                except IOError:
                    print('Has been exception with point out size of COORDS!')
                    raise
        else:
            field.append([])
            field[row - 2].append(data[row])

            if len(field) > fieldSize[1]:
                try:
                    raise IOError('Height of field is equal {0}, but must be {1}!'
                                  .format(len(field), fieldSize[1]))
                except IOError:
                    print('Has been exception with FIELD!')
                    raise

            if len(field[row - 2][0]) != fieldSize[0]:
                try:
                    raise IOError('Width of {0} row is equal {1}, but must be {2}!'
                                  .format(row - 1, len(field[row - 2][0]), fieldSize[0]))
                except IOError:
                    print('Has been exception with FIELD!')
                    raise
    return fieldSize, coords, field


"""Filling our field
    @params field -> our field which we must filling
    @params fieldSize -> size field Width and Height
    @params fillingSymbol -> which symbol we must filling in the field
    @params coords -> start point for filling"""


def fillField(field, fieldSize, fillingSymbol, coords):
    coords = list(map(lambda x: x - 1, coords))
    unverifiedNeighbors = []

    while True:
        for i in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            row = coords[1] + i[1]
            column = coords[0] + i[0]

            if row == -1 or column == -1 or row == fieldSize[1] or column == fieldSize[0]: continue

            if field[row][0][column] == fillingSymbol:
                field[row][0] = field[row][0][:column] + 'Z' + field[row][0][column + 1:]
                unverifiedNeighbors.append([])
                unverifiedNeighbors[len(unverifiedNeighbors) - 1].append(column)
                unverifiedNeighbors[len(unverifiedNeighbors) - 1].append(row)
        if len(unverifiedNeighbors) == 0:
            break
        else:
            coords = unverifiedNeighbors.pop(len(unverifiedNeighbors) - 1)


"""Starting point of the program"""
if __name__ == "__main__":
    with open('inputData.txt', 'r', encoding='UTF-8') as file:
        inputData = file.read()
    fillingSymbol = 'o'
    fieldSize, coords, field = parser(inputData.split('\n'))
    print("Before:")
    for i in field: print(i[0])
    fillField(field, fieldSize, fillingSymbol, coords)
    print("\nAfter:")
    for i in field: print(i[0])
