#coding=utf-8
'''
file=open('D:\\txl.txt','r')
for i in file.readlines():
    #print(i)
    #print(type(i))
    i=i.strip('\n')
    a=i.split(' ')
    print(a)
    if a[-1]=='110':
        print('110 is here!!')
file.close()
'''
file=open('D:\\txl.txt','r')
for i in file.readlines():
    print(i)
    if '110' in i:
        print('yes')
file.close()
