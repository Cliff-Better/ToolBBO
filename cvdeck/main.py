import 數學計算.Operate
from 溫度計算器 import Tmp 






if __name__ == "__main__":
    Tool = input("請選擇工具包:輸入 1.溫度計算 2.電費計算 3.兩數相加 4.吃甚麼")
    if Tool =="1":
        Tmp.temprature()
    elif Tool =="2":
        Tmp.eBill()
    elif Tool =="3": 
        print(數學計算.Operate.add(5,9))   
    elif Tool =="4":
        print(Tmp.lunch())

        




