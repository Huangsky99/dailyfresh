from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'df_street/index.html', {'title': "home"})


def lists(request):
    return render(request, 'df_street/list.html', {'title': 'lists'})


def cart(request):
    return render(request, 'df_street/cart.html', {'title': 'cart'})


def detail(request):
    return render(request, 'df_street/detail.html', {'title': 'detail'})


def order(request):
    return render(request, 'df_street/place_order.html', {'title': 'order'})


def user_info(request):
    return render(request, 'df_street/user_center_info.html', {'title': 'user_info'})


def user_order(request):
    return render(request, 'df_street/user_center_order.html', {'title': 'user_order'})


def user_site(request):
    return render(request, 'df_street/user_center_site.html', {'title': 'user_site'})
