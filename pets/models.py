from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    class Meta():
        db_table = 'pet'

    TYPE_CAT = 'cat'
    TYPE_DOG = 'dog'
    TYPE_MOUSE = 'mouse'
    TYPE_GUINEA_PIG = 'guinea pig'
    TYPES = {
        TYPE_CAT: 'кіт',
        TYPE_DOG: 'пес',
        TYPE_MOUSE: 'пацюк',
        TYPE_GUINEA_PIG: 'морська свинка',
    }

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Власник')
    type = models.CharField(max_length=10, choices=TYPES, default=TYPE_CAT, verbose_name='Вид')
    name = models.CharField(max_length=30, verbose_name="Ім'я")
    birth_date = models.DateField(verbose_name='Дата народження')
    photo = models.ImageField(blank=True, upload_to='images/pets', verbose_name='Фото')

    AGE_UNITS = (
        (365, ((5, 'років'), (2, 'роки'), (1, 'рік'))),
        (30, ((5, 'місяців'), (2, 'місяці'), (1, 'місяць'))),
        (7, ((5, 'тижнів'), (2, 'тижні'), (1, 'тиждень'))),
        (1, ((5, 'днів'), (2, 'дні'), (1, 'день'))),
    )
    AGE_DEFAULT = 'щойно'

    @property
    def age(self):
        age = date.today() - self.birth_date

        for size, units in self.AGE_UNITS:
            if age.days < size:
                continue

            age = age.days // size
            for size, unit in units:
                if age >= size:
                    age = f'{age} {unit}'

                    return age

        return self.AGE_DEFAULT
