from django.http import HttpResponse
from django.shortcuts import render
def myfun(request):
    #content={
       # "name":"you are best",
        #"number":[1,2,3,4,5,6,7,8]
    #}
    
    return render(request,'utilities.html')
'''<nav style="margin:70px;"> 
<a href="www.google.com" style="margin:20px;">google</a>
<a href="www.facebook.com" style="margin:20px;">facebook</a>
<a href="www.youtube.com" style="margin:20px;">youtube</a>
<a href="www.apple.com" style="margin:20px;">apple</a></nav>'''


def removepunctuation(request):
    inputtext=request.POST.get('text','default')
    removepunctuation=request.POST.get('removepunctuation','off')
    capitalize=request.POST.get('capitalize','off')
    spaceremover=request.POST.get('spaceremover','off')

    if removepunctuation =='on':
        punctuations='''!@#$%^&*"":;''{}[]()'''
        analyzed=""
        for char in inputtext:
            if char not in punctuations:
                analyzed=analyzed + char
        user_text={'task':'AFTER Removed-punctation BELOW','analyzed_text':analyzed}
        inputtext=analyzed
    
    if capitalize=='on':
        analyzed=""
        for char in inputtext:
                analyzed=analyzed + char.upper()
        user_text={'task':'after changing to capital','analyzed_text':analyzed}
        inputtext=analyzed
    
    if spaceremover=='on':
        analyzed=""
        for  index, char in enumerate(inputtext):
                if not (inputtext[index]==" " and  inputtext[index + 1]==" "):
                    analyzed=analyzed + char

        user_text={'task':'after removing space','analyzed_text':analyzed}
        inputtext=analyzed

    if(removepunctuation!='on' and capitalize!='on' and spaceremover!='on'):
        return HttpResponse("you are not selected any operation")
    return render(request,'analyzed.html',user_text)
    

    #else:
       # return HttpResponse('ERROR-your text has not been analyzed')


def spaceremover(request):
   return HttpResponse("spaceremover")

def capitalize(request):
   return HttpResponse("capitalize")


def home(request):
   return HttpResponse("hi home")

def about(request):
    return HttpResponse("hello")