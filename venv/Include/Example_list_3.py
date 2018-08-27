#使用list的方法将plist转换为on tap
phrase = "Don'tpanic!"
plist = list(phrase)
print(phrase)
print(plist)

found = []
word1 = plist.pop(6)
plist.remove('\'')
plist.pop(0)
plist.insert(2," ")
plist.insert(4,word1)
while len(plist) != 6:
    plist.pop(6)


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
