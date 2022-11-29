#!/usr/bin/python3
import os
import time

pos = [["_", "_", "_"],
       ["_", "_", "_"],
       ["_", "_", "_"]]


def tic-toc-toe-game():
    select = "X"
    player = 1
    status = True
    while status:
        __screen()
        option = input(
            f'Choose the column followed by the line number - Eg: b2 \n(Type q for quit) [Player {player}]: ')
        if "q" in option or "quit" in option:
            status: False
            break
        if not option or len(option) != 2:
            print("\nERROR: Invalid entry! Try again!\n")
            time.sleep(2)
            pass
        else:
            lst = []
            for m in option:
                lst.append(m)
            column = lst[0]
            line = lst[1]
            if 'a' not in column and 'b' not in column and 'c' not in column:
                print("\nERROR: Select one column between a, b or c\n")
                time.sleep(2)
                pass
            elif '1' not in line and '2' not in line and '3' not in line:
                print("\nERROR: Select one line between 1, 2 or 3")
                time.sleep(2)
                pass
            else:
                if column == 'a': matrix = 0
                elif column == 'b': matrix = 1
                else: matrix = 2
                if pos[int(matrix)][int(line) - 1] != "_":
                    print("\nERROR:Option already selected! Select another option")
                    time.sleep(2)
                else:
                    pos[int(matrix)][int(line) - 1] = select
                    status = __check_game(select, player)
                    player, select = __change_player(player, select)
        if status: os.system('clear')


def __check_game(select, player):
    status = True
    if pos[0][0] == select and pos[0][1] == select and pos[0][2] == select:
        status = __action(player, select)
    if pos[1][0] == select and pos[1][1] == select and pos[1][2] == select:
        status = __action(player, select)
    if pos[2][0] == select and pos[2][1] == select and pos[2][2] == select:
        status = __action(player, select)
    if pos[0][0] == select and pos[1][0] == select and pos[2][0] == select:
        status = __action(player, select)
    if pos[0][1] == select and pos[1][1] == select and pos[2][1] == select:
        status = __action(player, select)
    if pos[0][2] == select and pos[1][2] == select and pos[2][2] == select:
        status = __action(player, select)
    if pos[0][0] == select and pos[1][1] == select and pos[2][2] == select:
        status = __action(player, select)
    if pos[0][2] == select and pos[1][1] == select and pos[2][0] == select:
        status = __action(player, select)
    if __check_draw() == 1:
        __screen()
        print(f"\n FINAL GAME - DRAW!")
        status = False
    return status


def __action(player, select):
    __screen()
    print(f"\n FINAL GAME - PLAYER {player} ( {select} ) WINS!")
    time.sleep(2)
    return False


def __screen():
    os.system('clear')
    print('######## TIC-TAC-TOE GAME ########\n' +
          '#                                #\n' +
          '#       a        b         c     #\n' +
          '#            |        |          #\n' +
          f'#  1    {pos[0][0]}    |   {pos[1][0]}    |    {pos[2][0]}     #\n' +
          '#    ________|________|________  #\n' +
          '#            |        |          #\n' +
          f'#  2    {pos[0][1]}    |   {pos[1][1]}    |    {pos[2][1]}     #\n' +
          '#    ________|________|________  #\n' +
          '#            |        |          #\n' +
          f'#  3    {pos[0][2]}    |   {pos[1][2]}    |    {pos[2][2]}     #\n' +
          '#            |        |          #\n' +
          '#                                #\n' +
          '##################################\n')

def __check_draw():
    d = 1
    for k in pos:
        for i in k:
            if "_" in i:
                d = d + 1
    return d

def __change_player(player, select):
    if select == "X":
        select = "O"
        player = 2
    else:
        select = "X"
        player = 1

    return player, select


tic-toc-toe-game()
