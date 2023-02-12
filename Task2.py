import time
import random

def player_move(min_pick_up, max_pick_up):
    candy_out = -1
    while candy_out < min_pick_up or candy_out > max_pick_up:
        candy_out = int(input(f'Сколько конфет Вы забираете? '
            f'Введите количество от {min_pick_up} до {max_pick_up}: '))
        if min_pick_up > candy_out > max_pick_up:
            print(f'Вы хотите забрать {candy_out} конфет? А по правилам можно взять '
                f'не меньше {min_pick_up} и не больше {max_pick_up}, увы.')
    return candy_out

def win_algorithm(candy_on_table, min_pick_up, max_pick_up):
    return candy_on_table - candy_on_table // (min_pick_up + max_pick_up) * (min_pick_up + max_pick_up)

def bot_random(min_pick_up, max_pick_up):
    return random.randint(min_pick_up, max_pick_up)

def bot_intelligence(candy_on_table, min_pick_up, max_pick_up):
    way_num = win_algorithm(candy_on_table, min_pick_up, max_pick_up)
    if min_pick_up <= way_num < min_pick_up + max_pick_up:
        return way_num
    return random.randint(min_pick_up, max_pick_up)

def spelling(number_candies):
    spell = 'конфет'
    ones = [1, 21]
    twines = [2, 3, 4, 22, 23, 24]
    if number_candies in ones:
        spell = 'конфету'
    elif number_candies in twines:
        spell = 'конфеты' 
    return spell

candy_on_table = 121
min_pick_up = 1
max_pick_up = 28
player_1 = input('Вы - первый игрок, представьтесь, пожалуйста: ')
if input('Если Вы будете играть против другого игрока, введите "1": ') == '1':
    player_2 = input('Представьте, пожалуйста, своего противника: ')
else:
    player_2 = 'Bot'
player_dict = {1: player_1, 2: player_2}
bot_level = input('Если Вы хотите играть с продвинутым ботом, введите "1".\n'
    'Если с простеньким - любой другой символ: ')
if bot_level == '1':
    bot_level = int(bot_level)
else:
    bot_level = 2
hint = input('Если Вы желаете пользоваться подсказками по выигрышному алгоритму, введите 1.\n'
    'Если нет - любой другой символ: ')
if hint == '1':
    hint = int(hint)
else:
    hint = 2
print('Проводим жеребьёвку первого хода.')
player_num = int(time.time()//1%2+1)
print(f'Первым ходит {player_dict[player_num]}')
print('НАЧАЛИ!!!')
candy_out = 0
while candy_on_table > 0:
    if player_dict[player_num] != 'Bot':
        if hint == 1:
            print('Подсказка:')
            clue = win_algorithm(candy_on_table, min_pick_up, max_pick_up)
            if clue == 0:
                print('Ваш противник играет по выигрышному алгоритму, увы... так что берите сколько хотите.')
            else:
                print('Для выигрыша нужно взять '
                    f'{clue} {spelling(win_algorithm(candy_on_table, min_pick_up, max_pick_up))}.')
            print('---')
        candy_out = player_move(min_pick_up, max_pick_up)
    elif bot_level == 1:
        candy_out = bot_intelligence(candy_on_table, min_pick_up, max_pick_up)
    else:
        candy_out = bot_random(min_pick_up, max_pick_up)
    candy_on_table = candy_on_table - candy_out
    print(f'{player_dict[player_num]} забрал {candy_out} {spelling(candy_out)}.\n'
        f'На столе осталось {candy_on_table} {spelling(candy_on_table)}.')
    if player_num+1 > 2:
        player_num = 1
    else:
        player_num = 2
if player_num+1 > 2:
    player_num = 1
else:
    player_num = 2  
print('!!!')      
print(f'ИГРА ЗАВЕРШИЛАСЬ ПОБЕДОЙ ИГРОКА {player_dict[player_num]}!!!')
print()
