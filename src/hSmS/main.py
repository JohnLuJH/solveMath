from hSmS import setCalc
#程序入口点
print("欢迎使用高中数学题目求解器！")
print("1. 集合运算器")
operate = input("请输入您想要运行的数学运算器：")
if operate == "1":
    setCalc.run()