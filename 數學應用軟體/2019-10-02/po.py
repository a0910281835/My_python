# coding: utf-8
from numpy.random import randint
# explain ''' 分行
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止
愛情阿
天注定
椎間盤'''
phrase=words.split('\n')
from numpy.random import choice
num=randint(2,8) #幾段
for i in range(num):
    cout=randint(5,8) # 每段抽取的字數
    sen=choice(phrase,cout)
    ham=" ".join(sen)
    print(ham)
    
