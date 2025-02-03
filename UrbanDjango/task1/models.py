from django.db import models


# Create your models here.
class Buyer(models.Model):  # модель представляющая покупателя.
    name = models.CharField(max_length=100)  # имя покупателя(username аккаунта)
    # для хранения чисел до 999.99 с разрешением 2 знака после запятой
    # models.DecimalField(..., max_digits=5, decimal_places=2)
    balance = models.DecimalField(decimal_places=2, max_digits=6)  # баланс(DecimalField)
    age = models.IntegerField()  # возраст.


class Game(models.Model):  # модель представляющая игру.
    title = models.CharField(max_length=100)  # название игры
    cost = models.DecimalField(decimal_places=2, max_digits=4)  # цена(DecimalField)
    size = models.DecimalField(decimal_places=2, max_digits=4)  # размер файлов игры(DecimalField)
    description = models.TextField()  # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+ (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='games')  # покупатель обладающий игрой (ManyToManyField).
    # У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.
    # DecimalField - поле для дробных чисел.
    # BooleanField - поле для булевых значений.


# (mvenv) PS C:\module_19> cd UrbanDjango
# (mvenv) PS C:\module_19\UrbanDjango> python manage.py shell
# >>> from task1.models import Buyer
# >>> Buyer.objects.all()
# >>> Buyer.objects.create(name='Peter', balance=1500.99, age=22)
# >>> Buyer.objects.create(name='Slawa', balance=27, age=19)
# >>> Buyer.objects.create(name='Alex', balance=0.5, age=14)
# >>> Buyer.objects.count()
#
# >>> from task1.models import Game
# >>> Game.objects.create(title='CyberPunk 2077', cost=31, size=46.2, description='Game of the year', age_limited=1)
# >>> Game.objects.create(title='Mario', cost=5, size=0.5, description='Old Game', age_limited=0)
# >>> Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kills Mark?', age_limited=1)
# >>> Game.objects.count()
#
# >>> Game.objects.get(id=3).buyer.set((1,2))
# >>> Game.objects.get(id=2).buyer.set((3,2))
# >>> Game.objects.get(id=1).buyer.set((1,2))

