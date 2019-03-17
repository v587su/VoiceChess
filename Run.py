# coding: utf-8

import Chessboard


def print_chessman_name(chessman):
    if chessman:
        print(chessman.name)
    else:
        print("None")


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
        is_correct_chessman = False
        is_correct_position = False
        chessman = None
        while not is_correct_chessman:
            title = "Enter chess name: "
            input_chessman_name = input(title)
            chessman = cbd.get_chessman_by_name(input_chessman_name)
            if chessman != None and chessman.is_red == cbd.is_red_turn:
                is_correct_chessman = True
                print("position available:")
                for point in chessman.moving_list:
                    print(point.x, point.y)
            else:
                print("Chess not found")
        while not is_correct_position:
            title = "Enter chess aim position: "
            input_chessman_position = input(title)
            is_correct_position = chessman.move(
                input_chessman_position[0], input_chessman_position[1])
            if is_correct_position:
                cbd.print_to_cl()
                cbd.clear_chessmans_moving_list()


if __name__ == '__main__':
    main()