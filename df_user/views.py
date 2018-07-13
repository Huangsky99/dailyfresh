from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from models import UserInfo
from hashlib import sha1


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'df_user/register.html', {'title': 'sign up'})

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


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login(request):
    if request.method == 'GET':
        uname = request.COOKIES.get('uname', '')
        return render(request, 'df_user/login.html', {'title': 'sign in', 'uname': uname, 'error': 0})

    elif request.method == 'POST':
        body = request.POST
        uname = body.get('username')
        upwd = body.get('pwd')
        uremember = body.get('remember', 0)

        users = UserInfo.objects.filter(uname=uname)
        if len(users) < 1:
            return render(request, 'df_user/login.html', {'title': 'sign in', 'uname': uname, 'error': 1})

        sha = sha1()
        sha.update(upwd)
        if sha.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/street/index/')

            if uremember:
                red.set_cookie('uname', uname)

            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
