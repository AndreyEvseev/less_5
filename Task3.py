def field_printing(field: list):
    for i in range(len(field)):
        st_lel = ''
        for j in range(len(field)):
            st_lel += str(field[i][j])
        print(st_lel)

def user_input(coordinate: str) -> int: 
    inp = 0
    while inp/2 < 1 or inp/2 >3: 
        inp = 2*int(input(f'Введите номер столбца (1<={coordinate}<=3): '))
        if inp/2 < 1 or inp/2 >3:
            print(f'Введено некорректное значение: {int(inp/2)}')
    return inp

def check_for_win(play_list: list, player: int):
    win = 0
    diag_down, dag_up = '', ''
    for i in range(2, len(play_list), 2):
        diag_down += play_list[i][i]
        dag_up += play_list[i][len(play_list)-i]
        line, column = '', ''
        for j in range(2, len(play_list), 2):
            line += play_list[i][j]
            column += play_list[j][i]
        win = max(win, line.count(simbol_dict[player]), 
            column.count(simbol_dict[player]))
    win = max(win, diag_down.count(simbol_dict[player]),
                dag_up.count(simbol_dict[player]))
    return win

field =  [['   ', '   ', ' b1', '   ', ' b2', '   ', ' b3', '   '],
    ['  ', '  -', '---', '---', '---', '---', '---', '---'],
        ['a1 ', ' | ', '   ', ' | ', '   ', ' | ', '   ', ' | '],
            ['  ', '  -', '---', '---', '---', '---', '---', '---'],
                ['a2 ', ' | ', '   ', ' | ', '   ', ' | ', '   ', ' | '],
                    ['  ', '  -', '---', '---', '---', '---', '---', '---'],
                        ['a3 ', ' | ', '   ', ' | ', '   ', ' | ', '   ', ' | '],
                            ['  ', '  -', '---', '---', '---', '---', '---', '---']]
move_dict = {1: 'Ход первого игрока:', 0: 'Ход второго игрока:'}
simbol_dict = {1: ' Х ', 0: ' O '}
win_dict = {1: 'Победил первый игрок! Крестики рулят!', 0: 'Победил второй игрок! Нолики forever!'}
print('Играем в "Крестики - нолики". Первый игрок ходит Х, второй - О. ')
field_printing(field)
player_move = 1
win_flag = False
while player_move < 10 and not win_flag:
    player = player_move % 2
    move_flag = False
    while not move_flag:
        print(move_dict[player])
        a = user_input('a')
        b = user_input('b')
        if field[a][b] == '   ':
            field[a][b] = simbol_dict[player]
            move_flag = True
        else:
            print('Выбранная ячейка занята, выберите другую ячейку.')
    field_printing(field)
    if player_move > 4:    
        if check_for_win(field, player) == 3:
            win_flag = True
            print(win_dict[player])
    player_move += 1
if win_flag == False:
    print('Игра была равна - играли два значка: крестик и нолик.')    