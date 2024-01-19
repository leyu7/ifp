import os
import pandas as pd

'''骰子'''
def roll(dice_amount):
    result = []
    for i in range(dice_amount):
        n = ord(os.urandom(1)) % 6 + 1
        # 更随机  https://blog.csdn.net/a19990412/article/details/80934268
        # 随机数，除以6取余，再加1（结果由0-5变成1-6）
        result.append(n)
    return result


def init_state(disc_amount):  # You can choose how many discs
    col = list(range(1, disc_amount + 1))
    state = pd.DataFrame(columns=col)
    state.loc['P'] = 1  # 1: safe；0:unsafe
    state.loc['S'] = 0  # P: primary row; S: second row
    return state

