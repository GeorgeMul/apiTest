#開頭打印
print("歡迎使用綜合健康計算機~\n(1)計算(BMI)\n(2)計算基礎代謝率(BMR)\n(3)計算總熱量消耗(TDEE)")

#確認計算項目
test_name = input("請選擇要計算的項目 (輸入1 or 2 or 3):")

gender = input("請輸入您的性別(男 or 女):")
height = float(input("請輸入您的身高(公分):"))
weight = float(input("請輸入您的體重(公斤):"))
age = float(input("請輸入您的年齡:"))

#BMI測試
def BMI_test(height,weight):
    height /= 100
    BMI = weight / (height ** 2)
    BMI = round(BMI, 1)
    return BMI


#BMR測試
def BMR_test(gender,height,weight,age):
    if gender == "男":
        BMR1 =66 + (13.7 * weight + 5 * height - 6.8 * age)
        BMR1 = round(BMR1, 2)
        return BMR1
    else :
        BMR1 =655 + (9.6 * weight + 1.8 * height - 4.7 * age)
        BMR1 = round(BMR1, 2)
        return BMR1

def TDEE_test():
    sports =input("(1)久坐、幾乎沒運動\n"
          "(2)每週低強度運動1~3天\n"
          "(3)每週中強度運動3~5天\n"
          "(4)每週高強度運動6~7天\n"
          "(5)勞力密集工作或是每天高強度訓練\n"
          "請選擇您的運動量 (輸入1~5)")
    if sports == "1":
        return float(1.2)
    elif sports == "2":
        return float(1.375)
    elif sports == "3":
        return float(1.55)
    elif sports == "4":
        return float(1.725)
    else :
        return float(1.9)


#最終執行
if test_name == "1":
    print(f"您的BMI是:{BMI_test(height,weight)}")
elif test_name == "2":
    print(f"您的基礎代謝率(BNMR):{BMR_test(gender,height,weight,age)}")
else :
    num = round((BMR_test(gender,height,weight,age) * TDEE_test()), 2)
    print(f"您的基礎代謝率(BNMR):{num}")






