from unicodedata import digit, name
from django import forms
from django.core.validators import MaxValueValidator,MinValueValidator


class TextForm(forms.Form):
    levelch = (
    #見取り算
    (1,"繰り上がりなし"),
    (2,"五玉分解あり十分解なし"),
    (3,"五玉分解なし十分解あり"),
    (4,"五玉分解あり十分解あり"),
    (5,"二桁以上繰り上がりあり"),
    (6,"すべて"),)
    digitch = tuple((i,str(i)) for i in range(1,21))
    qnumberch = tuple((i,str(i)) for i in range(2,21)) 
    questionch = tuple((i,str(i)+"問") for i in range(1,51))
    digit = forms.ChoiceField(choices = digitch)
    level = forms.ChoiceField(choices =levelch)
    qnumber = forms.ChoiceField(choices = qnumberch)
    questionnum = forms.ChoiceField(choices=questionch)

    #掛け算
    Kakeeddigitch = tuple((i,str(i)) for i in range(1,8))
    Kakeingdigitch = tuple((i,str(i)) for i in range(1,8))
    Kakequestionch = (
        (1,"10問"),
        (2,"20問"),
        (3,"30問"),
        (4,"40問"),
        (5,"50問"),
        (6,"60問"),
        (7,"70問"),
        (8,"80問"),
        (9,"90問"),
        (10,"100問"))
    Kakeeddigit = forms.ChoiceField(choices = Kakeeddigitch)
    Kakeingdigit = forms.ChoiceField(choices = Kakeingdigitch)
    Kakequestion = forms.ChoiceField(choices = Kakequestionch)

    #割り算
    warieddigitch = tuple((i,str(i)) for i in range(1,21))
    wariingdigitch = tuple((i,str(i)) for i in range(1,21))
    wariquestionch = (
        (1,"10問"),
        (2,"20問"),
        (3,"30問"),
        (4,"40問"),
        (5,"50問"),
        (6,"60問"),
        (7,"70問"),
        (8,"80問"),
        (9,"90問"),
        (10,"100問"))
    warieddigit = forms.ChoiceField(choices = warieddigitch)
    wariingdigit = forms.ChoiceField(choices = wariingdigitch)
    wariquestion = forms.ChoiceField(choices = wariquestionch)

class ContactForm(forms.Form):
    name = forms.CharField()
    sender = forms.EmailField(label='Email')
    checksender = forms.EmailField(label='Email')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)  
# , widget= forms.TextInput(attrs={'placeholder':'桁数を入力'})
#  widget= forms.TextInput(attrs={'placeholder':'口数を入力'})