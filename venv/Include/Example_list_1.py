price = []
temps = [110.0,20.5]
words = ["hello","word"]
car_details = ["toyota","rav4",2.2,60807]
everythings = [temps,price,words,car_details]
#列表中可以存放 任何数据类型 长度可变
print("word" not in words)

a = ["a","e","i","o","u"]
A = input("请输入一个单词，查看单词中的元音:")
seem = []
for ch in A:
    if ch in a:
        if ch not in seem:
            seem.append(ch)
#append 函数，为列表中添加对象！
for ch in seem:
    print(ch)
print("hellogongsi")