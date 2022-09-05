#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
'''
@Author: lvmengting 
@Date: 2022-06-24 16:58:06
'''

from matplotlib.pyplot import cla


class Frog:

    def __init__(self, name):
        self.name = name 


    def __str__(self):
        return self.name 


    def interact_with(self, obstacle):
        '''不同类型的玩家遇到不同的障碍'''
        print(f'{self} the Forg encounters {obstacle} and {obstacle.action()}!')



class Bug:
    
    def __str__(self):
        return 'a bug'

    
    def action(self):
        return 'eats it'



class FrogWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name 


    def __str__(self):
        return '\n\n\t----Frog World---'


    def make_character(self):
        return Frog(self.player_name)  


    def make_obstacle(self):
        return Bug()



class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(f'{self} the Wizard battles against {obstacle} and {obstacle.action()}!')



class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kill it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    """ 抽象工厂，根据不同的玩家类型创建不同的角色和障碍 (游戏环境)
    这里可以根据年龄判断，成年人返回『巫师』游戏，小孩返回『青蛙过河』游戏"""
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)       

