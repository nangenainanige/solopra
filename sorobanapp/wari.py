import random
from sys import modules

def wari(eddig,ingdig,question):
    warizan = [[[] for j in range(10)] for i in range(question)]
    warizanans = [[[] for j in range(10)] for i in range(question)]
    for i in range(question):
        for j in range(10):
            if eddig == ingdig:
                if eddig ==1:
                    ans = random.randint(2,4)
                elif eddig ==2:
                    ans = random.randint(2,7)
                else:
                    ans = random.randint(2,9)
                ed = random.randint(10**(eddig-1)*ans,10**(eddig)-1)
                mod = ed % ans
                if ed + (ans - mod) >= 10**(eddig):
                    ed -= mod
                else:
                    ed += (ans-mod)
                ing = int(ed / ans)
                    
            else:
                ed = random.randint(10**(eddig-1),10**(eddig) - 1)
                if ingdig == 1:
                    ing = random.randint(2,9)
                else:
                    ing = random.randint(10**(ingdig-1),10**(ingdig) - 1)
                mod = ed % ing
                if ed + (ing - mod)>= 10**(eddig):
                    ed -= mod
                else:
                    ed += (ing - mod)
                ans = int(ed / ing)
            warizan[i][j] = [10*i + j +1, f'{ed:,}', f'{ing:,}', f'{ans:,}' ]
            warizanans[i][j] = [10*i + j +1, f'{ed:,}', f'{ing:,}', f'{ans:,}' ]
            if ans < 10**(eddig - ingdig):
                if (eddig - ingdig + 1) % 3 == 1:
                    warizan[i][j][3] = "a"+ f'{ans:,}'
                else:
                    warizan[i][j][3] = "b"+ f'{ans:,}'
    warizan_ =[warizan,warizanans]
    return warizan_
            

            