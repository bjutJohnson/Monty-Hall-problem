# coding=utf-8
# /usr/bin/python

'''
Monty Hall难题。 三个盒子，分别编号为A、B、C，其中有两个里面装的是可以吃的苹果，另一个装的是iphone 7，
盒子打开之前，不知道三个盒子里面装的到底是苹果还是iphone 7。给你一个选择机会，你可以选择A、B、C中任意一个，
如你可以选择B盒子，这时，我打开了其它两个盒子中的一个（假如是C），告知这个盒子里面装的是苹果，然后再给你一次
选择机会，你是坚持自己最初的选择（B），还是选择剩下的两个盒子（A和B）的另一个（A）？？？

本程序用来模拟选择情况，程序的基本逻辑：初试时，三个盒子装的东西随机生成（两个苹果，一个装iphone 7）；
然后，模拟两个人，其中一人始终坚持自己一开始的选择，另一个人则在我打开一个装苹果的盒子后，选择另外一个盒子；
最后，我们通过模拟这个实验100次、200次、500次、1000次、2000次、5000次、10000次等来计算谁获得iphone7的概率更高
'''

import random

# 三个盒子，用一个数组表示
THREE_BOX = []

# 在三个数中随机生成一个指示是iphone 7的编号或者用户随机选择一个盒子
def generateIndex():
    iRet = random.sample([0, 1, 2], 1)
    return iRet[0]

# 为了使程序更真实，模拟产生装有iphone或苹果的盒子，index指示装iphone的盒子
def generateBox(index):
    if THREE_BOX:
        del THREE_BOX[:]


    for i in range(3):
        if i != index:
            THREE_BOX.append("apple")
        else:
            THREE_BOX.append("iphone 7")


# 模拟我的行为，从用户的选择之外的两个盒子中选择一个装苹果的盒子打开告知用户
# 返回打开的盒子的编号
def simulateMyBehavior(userSelectIndex, iphone7Index):
    iRet = -1

    tmp = [0, 1, 2]

    if userSelectIndex == iphone7Index:
        tmp.remove(userSelectIndex)

        iRet =  random.sample([tmp[0], tmp[1]], 1)
    else:
        tmp.remove(userSelectIndex)
        tmp.remove(iphone7Index)
        iRet = tmp[0]

    return iRet

# 模拟两个人选择的过程，num指示模拟次数
def simulateResult(num):
    oneSelectSuccess = 0
    twoSelectSuccess = 0

    for i in range(num):
        # 随机生成iphone 7的编号
        iPhone7Index = generateIndex()

        # 根据iphone7的编号产生三个盒子
        generateBox(iPhone7Index)

        # 用户随机选择
        userSelectIndex = generateIndex()

        #print("user: ", userSelectIndex, ", iphone 7: ", iPhone7Index)

        # 模拟我的行为：即打开一个盒子，告知用户这个盒子里面是一个苹果
        openBoxIndex = simulateMyBehavior(userSelectIndex, iPhone7Index)


        # 如果用户始终坚持最开始的选择
        if userSelectIndex == iPhone7Index:
            oneSelectSuccess = oneSelectSuccess + 1
        # 如果用户改变选择，实际上是二选一，因此else语句必然应对的是改变选择的情况
        else:
            twoSelectSuccess = twoSelectSuccess + 1


    print("one select success ratio: ", oneSelectSuccess * 1.0 / num)
    print("two select success ratio: ", twoSelectSuccess * 1.0 / num)

# 测试
def test():
    print("100次的分布情况：")
    simulateResult(100)

    print("===============")
    print("200次的分布情况：")
    simulateResult(200)

    print("===============")
    print("300次的分布情况：")
    simulateResult(300)

    print("===============")
    print("400次的分布情况：")
    simulateResult(400)

    print("===============")
    print("500次的分布情况：")
    simulateResult(500)

    print("===============")
    print("600次的分布情况：")
    simulateResult(600)

    print("===============")
    print("700次的分布情况：")
    simulateResult(700)

    print("===============")
    print("800次的分布情况：")
    simulateResult(800)

    print("===============")
    print("900次的分布情况：")
    simulateResult(900)

    print("===============")
    print("1000次的分布情况：")
    simulateResult(1000)

    print("===============")
    print("2000次的分布情况：")
    simulateResult(2000)

    print("===============")
    print("5000次的分布情况：")
    simulateResult(5000)

    print("===============")
    print("10000次的分布情况：")
    simulateResult(10000)

    print("===============")
    print("20000次的分布情况：")
    simulateResult(20000)

    print("===============")
    print("30000次的分布情况：")
    simulateResult(30000)

    print("===============")
    print("40000次的分布情况：")
    simulateResult(40000)

    print("===============")
    print("50000次的分布情况：")
    simulateResult(50000)

    print("===============")
    print("100000次的分布情况：")
    simulateResult(100000)

test()