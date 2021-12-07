#!/usr/bin/env python

import random
import jieba
import jieba.posseg as pseg

__all__ = ['chs2miao']
jieba.setLogLevel(20)


def _词转换(x, y, 猫叫率):
    if random.random() > 猫叫率:
        return x
    if x in {'，', '。'}:
        return '，喵～'
    if x in {'!', '！'}:
        return '，喵喵喵！'
    if len(x) > 1 and random.random() < 0.5:
        return f'{x[0]}，喵，喵，{x}'
    else:
        if y == 'n' and random.random() < 0.5:
            x = '猫猫' * len(x)
        return f'喵，{x}'


def chs2miao(s, 猫叫率=0.5):
    return ''.join([_词转换(x, y, 猫叫率) for x, y in pseg.cut(s)])


if __name__ == '__main__':
    print(chs2miao('我们一起学猫叫'))
