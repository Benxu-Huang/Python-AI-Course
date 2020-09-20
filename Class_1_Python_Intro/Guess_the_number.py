# 作業2 猜數字
import random
randomNum = random.randint(1,100)
i = 0
history = []

print(randomNum)

while True:
    i=i+1
    inputPwd = int(input("請輸入數字:"))
    history.append(inputPwd)

    if  inputPwd>randomNum:
        print("第{}次猜數字".format(i))
        print("結果：你猜的數字較大")

    elif inputPwd<randomNum:
        print("第{}次猜數字".format(i))
        print("結果：你猜的數字較小")
    else:
        print("第{}次猜數字".format(i))
        print("結果：猜對了！！！")
        break

    print("您目前的猜數字紀錄{}".format(history))    

    newArr = history.copy()
    newArr.sort()

    if  len(newArr) > 2:
        for index, val in enumerate(newArr):
            if  index < len(newArr)-1:
                if  newArr[index] < randomNum and newArr[index+1] > randomNum:
                    print("正確數字介於{}與{}之間".format(val,newArr[index+1]))
                    break

    print("-----------------------------\n")