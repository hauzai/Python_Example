#复制列表时，不能使用=，应使用copy方法
one = [1,2,3]
two = one
two.append(4)
#这里可以看出，=将one的地址赋给了two，当two被更改时，其实是更改了one所指向的对象
print(one)
print(two)

three = two.copy()
three.append(5)
#copy()方法获取到了two所指向的对象，并将它赋给了three所指向的内存
print(two)
print(three)
########################################################################################################################
'''
python中的中括号记法[]
1.常规索引值：可以使用list[0]来访问列表中某位置的对象
2.负索引值：可以使用负数索引值，list[-1]可以用来访问列表中最后一个值，以此类推
3.范围索引：python中括号可以使用 list[start:stop:step]
'''
print(one[-1])
print(one[0:3:2])

test = list("hello world")
print(test)
print(test[0::3])