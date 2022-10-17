import random


def kake(eddig,ingdig,question):
    kakezan = [[[] for j in range(10)] for i in range(question)]
    kakezanans = [[[] for j in range(10)] for i in range(question)]
    for i in range(question):
        for j in range(10):
            if eddig == 1:
                ed = random.randint(2,9)
            else:
                ed = random.randint(10**(eddig-1),10**(eddig) - 1)
            if ingdig == 1:
                ing = random.randint(2,9)
            else:
                ing = random.randint(10**(ingdig-1),10**(ingdig) - 1)
            ans = ed * ing
            kakezan[i][j] = [10*i + j+1, f'{ed:,}', f'{ing:,}', f'{ans:,}']
            kakezanans[i][j] = [10*i + j+1, f'{ed:,}', f'{ing:,}', f'{ans:,}']
            if ans < 10**(eddig + ingdig -1):
                if (eddig + ingdig) % 3 == 1:
                    kakezan[i][j][3] = "a"+ f'{ans:,}'
                else:
                    kakezan[i][j][3] = "b"+ f'{ans:,}'
    kakezan_ =[kakezan,kakezanans]
    return kakezan_
