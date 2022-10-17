from asyncio import QueueEmpty
#from msvcrt import kbhit
from sre_constants import MIN_REPEAT_ONE
from django.shortcuts import render, redirect
from .forms import TextForm as tf
from .mitori2 import sorobanmitori
from .kake import kake
from .wari import wari
import numpy as np
import random
from .table import table
from .forms import ContactForm as CF
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail

def index(request):
    params = {
        "title" : "hello",
        'top':'index',
        "goto" : "mitorizan",
    }
    return render(request, 'soroban/top.html',params)

def mitorizan(request):
    #return render(request, "soroban/frontpage.html")
    #f = TextForm()
    params = {
        'title':'見取り算',
        'top':'index',
        }
    if (request.method == 'POST'):
        digit = int(request.POST.get('digit',False)) #桁数
        level = int(request.POST.get('level',False)) #難易度
        qnumber = int(request.POST.get('qnumber',False)) #口数
        questionnum = int(request.POST.get('questionnum',False)) #問題数
        kuchinum = [i+1 for i in range(qnumber)]
        mitoriza = [sorobanmitori(digit,level,qnumber) for i in range(questionnum)]
        for i in range(questionnum):
            mitoriza[i].insert(0,str(i+1))
        params["mitorizan"] = mitoriza
        params["kuchinum"] = kuchinum
        tablelist = table(digit,questionnum)
        params["tableborder"] = tablelist[0]
        linenumber = ["" for i in range(tablelist[1])]
        params["linenumber"] = linenumber
        imputform = tf(initial={
            "digit":digit,
            "level":level,
            'qnumber':qnumber,
            'questionnum':questionnum})
        params["form"] = imputform
        if level == 1:
            qID = random.randint(100000,199999)
        elif level == 2:
            qID = random.randint(200000,299999)
        elif level == 3:
            qID = random.randint(300000,399999)
        elif level == 4:
            qID = random.randint(400000,499999)
        elif level == 5:
            qID = random.randint(500000,599999)
        elif level == 6:
            qID = random.randint(600000,699999)
        params["ID"] = qID
        params["message"] = "nonemessage"
        params["clickmessage"]="clickmessage"
    else:
        imputform = tf(initial={
            "digit":1,
            "level":1,
            'qnumber':1,
            'questionnum':1})
        params["form"] = imputform
        params["message"] = "message"
        params["clickmessage"] = "noneclickmessage"
    return render(request, 'soroban/mitori.html',params)

def kakezan(request):
    params = {
        'title':'かけ算',}
    if (request.method == 'POST'):
        Kakeeddigit = int(request.POST.get('Kakeeddigit',False)) #桁数
        Kakeingdigit = int(request.POST.get('Kakeingdigit',False)) #難易度
        Kakequestion = int(request.POST.get('Kakequestion',False)) #口数
        imputform = tf(initial={
            "Kakeeddigit":Kakeeddigit,
            "Kakeingdigit":Kakeingdigit,
            'Kakequestion':Kakequestion})
        kakezan = kake(Kakeeddigit,Kakeingdigit,Kakequestion)
        params["kakezan"] = kakezan[0]
        params["kakezanans"] = kakezan[1]            
        params["form"] = imputform
        params["message"] = "nonemessage"
        params["clickmessage"]="clickmessage"
    else:
        imputform = tf(initial={
        "Kakeeddigit":1,
        "Kakeingdigit":1,
        "Kakequestion":1})
        params["form"] = imputform
        params["message"] = "message"
        params["clickmessage"]="noneclickmessage"
    return render(request, 'soroban/kake.html',params)

def warizan(request):
    params = {
        'title':'わり算',}
    if (request.method == 'POST'):
        warieddigit = int(request.POST.get('warieddigit',False)) #桁数
        wariingdigit = int(request.POST.get('wariingdigit',False)) #難易度
        wariquestion = int(request.POST.get('wariquestion',False)) #口数
        imputform = tf(initial={
            "warieddigit":warieddigit,
            "wariingdigit":wariingdigit,
            'wariquestion':wariquestion})
        warizan = wari(warieddigit,wariingdigit,wariquestion)
        params["warizan"] = warizan[0]
        params["warizanans"] = warizan[1]    
        params["form"] = imputform
        params["message"] = "nonemessage"
        params["clickmessage"]="clickmessage"
    else:
        imputform = tf(initial={
        "warieddigit":1,
        "wariingdigit":1,
        "wariquestion":1})
        params["form"] = imputform
        params["message"] = "message"
        params["clickmessage"]="noneclickmessage"
    return render(request, 'soroban/wari.html',params)


def contact(request):
    if request.method == 'POST':
        form = CF(request.POST)
        

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            

            mes_sen = message +"\n" + sender
            
            send_mail(name,mes_sen,"solopra.official@gmail.com",["solopra.official@gmail.com"])

            
            # if BadHeaderError:
            #     return HttpResponse('無効なヘッダーが見つかりました')
            return redirect('complete')

    else:
        form = CF()

    return render(request, 'soroban/contact.html', {'form': form})

def complete(request):
    return render(request, 'soroban/complete.html')
# Create your views here.
