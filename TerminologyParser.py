def parse(terminology):
    if len(terminology) != 4:
        raise ValueError
    pos_list = '一二三四五六七八九'
    if terminology[0] in ['前', '后', '中']:
        [pos_from, name, method, pos_to] = terminology
    else:
        [name, pos_from, method, pos_to] = terminology

    if (pos_from not in pos_list) or (pos_to not in pos_list):
        raise ValueError

    return name, pos_from, method, pos_to


def get_chessman(cbd, chessman_name, pos_from, method):
    chessman = None
    pos_from_n = _chinese_to_number(pos_from)
    name_dict = {
        '兵': ['pawn_1', 'pawn_2', 'pawn_3', 'pawn_4', 'pawn_5'],
        '卒': ['pawn_1', 'pawn_2', 'pawn_3', 'pawn_4', 'pawn_5'],
        '帅': ['king'],
        '将': ['king'],
        '士': ['mandarin_left', 'mandarin_right'],
        '仕': ['mandarin_left', 'mandarin_right'],
        '象': ['elephant_left', 'elephant_left'],
        '相': ['elephant_left', 'elephant_left'],
        '马': ['knight_left', 'knight_left'],
        '车': ['rook_left', 'rook_left'],
        '炮': ['cannon_left', 'cannon_right'],
    }
    is_red_turn = cbd.is_red_turn()
    prefix = lambda x: 'red_' if is_red_turn else 'black_'

    if pos_from in ['前', '后', '中']:
        pass
    else:
        for name_str in name_dict[chessman_name]:
            name = prefix + name_str
            chessman = cbd.get_chessman_by_name(name)
            if chessman is not None and chessman.is_red == cbd.is_red_turn:
                position = chessman.position
                if pos_from_n == position.x:
                    break
    return chessman.position


def cal_aim_postion(postion, chessman_name, pos_from, method, pos_to):
    rule1_list = ['兵卒帅将车炮']
    rule2_list = ['士仕象相马']
    x = postion.x
    y = postion.y
    pos_from_n = _chinese_to_number(pos_from)
    pos_to_n = _chinese_to_number(pos_to)

    if chessman_name in rule1_list:
        if method == '平':
            x_new =
        else:
            pass
    elif chessman_name in rule2_list:
        pass


def _chinese_to_number(number_cn):
    pos_list = '一二三四五六七八九'
    number = pos_list.index(number_cn) + 1
    return number
