import random
import numpy as np
def addlevel(a,b):
#足し算の足される数、足す数をそれぞれ引数a,bとして繰り上がりなどのレベルに応じた判定を出す
#'level1':繰り上がりなし
# 'level5':五繰り上がりあり
# 'level10':十繰り上がりあり
# 'level1100':五玉を用いた十繰り上がりあり
    if a <10 and b < 10:
        if a<=4 and b <= 4:
            if a + b >=5:
                return 'level5'
            else:
                return 'level1'
        elif a<=4 and b >= 6:
            if a + b >= 10:
                return 'level10'
            else:
                return 'level1'
        elif a>=5 and b >= 6:
            if a + b >= 15:
                return 'level10'
            else:
                return 'level100'
        elif a>=5 and b <= 5:
            if a + b >= 10:
                return 'level10'
            else:
                return 'level1'
        else:
            return 'level1'
def sublevel(a,b):
#引き算の引かれる数、引く数をそれぞれ引数a,bとして繰り下がりなどのレベルに応じた判定を出す
#'level1':繰り下がりなし
# 'level5':五繰り下がりあり
# 'level10':十繰り下がりあり
# 'level1100':五玉を用いた十繰り下がりあり
    if a<=4:
        if a < b % 5 or b == 5:
            return "level10"
        elif a >= b % 5 and a < b:
            return "level100"
        else:
            return "level1"
    elif a >= 5 and b <= 4:
        if a % 5 < b:
            return "level5"
        else:
            return "level1"
    elif a >= 5 and b >= 5:
        if a < b:
            return "level10"
        else:
            return "level1"
        
def nonekuriaddmaker(ed):
    list1=[1,2,3,5,6,7,8]
    list2=[1,2,5,6,7]
    list3=[1,5,6]
    list4=[5]
    list5=[1,2,3,4]
    list6=[1,2,3]
    list7=[1,2]
    list8=[1]
    list0=[1,2,3,4,5,6,7,8,9]
    if ed == 1:
        return random.choice(list1)
    elif ed == 2:
        return random.choice(list2)
    elif ed == 3:
        return random.choice(list3)
    elif ed == 4:
        return random.choice(list4)
    elif ed == 5:
        return random.choice(list5)
    elif ed == 6:
        return random.choice(list6)
    elif ed == 7:
        return random.choice(list7)
    elif ed == 8:
        return random.choice(list8)
    elif ed == 0:
        return random.choice(list0)

def nonekurisubmaker(ed):
    list1=[1,]
    list2=[1,2]
    list3=[1,2,3]
    list4=[1,2,3,4]
    list5=[5]
    list6=[1,5,6]
    list7=[1,2,5,6,7]
    list8=[1,2,3,5,6,7,8]
    list9=[1,2,3,4,5,6,7,8,9] #1や5も引けるが次に同じ数を足す重複を防ぐ
    if ed == 1:
        return random.choice(list1)
    elif ed == 2:
        return random.choice(list2)
    elif ed == 3:
        return random.choice(list3)
    elif ed == 4:
        return random.choice(list4)
    elif ed == 5:
        return random.choice(list5)
    elif ed == 6:
        return random.choice(list6)
    elif ed == 7:
        return random.choice(list7)
    elif ed == 8:
        return random.choice(list8)
    elif ed == 9:
        return random.choice(list9)

#五玉繰り上がりの発生確率は約12%のため"level2:五玉繰り上がりあり"を選択した場合はランダムの数をある程度指定する。
def fivemaker(ed):
    list1=[4,6] #１の時は4しか５玉分解にならないため
    list2=[3,3,4,4,5,6,7]
    list3=[2,2,3,3,4,4,5,6]
    list4=[1,2,3,4,]
    list5=[1,2,3,4]
    list6=[2,2,3,3,4,4,5]
    list7=[3,3,4,4,5,6]
    list8=[4,6] #8の時は4しか５玉分解にならないため
    if ed == 1:
        return random.choice(list1)
    elif ed == 2:
        return random.choice(list2)
    elif ed == 3:
        return random.choice(list3)
    elif ed == 4:
        return random.choice(list4)
    elif ed == 5:
        return random.choice(list5)
    elif ed == 6:
        return random.choice(list6)
    elif ed == 7:
        return random.choice(list7)
    elif ed == 8:
        return random.choice(list8)

#五玉繰り上がりありを選択した場合、足される数が1以上4以下と5以上8以下の数が多いほうで足し算引き算を決める
def fivenumberchecker(a):
    addcount = 0
    subcount = 0
    for i in range(1,len(a)):
        if (a[i] >=1) and (a[i] <=4):
            addcount += 1
        elif (a[i] >=5) and (a[i] <=8):
            subcount += 1
    if addcount >= subcount:
        return 1
    else:
        return 0

def addtenmaker(ed): #五玉繰り上がりなし十玉繰り上がりありの場合、十玉繰り上がりの機会を増やす必要がある
    list1=[9,9,9,2,5,6,7] 
    list2=[8,8,8,9,9,9,]
    list3=[7,7,7,8,8,8,9,9,9,5]
    list4=[6,7,8,9]
    list5=[5,5,5,1,2,3]
    list6=[9,9,4,4,5,5,1,2] 
    list7=[8,9,3,4,5]
    list8=[2,3,4,5,7,8,9]
    list9=[2,3,4,6,7,8,9]
    if ed % 5 == 1:
        return random.choice(list1)
    elif ed % 5 == 2:
        return random.choice(list2)
    elif ed % 5 == 3:
        return random.choice(list3)
    elif ed % 5 == 4:
        return random.choice(list4)
    elif ed == 5:
        return random.choice(list5)

def subtenmaker(ed): #五玉繰り上がりなし十玉繰り上がりありの場合、十玉繰り上がりの機会を増やす必要がある
    list1=[9,8,7,5,4,3,2] 
    list2=[9,9,8,8,5,5,4,4,3,3,1,2]
    list3=[9,9,5,5,4,4,1,2,3]
    list4=[5,5,5,2,3,4]
    list5=[9,9,8,8,7,7,6,6,5]
    list6=[9,9,8,8,7,7,5]
    list7=[9,9,8,8,5,6]
    list8=[9,9,9,2,3,5]
    if ed  == 1:
        return random.choice(list1)
    elif ed == 2:
        return random.choice(list2)
    elif ed == 3:
        return random.choice(list3)
    elif ed == 4:
        return random.choice(list4)
    elif ed == 5:
        return random.choice(list5)
    elif ed == 6:
        return random.choice(list6)
    elif ed == 7:
        return random.choice(list7)
    elif ed == 8:
        return random.choice(list8)

#見取り算を一問作成する
def sorobanmitori(dic,a,num):
#@param dic 見取り算の桁数を指定　横
#@param a 難易度を指定
#@param num 口数を指定(項数）　縦
#aの難易度
#a = 1:level1のみ
#a = 2:level5まで含む
#a = 3:level10まで含む
#a = 4:二桁以上の繰り上がり含む　level10が連続２回以上
#a = 5:すべての要素含む
    F = np.zeros((dic + 1),dtype = int)
    formula = np.zeros((num,dic+1),dtype = int)
    for number in range(num):#問題数分繰り返す
        judge = random.randint(1,2) % 2 #judgeには0か1がランダムで代入され1ならば足し算、0ならば引き算
        if F[0] == 0 and F[1] <= 1: #最高位が1以下の場合は足し算
            judge = 1
        elif (a == 1 or a == 3) and F[1] == 5:
            judge = 1
        elif (a == 3 and F[0] % 5 == 4 and F[1] % 5 == 4) or (a == 4 and F[0] % 10 == 9 and F[1] == 9): #最高位の足す数が０になるのを防ぐ
            judge = 0
        elif (a == 1 or a == 2) and (F.max() == 9):
            #'level5'までで足される数に9が含まれている場合は引き算
            judge = 0
        elif (a == 2) and (fivenumberchecker(F) == 1):
            judge = 1
        elif (a == 2) and (fivenumberchecker(F) == 0):
            judge = 0


        if judge == 1: 
            for i in range(1,dic+1):
#指定した桁数分を桁ごと
                for count in range(100): #無限ループを避けるため有限回
                    if count == 99:
                        print(F,formula)
                    formula[number,i] = random.randint(1,9)
                    if a ==1 or a == 2: #足される数が９の場合、十玉繰り上がりなしでは０しか条件を満たさない
                        if F[i] == 9:
                            formula[number,i] = 0
                            break
                        elif a == 1:
                            formula[number,i] = nonekuriaddmaker(F[i])
                            F[i] += formula[number,i]
                            break
                    if (a == 3 and F[i-1] % 5 == 4) or (a == 4 and F[i-1] % 10 == 9):
                        if F[i] == 9:
                            formula[number,i] = 0
                            break
                        elif a == 3:
                            formula[number,i] = nonekuriaddmaker(F[i])
                            F[i] += formula[number,i]
                            break
                        elif a == 4:
                            if F[i] >= 5 or F[i] == 0:
                                formula[number,i] = nonekuriaddmaker(F[i])
                                F[i] += formula[number,i]
                                break
                            else:
                                formula[number,i] = fivemaker(F[i])
                                F[i] += formula[number,i]
                                break
                    if (a == 2) and ((F[i] >= 1) and (F[i] <=4)): #五玉繰り上がりありの場合五玉分解の機会を増やす
                            formula[number,i] = fivemaker(F[i])
                    if a == 3 and F[i-1] != 4 and (F[i] >= 1 and F[i] <= 8):
                        formula[number,i] = addtenmaker(F[i])
                    if (formula[number-1,0] != 9) or (formula[number,i] != formula[number-1,i]): #同じ数字で足し引きを防ぐ                    
                        if addlevel(F[i],formula[number,i]) =="level1": #繰り上がりなしの場合
                            if a != 4 or (F[i] == 5 or F[i] ==0) or F[i-1] == 9:
                                F[i] += formula[number,i]
                                break
                        elif addlevel(F[i],formula[number,i]) =="level5": #五玉繰り上がりありの場合
                            if a == 2 or a >= 4:
                                F[i] += formula[number,i]
                                break
                        elif addlevel(F[i],formula[number,i]) =="level10": #十繰り上がりありの場合
                            if (a ==3 or a ==4) and (F[i-1] % 10 != 9): #「五玉くりあがりなし十繰り上がりあり」または「十繰り上がりあり」かつ「二けた以上繰り上がりなし」の場合
                                if a != 3 or F[i-1] != 4:
                                    F[i-1] += 1
                                    F[i] -= (10 - formula[number,i])
                                    break
                            elif a >=5:#二けた以上繰り上がりありの場合
                                for up in range(i,0,-1): 
                                    if F[up-1] == 9:
                                        if up == 1:
                                            F[up-1] +=1
                                            F[i] -= (10 - formula[number,i])
                                            break
                                        else:
                                            F[up-1] -= 9
                                    else:
                                        F[up-1] += 1
                                        F[i] -= (10 - formula[number,i])
                                        break
                                break
                        elif addlevel(F[i],formula[number,i]) =="level100": #分解ありの場合
                            if a >= 6:
                                for up in range(i,0,-1):
                                    if F[up-1] == 9:
                                        if up == 1:
                                            F[up-1] +=1
                                            F[i] -= (10 - formula[number,i])
                                            break
                                        else:
                                            F[up-1] -= 9
                                    else:
                                        F[up-1] += 1
                                        F[i] -= (10 - formula[number,i])
                                        break
                                break
        if judge == 0: #引き算
            formula[number,0] = 9 #引き算であることをわかりやすくするため引き算の場合はformulaの最高位を9とする
            if (a  == 1 or a == 2) and F[1] == 0: #F =[003423]の時など
                formula[number,1] = 0 
            elif a >=3 and F[0] != 0: #F =[203456]の時など
                for count in range(100):
                    if count == 99:
                        F[i] = warning
                    formula[number,1] = random.randint(1,9)
                    if a == 3 and (F[1] >= 1 and F[1] <= 8):
                        formula[number,1] = subtenmaker(F[1])
                    if a == 1 and F[1] == 9:
                        formula[number,1] = random.choice([2,3,4,6,7,8]) #繰り下がりなしの場合9から1または５を引いたとき次に同じ数を足してしまうことを回避
                        F[1] -= formula[number,1]
                        
                    if sublevel(F[1],formula[number,1]) == "level100":
                        if a >= 6:
                            F[0] -= 1
                            F[1] += (10 - formula[number,1])
                            break
                    elif sublevel(F[1],formula[number,1]) == "level10":
                        if F[0] % 10 == 0: #二桁以上繰り下がりの場合
                            if a >= 5:
                                F[0] -= 1
                                F[1] += (10 - formula[number,1])
                                break    
                        else:
                            F[0] -= 1
                            F[1] += (10 - formula[number,1])
                            break
                    elif sublevel(F[1],formula[number,1]) == "level5":
                        if a >= 4:
                            F[1] -= formula[number,1]
                            break
                    else: #level1の時
                        F[1] -= formula[number,1]
                        break
            elif a == 1 and F[1] == 5: #level1でF[1] == 5 のときは-5しかないため
                formula[number,1] = 5
                F[1] -= formula[number,1]
            elif (a == 1 or a == 2) and F[1] == 9:
                formula[number,1] = random.choice([2,3,4,6,7,8]) #繰り下がりなしの場合9から1または５を引いたとき次に同じ数を足してしまうことを回避
                F[1] -= formula[number,1]
            elif (a == 2) and ((F[1] >= 5) and (F[1] <=8)): #五玉繰り上がりありの場合五玉分解の機会を増やす
                for count in range(100): #無限ループを避けるため有限回
                    if count == 99:
                        F[i] = warning
                    formula[number,1] = fivemaker(F[1])
                    if (formula[number-1,0] != 0) or (formula[number,1] != formula[number-1,1]):
                        break
                F[1] -= formula[number,1]
            else:
                for count in range(100):
                    if count == 99:
                        F[i] = warning
                    formula[number,1] = random.randint(1,F[1]-1) #formulaの最高位は引かれる数を超えないために引く数を1以上は小さくする。
                    if sublevel(F[1],formula[number,1]) == 'level5':
                        if (a == 2) or (a >= 4):
                            F[1] -= formula[number,1]
                            break
                    else:
                        F[1] -= formula[number,1]
                        break
                
                    
            for i in range(2,dic + 1):
                for count in range(100): #無限ループを避けるため有限回
                    if count == 99:
                        print(F)
                    if (a == 1 or a == 2) and F[i] == 0:
                        formula[number,i] = 0
                        break
                    elif (a == 1 or a == 2) and F[i] == 9:
                        formula[number,i] = random.choice([2,3,4,6,7,8]) #繰り下がりなしの場合9から1または５を引いたとき次に同じ数を足してしまうことを回避
                        F[i] -= formula[number,i]
                        break
                    elif (a == 3 and F[i-1] % 5 == 0) or (a == 4 and F[i-1] % 10 == 0):
                        if F[i] == 0:
                            formula[number,i] = 0
                            break
                        elif a == 3:
                            formula[number,i] = nonekurisubmaker(F[i])
                            F[i] -= formula[number,i]
                            break
                        elif a == 4:
                            if F[i] <= 4 or F[i] == 9:
                                formula[number,i] = nonekurisubmaker(F[i])
                                F[i] -= formula[number,i]
                                break
                            else:
                                formula[number,i] = fivemaker(F[i])
                                F[i] -= formula[number,i]
                                break
                                
                    else:
                        formula[number,i] = random.randint(1,9)
                        if a == 1:
                            formula[number,i] = nonekurisubmaker(F[i])
                        if (a == 2) and ((F[i] >= 5) and (F[i] <=8)): #五玉繰り下がりありの場合は五玉繰り下がりの機会を意図的に増やす必要がある
                            formula[number,i] = fivemaker(F[i])
                        if a == 3 and F[i-1] != 5 and (F[i] >= 1 and F[i] <= 8):
                            formula[number,i] = subtenmaker(F[i])
                        if sublevel(F[i],formula[number,i]) == "level1":
                            if a != 4 or (F[i] == 9 or F[i] == 4) or F[i-1] == 0:
                                F[i] -= formula[number,i]
                                break
                        elif sublevel(F[i],formula[number,i]) == "level5":
                            if (a ==2) or (a >= 4): #五玉繰り上がりありの場合
                                F[i] -= formula[number,i]
                                break
                        elif sublevel(F[i],formula[number,i]) == "level10":
                            if (a ==3 or a == 4):#十繰り下がりありかつ二けた以上繰り下がりなしの場合
                                if F[i-1] != 0:
                                    if a != 3 or F[i-1] != 5:
                                        F[i-1] -= 1
                                        F[i] += (10 - formula[number,i])
                                        break
                            elif a >= 5:        
                                for down in range(i,0,-1):
                                    if F[down-1] ==0:
                                        F[down-1] +=9
                                    else:
                                        F[down-1] -= 1
                                        F[i] += (10 - formula[number,i]) ####
                                        break
                                break
                        elif sublevel(F[i],formula[number,i]) =="level100":
                            if a >=6: #分解ありの場合
                                for down in range(i,0,-1):
                                    if F[down-1] ==0:
                                        F[down-1] +=9
                                    else:
                                        F[down-1] -= 1
                                        F[i] += (10 - formula[number,i])
                                        break
                                break
    
    #それぞれの要素にコンマをうち文字列型に変換する
    formulalist = formula.tolist()
    strlist = [list("".join(map(str,formulalist[i]))) for i in range(num)]
    answer = list("".join(map(str,F.tolist())))
    for j in range(num):
        for i in range(dic-2,1,-3):
            strlist[j].insert(i,",")
        for i in range(100):
            if strlist[j][0] == "0" and (strlist[j][1] == "0" or strlist[j][1] == ","):
                strlist[j].pop(0)
            elif strlist[j][0] == ",":
                strlist[j].pop(0)
            elif strlist[j][0] == "0" and (strlist[j][1] != "0" and strlist[j][1] != ","):
                strlist[j][0] = ""
                break
            elif strlist[j][0] == "9":
                strlist[j][0] = "-"
                break
    for i in range(len(answer)-3,0,-3):
        answer.insert(i,",")
    for i in range(len(answer)):
        if (answer[0] == "0") or (answer[0] == ",") :
            answer.pop(0)
        else:
            break
    formulastrlist = ["".join(strlist[i]).rjust(dic + int((dic - 1) / 3)+1) for i in range(num)]
    formulastrlist.insert(0,"".join(answer)) #strlistの一つ目の要素は答え

    return formulastrlist
    