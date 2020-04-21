#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/21 21:25
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : func_param.py
# @notice ：


# m n
# def fac(num):
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
#
# m = int(input("m = "))
# n = int(input("n = "))
# print(fac(m) // fac(n) // fac(m - n))


# import os
# import time
#
#
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#     main()


# import random
# def generate_code(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code
#
# print(generate_code(4))


# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()
#
#
# if __name__ == '__main__':
#     main()


from random import randrange, randint, sample


# def display(balls):
#     """
#     输出列表中的双色球号码
#     """
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%02d' % ball, end=' ')
#     print()
#
#
# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls
#
#
# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end='')
#
#
# if __name__ == '__main__':
#     main()


import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()