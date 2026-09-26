#集合运算器
def run():
    print("集合运算器已启动！")
    setA = input("请输入集合A（用逗号分隔元素）：")
    setB = input("请输入集合B（用逗号分隔元素）：")
    setU = input("请输入全集U（用逗号分隔元素）：")
    setA = set(setA.split(","))
    setB = set(setB.split(","))
    setU = set(setU.split(","))
    #并集、交集、差集
    print("setA ∪ setB=", setA.union(setB))
    print("setA ∩ setB=", setA.intersection(setB))
    print("setA - setB=", setA.difference(setB))
    #补集
    print("setA的补集=", setU.difference(setA))
    print("setB的补集=", setU.difference(setB))