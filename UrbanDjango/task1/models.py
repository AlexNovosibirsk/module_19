from django.db import models


# Create your models here.
class Buyer(models.Model):  # модель представляющая покупателя.
    name = models.CharField(max_length=100)  # имя покупателя(username аккаунта)
    # для хранения чисел до 999.99 с разрешением 2 знака после запятой
    # models.DecimalField(..., max_digits=5, decimal_places=2)
    balance = models.DecimalField(decimal_places=2, max_digits=4)  # баланс(DecimalField)
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
