__author__ = 'jc441938'

from random import randint
num_of_pics=int(input('HOW MANY QUICK PICKS?'))
pick_of_6_num=[]
for i in range(0,num_of_pics):
    num=randint(1,45)
    for j in range(0,6):
        while num in pick_of_6_num:
            num=randint(1,45)
        pick_of_6_num.append(num)
    pick_of_6_num.sort()
    print(sorted(pick_of_6_num))
    pick_of_6_num=[]
