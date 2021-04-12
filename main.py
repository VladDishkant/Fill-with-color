
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
            field[row-2].append(data[row])

            if len(field) > fieldSize[1]:
                try:
                    raise IOError('Height of field is equal {0}, but must be {1}!'
                                  .format(len(field), fieldSize[1]))
                except IOError:
                    print('Has been exception with FIELD!')
                    raise

            if len(field[row-2][0]) != fieldSize[0]:
                try:
                    raise IOError('Width of {0} row is equal {1}, but must be {2}!'
                                  .format(row-1, len(field[row-2][0]), fieldSize[0]))
                except IOError:
                    print('Has been exception with FIELD!')
                    raise
    return fieldSize, coords, field

if __name__ == "__main__":
    with open('inputData.txt', 'r', encoding='UTF-8') as file:
        inputData = file.read()
    fieldSize, coords, field = parser(inputData.split('\n'))
