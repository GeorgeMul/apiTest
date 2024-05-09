#BMI計算機
#讓用戶輸入身高並換成text
text1 = float(input("請輸入您的身高(公分)\n"))
text2 = float(input("請輸入您的體重(公斤)\n"))

#把text做除法在打印出來
text1 /=100
BMI = text2/text1**2
BMI = round(BMI, 1)
print(f"您的BMI是:{BMI}")