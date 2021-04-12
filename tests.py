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
