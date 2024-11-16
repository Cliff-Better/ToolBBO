# 攝氏轉華氏
def c_to_f(c):
  return (c*9/5)+32
# 華氏轉攝氏
def f_to_c(f):
  return (f-32)*5/9



def temperture():
    you123 = input("選擇類型(1:攝氏,2:華氏):")
    if  you123 =="1":
        num = int(input("請輸入攝氏溫度:"))
        print(f"{num}度 對應的華氏溫度是{c_to_f(num):.1f}度")
    else :
        num = int(input("請輸入華氏溫度:"))
        print(f"{num}度 對應的攝氏溫度是{f_to_c(num):.1f}度")









# 電費計算
def eBill():
    while True:
        try:
                num = float(input("輸入電度"))
                output = 0
                if num <= 200:
                    output = num * 3.2
                elif num <= 300:
                    output = 200 * 3.2 + (num - 200) * 3.4
                else:
                    output = 200 * 3.2 + 100 * 3.4 + (num - 300) * 3.6

                print(f'用電{num}度共{output:.2f}元')

        except ValueError:
            print("輸入錯誤")





import random

def lunch():
    foods = []
    
    with open("food.txt","r",encoding="utf-8") as file:
      for line in file:
         foods.append(line.strip())

    result = random.choice(foods)

    return result

 