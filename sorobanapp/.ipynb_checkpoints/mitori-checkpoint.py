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
#五玉繰り上がりの発生確率は約12%のため"level2:五玉繰り上がりあり"を選択した場合はランダムの数をある程度指定する。
def fivemaker(ed):
  list1=[4]
  list2=[3,4]
  list3=[2,3,4]
  list4=[1,2,3,4]
  list5=[1,2,3,4]
  list6=[2,3,4]
  list7=[3,4]
  list8=[4]
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
        if (a == 1 or a == 2) and (F.max() == 9):
            #'level5'までで足される数に9が含まれている場合は強制的に引き算
            judge = 0
        elif F[0] == 0 and F[1] <= 1:
            judge = 1
            #引かれる数の最高位が１以下の場合は足し算　ただしその前の計算において最高位が繰り上がった場合はその限りでない
            #ただし'level1のみ'で F = [00199] などの場合は引き算として処理
        elif (a == 2) and (fivenumberchecker(F) == 1):
            judge = 1
        elif (a == 2) and (fivenumberchecker(F) == 0):
            judge = 0


        if judge == 1: 
            for i in range(1,dic+1):
#指定した桁数分を桁ごと
                for count in range(100): #無限ループを避けるため有限回
                    formula[number,i] = random.randint(1,9)
                    if (a == 2) and ((F[i] >= 1) and (F[i] <=4)):
                        formula[number,i] = fivemaker(F[i])

                    if addlevel(F[i],formula[number,i]) =="level1": #繰り上がりなしの場合
                        F[i] += formula[number,i]
                        break
                    elif addlevel(F[i],formula[number,i]) =="level5": #五玉繰り上がりありの場合
                        if a >= 2:
                            F[i] += formula[number,i]
                            break
                    elif addlevel(F[i],formula[number,i]) =="level10": #十繰り上がりありの場合
                        if a ==3 and F[i-1] != 9: #十繰り上がりありかつ二けた以上繰り上がりなしの場合
                            F[i-1] += 1
                            F[i] -= (10 - formula[number,i])
                            break
                        elif a >=4:#二けた以上繰り上がりありの場合
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
                        if a >= 5:
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
            elif F[0] == 0 and F[1] == 1: #F =[01234]の時などでは
                formula[number,1] = 0
            elif a >=3 and F[0] != 0: #F =[203456]の時など
                formula[number,1] = random.randint(1,9)
                if F[1] < formula[number,1]:
                    F[0] -= 1
                    F[1] += (10 - formula[number,1])
                else:
                    F[1] -= formula[number,1]
            elif a == 1 and F[1] == 5:
                formula[number,1] = 5
                F[1] -= formula[number,1]
            else:
                for i in range(100):
                    formula[number,1] = random.randint(1,F[1]-1) #formulaの最高位は引かれる数を超えないために引く数を1以上は小さくする。
                    if a != 1:
                        F[1] -= formula[number,1]
                        break
                    elif a == 1 and (sublevel(F[1],formula[number,1]) == 'level1'):
                        F[1] -= formula[number,1]
                        break
                
                    
            for i in range(2,dic + 1):
                for count in range(100): #無限ループを避けるため有限回
                    if (a == 1 or a == 2) and F[i] == 0:
                        formula[number,i] = 0
                    else:
                        formula[number,i] = random.randint(1,9)                            
                        if (a == 2) and ((F[i] >= 5) and (F[i] <=8)):
                            formula[number,i] = fivemaker(F[i])
                        if sublevel(F[i],formula[number,i]) == "level1":
                            F[i] -= formula[number,i]
                            break
                        elif sublevel(F[i],formula[number,i]) == "level5":
                            if a >=2: #五玉繰り上がりありの場合
                                F[i] -= formula[number,i]
                                break
                        elif sublevel(F[i],formula[number,i]) == "level10":
                            if a ==3:#十繰り下がりありかつ二けた以上繰り下がりなしの場合
                                if F[i-1] != 0:
                                    F[i-1] -= 1
                                    F[i] += (10 - formula[number,i])
                                    break
                            elif a>=4:        
                                for down in range(i,0,-1):
                                    if F[down-1] ==0:
                                        F[down-1] +=9
                                    else:
                                        F[down-1] -= 1
                                        F[i] += (10 - formula[number,i]) ####
                                        break
                                break
                        elif sublevel(F[i],formula[number,i]) =="level100":
                            if a >=4: #分解ありの場合
                                for down in range(i,0,-1):
                                    if F[down-1] ==0:
                                        F[down-1] +=9
                                    else:
                                        F[down-1] -= 1
                                        F[i] += (10 - formula[number,i])
                                        break
                                break
    
    question = np.zeros(num,dtype = 'int')
    for j in range(num):
        for i in range(dic,0,-1):
            question[j] += formula[j,i] * (10**(dic - i))
        if formula[j,0] == 9:
                c = -question[j]
                question[j] = c
                
                
    return question

#同じ数字で連続して足したり引いたりしていないかのチェック
def checkedmitori(digit,level,number):
    for i in range(100):
        check = sorobanmitori(digit,level,number)
        failjudge = 0
        for checker in range(number-1):
            if check[checker] + check[checker+1] == 0:
                    #同じ数字で連続して足したり引いたりしていないかのチェック
                    failjudge += 1
        if failjudge == 0:
            break
    return check



import pandas as pd
#データフレームとして問題作成を行う
def sorobanquestion(questionnums,digit,level,number):
    #@param questionnums:問題数
    #@param digit:桁数
    #@param level:難易度
    #@param number:口数
    df = pd.DataFrame()
    for questionnum in range(1,questionnums+1):
        for i in range(100):
            check = sorobanmitori(digit,level,number)
            failjudge = 0
            for checker in range(number-1):
                if check[checker] + check[checker+1] == 0:
                    #同じ数字で連続して足したり引いたりしていないかのチェック
                    failjudge += 1
            if failjudge == 0:
                break
        df[questionnum] = check
        
            
    return df