from django.shortcuts import render, redirect
from models import UserInfo, AddressInfo
from hashlib import sha1


# Create your views here.
def register(request):
    if request.method == 'GET':
        context = {'title': 'sign up'}
        return render(request, 'df_user/register.html', context)
    elif request.method == 'POST':
        body = request.POST
        uname = body.get('user_name')
        upwd = body.get('pwd')
        upwd2 = body.get('cpwd')
        uemail = body.get('email')

        if upwd != upwd2:
            return redirect('/user/register/')

        s1 = sha1()
        s1.update(upwd)
        upwd3 = s1.hexdigest()

        user = UserInfo()
        user.uname = uname
        user.upwd = upwd3
        user.uemail = uemail

        user.save()

        return redirect('/user/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'df_user/login.html')
