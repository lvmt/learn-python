#!/usr/bin/env python -*-
#-*- coding:utf-8 -*-


class BenCar:
    
    brand = '奔驰'
    country = '德国'  # 类属性, 共同属性
    
    def __init__(self,color,enginSN):  # 实例属性,每个实例独有的
        # __init__ 是 创建好实例后 立即就要 执行 的方法，所以称之为初始化方法。
        self.color = color
        self.engineSN = enginSN
    
    @staticmethod
    def pressHorn():
        print('嘟嘟~~~~~~')
        
    def changecolor(self,newcolor):
        self.color = newcolor
        
        
class Benz2016(BenCar):
    price = 58000
    model = 'Benz2016'
    
    
class Benz2018(BenCar):
    price = 88000
    model = 'Benz2018'

    def __inti__(self,color,enginSN,weight):
        # 先调用父类的初始化方法
        BenCar.__init__(self,color,enginSN)
        self.weight = weight
        self.oilweight = 0
            
    

if __name__ == '__main__':
    
    # cc = BenCar('red', '9898')
    # print(f'实例的颜色是: {cc.color}')
    # cc.changecolor('yellow')
    # print(f'修改后的颜色是: {cc.color}')

    car1 = Benz2016('red','234234545622')    
    car2 = Benz2018('blue','111135545988')   

    print (car1.brand)
    print (car1.country)
    car1.changecolor('black')

    print (car2.brand)
    print (car2.country)
    car2.pressHorn()
