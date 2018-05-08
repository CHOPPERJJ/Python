#coding=utf-8
# 遍历set,set中为tuple的项目，x[0]访问第一项，x[1]访问第二项
s = set ([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0], ':', x[1]

# 更新set或者删除set中的元素
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for it in L:
    if it in s:
        s.remove(it)
    else:
        s.add(it)
print(s)

# python函数练习
L = range(1, 101)
print sum(L)