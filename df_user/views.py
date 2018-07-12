from django.shortcuts import render
from models import UserInfo, AddressInfo


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'df_user/register.html')
    else:
        body = request.body
        uname = body.get('user_name')
        upwd = body.get('pwd')
        upwd2 = body.get('cpwd')
        uemail = body.get('email')
