print("歡迎使用拉麵點餐機~")

print("(1)鹽味拉麵 $220")
print("(2)醬油拉麵 $240")
print("(3)豚骨拉麵 $280")

noodles = int(input("請選擇拉麵口味 (輸入:1 or 2 or 3)"))

if noodles == 1:
    total = 220
elif noodles == 2:
    total = 240
else :
    total = 280

taste = input("是否加大, 豚骨口味+$50 其他+$30 (輸入:Y or N)").upper()
if taste == "Y" and total == 280 :
    total +=50
elif taste == "Y":
    total +=30

egg = input("是否加糖心蛋+$30 (輸入:Y or N)").upper()
if egg == "Y" :
    total +=30

pork = input("是否加叉燒+$60 (輸入:Y or N)").upper()
if pork == "Y" :
    total +=60

if taste == "Y" and egg == "Y" and pork == "Y" :
    total -=20
    print(f"\n\n加好加滿折價$20,總金額${total},感謝您的光臨")
else :
    print(f"\n\n總金額${total},感謝您的光臨")