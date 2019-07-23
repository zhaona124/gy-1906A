# a="alanwalker"
# print(a[0:3])
# print(a[-6:])
#按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# def juge_3(a):
#     # a=input()
# a = a.replace("''", '"')

    # print(p)
a='["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]'

a=a[2:-2]
    # print(p)
a=a.split('" , "')
    # print(ab)
    # a='http://www.w3.org/2000/svg'
    # ab=a.split('://')[0]
    # abc=a.split('://')[1]
    # d=abc[:abc.find('/')]
    # f=abc[abc.find('/'):]
    # h=f[f.find('/')+1:]
    # print(h)
n={}
for k in a:
    j=k[1:]
    if(j in n):
        n[j]+= 1
        print(j)
    else:
       n[k] = 1
    print(n)
t1=3
t2=3
for key in n:#字典循环遍历，根据key
    if(n[key]==3):
        t1=1
    if(n[key]==2):
        t2=1
if(t1==1 and t2==1):
    print('三带二')
else:
  print('不符合要求')
# for y in  range(3):
# juge_3("[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']")
# juge_3('''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]''')
# juge_3('''["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]''')
# with open('E:\\softwareData\\untitled\day04\\cards.txt','r')as d:
#     f=d.readlines()
#     print(f)
#     for g in f:
#         m=g.replace('\n','')
#         juge_3(m)







