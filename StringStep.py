import Point


class StringStep:
    def __init__(self, terminology):
        self.terminology = terminology
        self.name, self.pos_from, self.method, self.pos_to = self._parse(terminology)

    def get_action(self, cbd):
        chessman = self._get_chessman(cbd)
        if not chessman:
            return None, None
        point = self._cal_aim_point(chessman.position, cbd)

        return chessman, point

    def _parse(self, terminology):
        if len(terminology) != 4:
            raise ValueError

        pos_list = '一二三四五六七八九'

        for i in range(1, 10):
            terminology = terminology.replace(pos_list[i - 1], str(i))

        if terminology[0] in ['前', '后', '中']:
            [pos_from, name, method, pos_to] = terminology
        else:
            [name, pos_from, method, pos_to] = terminology

        if int(pos_from) not in range(1, 10) or int(pos_to) not in range(1, 10):
            raise ValueError

        return name, int(pos_from), method, int(pos_to)

    def _get_chessman(self, cbd):
        is_red_turn = cbd.is_red_turn
        prefix = 'red_' if is_red_turn else 'black_'
        is_right_chessman = False
        chessman = None
        chessman_name = self.name
        pos_from = self.pos_from
        method = self.method
        name_dict = {
            '兵': ['pawn_1', 'pawn_2', 'pawn_3', 'pawn_4', 'pawn_5'],
            '卒': ['pawn_1', 'pawn_2', 'pawn_3', 'pawn_4', 'pawn_5'],
            '帅': ['king'],
            '将': ['king'],
            '士': ['mandarin_left', 'mandarin_right'],
            '仕': ['mandarin_left', 'mandarin_right'],
            '象': ['elephant_left', 'elephant_right'],
            '相': ['elephant_left', 'elephant_right'],
            '马': ['knight_left', 'knight_right'],
            '车': ['rook_left', 'rook_right'],
            '炮': ['cannon_left', 'cannon_right']
        }
        if pos_from in ['前', '后', '中']:
            pass
        else:
            pos_from = 10 - self.pos_from if is_red_turn else self.pos_from
            for name_str in name_dict[chessman_name]:
                name = prefix + name_str
                chessman = cbd.get_chessman_by_name(name)
                if chessman is not None and chessman.is_red == cbd.is_red_turn:
                    position = chessman.position
                    print(position.x, position.y)
                    if pos_from == position.x + 1:
                        is_right_chessman = True
                        break

        if is_right_chessman:
            return chessman
        else:
            print('Chessman not found!')
            return None

    def _cal_aim_point(self, postion, cbd):
        is_red_turn = cbd.is_red_turn
        rule1_list = '兵卒帅将车炮'
        rule2_list = '士仕相象马'
        x = postion.x
        y = postion.y
        x_new = x
        y_new = y
        chessman_name = self.name
        method = self.method
        pos_from = 10 - self.pos_from if is_red_turn else self.pos_from
        pos_to = 10 - self.pos_to if is_red_turn else self.pos_to

        if chessman_name in rule1_list:
            if method == '平':
                x_new = pos_to - 1 if is_red_turn else pos_to - 1
                y_new = y
            elif method == '进':
                pos_to = self.pos_to
                x_new = x
                y_new = y + pos_to if is_red_turn else y - pos_to
            elif method == '退':
                pos_to = self.pos_to
                x_new = x
                y_new = y - pos_to if is_red_turn else y + pos_to
            else:
                raise ValueError
        elif chessman_name in rule2_list:
            step = 1

            if chessman_name in '象相' or (chessman_name == '马' and abs(pos_from - pos_to) == 1):
                step = 2
            if method == '进':
                y_new = y + step if is_red_turn else y - step
                x_new = pos_to - 1
            elif method == '退':
                y_new = y - step if is_red_turn else y + step
                x_new = pos_to - 1
            else:
                raise ValueError
        return Point.Point(x_new, y_new)
