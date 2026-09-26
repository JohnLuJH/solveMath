#集合运算器
print("集合运算器已启动！")
setA = "1,2,3"
setB = "2,3,4"
setU = "1,2,3,4,5"
setA = set(int(x) for x in setA.split(","))
setB = set(int(x) for x in setB.split(","))
setU = set(int(x) for x in setU.split(","))
#并集、交集、差集
print("setA ∪ setB=", setA.union(setB))
print("setA ∩ setB=", setA.intersection(setB))
print("setA - setB=", setA.difference(setB))
#补集
print("setA的补集=", setU.difference(setA))
print("setB的补集=", setU.difference(setB))