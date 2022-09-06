from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import userForms
from news.models import News
from contact.models import Contact
from django.core.mail import send_mail

def homePage(request):
    send_mail(
        'testing mail',
        'Hello dear, Here is the message.',
        'zahidriaz337@gmail.com',
        ['zahidriaz371@gmail.com'],
        fail_silently=False,
    )
    newsData = News.objects.all();
    data = {
        'newsData' : newsData
    }

    # data = {
    #     'title':'Home Page',
    #     'list': ['zahid','amajd','tariq'],
    #     'number':[10, 20, 30, 40],
    #     'detail':[
    #         {'name':'zahid', 'number':'54321'},
    #         {'name':'amjad', 'number':'98760'}
    #     ]
    # }
    return render(request, 'index.html', data)

def aboutUs(request):
    return HttpResponse('welcome my firstProject')

def Course(request):
    return HttpResponse('welcome my Course')

def courseDetail(request,courseid):
    return HttpResponse(courseid)

def userForm(request):
    fn = userForms()
    data = {'form':fn}
    try:
        if request.method=='POST':
            n1=request.POST['username']
            n2=request.POST['password']
            n3=request.POST['confirmPassword']
            print(n1, n2, n3)
            data = {
                'form':fn
            }

            return HttpResponseRedirect('/about-us/')
    except:
        pass
    return render(request, 'userform.html', data)

def calculator(request):
    c = ''
    try:
        if request.method=="POST":
            num1 = eval(request.POST.get('Num1'))
            num2 = eval(request.POST.get('Num2'))
            opr = request.POST.get('opr')
            if opr == '+':
                c = num1 + num2
            elif opr == '-':
                c = num1 - num2
            elif opr == '*':
                c = num1 * num2
            elif opr == '/':
                c = num1 / num2
    except:
        c = 'invalid operation'
    print(c)
    return render(request, 'calculator.html',{'c':c})

def evenOdd(request):
    c = ''
    try:
        if request.method=="POST":
            num = eval(request.POST.get('Num'))
            if num%2 == 0:
                c = 'Even Number'
            else: 
                c = 'Odd Number'
    except:
        c = 'invalid operation'
    print(c)
    return render(request, 'evenOdd.html',{'c':c})

def saveContact(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        about=request.POST.get('about')

        en= Contact(User_Name=username, Password=password, Confirm_Password=confirmPassword, Email=email, Phone=phone, About_Yourself=about)
        en.save()

    return render(request, 'contact.html')