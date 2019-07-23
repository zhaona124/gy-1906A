# a=[]
# #在最后一位新增列表数据
# a.append(1)
# a.append('你是最棒的')
# print(a)
# b=[1,4,5,6,'侬好']
# print(a+b)
# #extend方法合并两个列表，是在原来的列表末尾加上另一个列表
# a.extend(b)
# print(a)
# # #删除某个元素
# # a.pop(0)
# # print(a)
# # #不给下标默认删除最后一位数
# # a.pop()
# # print(a)
# # #清空列表
# # # a.clear()
# # # print(a)
# # #根据下标修改值
# # a[0],a[1]='w',2
# # print(a)
# #根据下标查某个元素
# print(a[0:3])
#
# #遍历
# # for i in a:
# #     print(i)
# #查列表长度（跟字符串一样的方法）
# print(len(a))
# #成员判断
# if(4 in a):
#     print('在此列表中')
# else:
#     print('不在此列表中')

# a={}
# a['姓名'],a['年龄']='赵娜',18
# print(a)
c={'姓名':'赵娜'}
d={'年龄':'18'}
# c.update(d)
print(dict(c,**d))
