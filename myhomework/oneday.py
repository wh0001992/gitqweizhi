'''
#一、求10阶乘
#循环变量
a = 1
mcl = 1
#循环体
for a in range(1,11):
    mcl = a * mcl
#输出
print(mcl)
#二、求100以内能被3整除的数，并将作为列表输出
#循环变量
list1 = []
#循环体(判断100以内能被3整除的数，如果能整除，放入列表内)
for a in range(1,101):
    if a%3 == 0:
        list1.append(a)
print(list1)
#输出
'''
#三、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
'''
定义一个列表 list2 = [1,2,3,4,3,4,2,5,5,8,9,7]
去重
   依次取该列表中的元素
   判断元素在列表中出现的次数list2.count 与 1做比较
   出现次数大于1就删除
输出去重后的列表
'''
'''
list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
list2 = [1,2,3,4,3,4,2,5,5,8,9,7]
for a in list1:
    if list1.count(a) > 1:
        if list2.count(a) > 1:
            list2.remove(a)
print(list2)
'''
#四、求斐波那契数列 1 1 2 3 5 8 13 ……
#list5 = [1,1]
#for a in range(1,10):
#list5.append(list5[a-1]+list5[a])
#print(list5)


#五、求100以内的质数
#质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。

list6 = []
for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        list6.append(i)
print(list6)