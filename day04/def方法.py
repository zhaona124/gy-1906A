#实现两数相加的方法：
def m_1(num1,num2):
    a=num1
    b=num2
    s=a+b
    print(a,'+',b,'=',s)
    return s
# # with open('E:\\softwareData\\untitled\\day04\\lint.txt') as g:
# #     h=g.readlines()
# #     for j in h:
# #         j = j.replace('/n', '')
# #         j_1=j.split(',')#字符串格式转为列表格式先去掉逗号
# #         m_1(int(j_1[0]),int(j_1[1]))#字符串强转数字格式后取位数
# def m_2(n,o):
#     h=n*o
#     print(n,'*',o,'=',h)
# with open('E:\\softwareData\\untitled\\day04\\lint.txt') as y:
#     t=y.readlines()
#     for r in t:
#         r = r.replace('/n', '')
#         r_1=r.split(',')#字符串格式转为列表格式先去掉逗号
#         m_2(int(r_1[0]),int(r_1[1]))#字符串强转数字格式
# def m_3(c,v):
#     if (v!= 0):
#         z=c/v
#         print(c,'/',v,'=',z)
#     else:
#         print('除数不能为0')
# with open('E:\\softwareData\\untitled\\day04\\lint.txt') as k:
#     m=k.readlines()
#     for u in m:
#         u = u.replace('/n', '')
#         u_1=u.split(',')#字符串格式转为列表格式先去掉逗号
#         m_3(int(u_1[0]),int(u_1[1]))#字符串强转数字格式
m_1(m_1(4,5),6)

#
# def r_1(m1,n1):
#     return '{}{}你好世界'.format(m1,n1)
# print(r_1('hello','world'))

def buy_coffees(cups,cash=100):
    #去咖啡店
    print("去咖啡店")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"杯咖啡")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"钱")
    #你给服务员多少钱
    money = cash
    print("你给服务员",money,"钱")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")
buy_coffees(2)
buy_coffees(4,200)


