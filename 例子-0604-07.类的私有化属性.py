#coding=utf-8
'''
class student:
    def __init__(self):
        self.__number=30

banji=student()
print(banji.__number)
'''
class student:
    def __init__(self,num):
        self.__num=num
    def printage(self):
        print('your age is %d' % self.__num)
age=student(30)
age.printage()
