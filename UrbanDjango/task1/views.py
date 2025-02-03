from django.http import HttpResponse
from django.shortcuts import render

from task1.forms import UserRegister
from task1.models import Game, Buyer

users = ["Peter"]


def platform(request):
    data = {"title": "Главная страница"}
    return render(request, "task1/platform.html", data)


def games(request):
    Games = Game.objects.all()
    data = {
        "title": "Игры",
        'games': Games
    }
    return render(request, "task1/games.html", context=data)


def cart(request):
    data = {"title": "Корзина"}
    return render(request, "task1/cart.html", data)


def sign_up_by_html(request):
    Buyers = Buyer.objects.all()
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if int(age) < 18:
            info["error"] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info["error"] = 'Пароли не совпадают'
        else:
            check = False
            for buyer in Buyers:
                if buyer.name == username:
                    check = True
                    break
            if check:
                info["error"] = f'Пользователь {username} уже существует'
            else:
                Buyer.objects.create(name=username, balance=99.99, age=age)
                return HttpResponse(f"Приветствуем, {username}!")

    return render(request, "task1/registration_page.html", info)


def sign_up_by_django(request):
    form = UserRegister()
    info = {"form": form}
    if request.method == "POST":

        form = UserRegister(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if int(age) < 18:
                info["error"] = 'Вы должны быть старше 18'
            elif password != repeat_password:
                info["error"] = 'Пароли не совпадают'
            elif username in users:
                info["error"] = f'Пользователь {username} уже существует'
            else:
                return HttpResponse(f"Приветствуем, {username}!")

    return render(request, "task1/registration_page.html", info)
