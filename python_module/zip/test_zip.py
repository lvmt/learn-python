#/usr/bin/python
#-*- coding:utf-8 -*-

#python的转置功能：zip函数

rows = [
    ["Number", "data1", "data2"],
    [1,2,3,4],
    [5,6,7,8]
]

print(rows)
'''
[['Number', 'data1', 'data2'], [1, 2, 3, 4], [5, 6, 7, 8]]
'''

zip_rows = zip(*rows)
print(zip_rows)
'''
[('Number', 1, 5), ('data1', 2, 6), ('data2', 3, 7)]
'''

'''从转置后的结果上可以发现，转置的结果舍弃了一部分的数据，原因如下随时：
zip(*rows)，首先是将*rows列表打散，zip从列表中提取第1个值组成tuple，在从每个列表中提取第2个值组成tuple，一直到最短列表的最后一个值提取完毕后结束，更长的列表之后的值将会被舍弃。
即：最后的元祖个数是由原来的每个参数的最短长度决定的。
'''