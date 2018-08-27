a=[0,1,2,3,4]
#移除对象
#a.remove(5) ValueError: list.remove(x): x not in list
#remove函数可以移除列表中的一个已知对象，若列表中无此对象则报错
a.remove(0)
print(a)

#移除和返回对象
#pop方法，删除！ 和 返回！ 列表中某一索引值位置上的对象，若未提供索引值，则删除 和 返回最后一个位置上的对象
#索引值若不存在，则报错
#注意，pop可以返回被删除的值
b = a.pop(0)
#a.pop(4) IndexError: pop index out of range
print(a)
print(b)

#使用列表扩展列表
#extend()将一个列表插入另一个列表
c = [5,6,7]
a.extend(c)
print(a)

#列表的某个位置插入一个对象
#insert（）可以将对象插入列表的任意索引位置，但是插入至最后应使用append（）
d = 1
a.insert(0,d)
print(a)