import main


def test_parser():
    inputData = """7 4
4 2
oooAAoo
ooDooBo
ooDooBo
oooCCoo"""

    fieldSize, coords, field = main.parser(inputData.split('\n'))

    assert fieldSize == [7, 4] \
           and coords == [4, 2] \
           and field == [['oooAAoo'], ['ooDooBo'], ['ooDooBo'], ['oooCCoo']]


def test_parserWrongFieldSize():
    inputData = """7 d
    4 2
    oooAAoo
    ooDooBo
    ooDooBo
    oooCCoo"""

    try:
        main.parser(inputData.split('\n'))
        assert False
    except IOError:
        assert True


def test_parserWrongCoordsSize():
    inputData = """7 4
    4 Z
    oooAAoo
    ooDooBo
    ooDooBo
    oooCCoo"""

    try:
        main.parser(inputData.split('\n'))
        assert False
    except IOError:
        assert True


def test_parserWrongWidthField():
    inputData = """7 4
    4 2
    oooAA
    ooDooBo
    ooDooBo
    oooCCoo"""

    try:
        main.parser(inputData.split('\n'))
        assert False
    except IOError:
        assert True


def test_parserWrongHeightField():
    inputData = """7 4
    4 2
    oooAAoo
    ooDooBo
    ooDooBo
    oooCCoo
    ooooooo"""

    try:
        main.parser(inputData.split('\n'))
        assert False
    except IOError:
        assert True


def test_fillNeighbors_firstCase():
    inputData = """7 4
4 2
oooAAoo
ooDooBo
ooDooBo
oooCCoo"""

    fillingSymbol = 'o'
    fieldSize, coords, field = main.parser(inputData.split('\n'))
    main.fillField(field, fieldSize, fillingSymbol, coords)
    assert field == [['oooAAoo'], ['ooDZZBo'], ['ooDZZBo'], ['oooCCoo']]


def test_fillNeighbors_secondCase():
    inputData = """7 4
4 2
oooXXoo
ooXooXo
ooXooXo
ooXooXo"""

    fillingSymbol = 'o'
    fieldSize, coords, field = main.parser(inputData.split('\n'))
    main.fillField(field, fieldSize, fillingSymbol, coords)
    assert field == [['oooXXoo'], ['ooXZZXo'], ['ooXZZXo'], ['ooXZZXo']]


def test_fillNeighbors_thirdCase():
    inputData = """7 4
4 2
oooXXoo
ooXooXo
oooooXo
ooXooXo"""

    fillingSymbol = 'o'
    fieldSize, coords, field = main.parser(inputData.split('\n'))
    main.fillField(field, fieldSize, fillingSymbol, coords)
    assert field == [['ZZZXXoo'], ['ZZXZZXo'], ['ZZZZZXo'], ['ZZXZZXo']]


def test_fillNeighbors_fourthCase():
    inputData = """10 10
1 1
oooooooooo
ooXooooooo
oXoXoooooo
ooXooooooo
oooooooooo
oooooXXXoo
oooooXooXo
oooooXooXo
oooooXoXoo
oooooooooo"""

    fillingSymbol = 'o'
    fieldSize, coords, field = main.parser(inputData.split('\n'))
    main.fillField(field, fieldSize, fillingSymbol, coords)
    assert field == [['ZZZZZZZZZZ'], ['ZZXZZZZZZZ'], ['ZXoXZZZZZZ'], ['ZZXZZZZZZZ'], ['ZZZZZZZZZZ'],
                     ['ZZZZZXXXZZ'], ['ZZZZZXZZXZ'], ['ZZZZZXZZXZ'], ['ZZZZZXZXZZ'], ['ZZZZZZZZZZ']]