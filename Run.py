# coding: utf-8

import Chessboard
from StringStep import StringStep


def main():
    cbd = Chessboard.Chessboard('123')
    cbd.init_board()
    cbd.print_to_cl()
    while not cbd.is_end():
        cbd.calc_chessmans_moving_list()
        if cbd.is_red_turn:
            print("is_red_turn")
        else:
            print("is_black_turn")

        is_correct = False
        while not is_correct:

            title = 'Input string action:'
            terminology = input(title)
            try:
                step = StringStep(terminology)
            except ValueError:
                print('Wrong Input')
                is_correct = False
            else:
                chessman, point = step.get_action(cbd)
                if chessman:
                    is_correct = chessman.move(point.x, point.y)
            if is_correct:
                cbd.print_to_cl()
                cbd.clear_chessmans_moving_list()


if __name__ == '__main__':
    main()
