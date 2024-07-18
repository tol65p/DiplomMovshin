from django.db import models

# Create your models here.
class Users(models.Model):
    nickname = models.CharField(max_length=20, help_text='Псевдоним:', unique=True)
    password = models.CharField(max_length=20, help_text='Пароль:')
    email = models.EmailField(help_text='e-mail:', unique=True)

    def __str__(self):
        return f'{self.nickname}   {self.password}   {self.email}'

class Runners(models.Model):
    genders = [('men', 'м'), ('women', 'ж')]
    user = models.OneToOneField('Users', on_delete=models.CASCADE)
    fam = models.CharField(max_length=20, help_text='Фамилия:')
    name = models.CharField(max_length=20, help_text='Имя:')
    gender = models.CharField(max_length=5, choices=genders, help_text='Пол:', db_index=True)
    birthday = models.DateField(help_text='Дата рождения:')
    city = models.CharField(max_length=30, help_text='Город / нас.п.:')
    tel = models.CharField(max_length=20, help_text='Телефон:', blank=True)
    sportTeam = models.CharField(max_length=20, help_text='Команда:', blank=True)
    identKod = models.BigIntegerField(help_text='Идент. код:', unique=True)

    def __str__(self):
        return f'{self.user}   {self.fam}   {self.name}   {self.gender}   {self.birthday}   {self.city}   {self.sportTeam}   {self.identKod}'

class Events(models.Model):
    date = models.DateField(help_text='Дата пробега:')
    city = models.CharField(max_length=30, help_text='Город / нас.п.:')
    distance = models.DecimalField(max_digits=6, decimal_places=3, help_text='Дистанция, км:')
    price = models.PositiveSmallIntegerField(help_text='Стоимость, грн:')

    def __str__(self):
        return f'{self.date}   {self.city}    {self.distance} км    {self.price} грн'

class AgeCategory(models.Model):
    event = models.ForeignKey('Events', on_delete=models.CASCADE, db_index=True)
    age_do = models.PositiveSmallIntegerField(help_text='возраст до:')
    category = models.CharField(max_length=10, help_text='Возрастная категория:')

    def __str__(self):
        return f'{self.event}   {self.age_do}   {self.category}'
class CheckPoints(models.Model):
    event = models.ForeignKey('Events', on_delete=models.CASCADE, db_index=True)
    distance = models.DecimalField(max_digits=6, decimal_places=3, help_text='Расстояние от Старта, км:')

    def __str__(self):
        return f'{self.event}    КП {self.distance} км'

class Protokols(models.Model):
    event = models.ForeignKey('Events', on_delete=models.CASCADE, db_index=True)
    runner = models.ForeignKey('Runners', on_delete=models.CASCADE)
    category = models.ForeignKey('AgeCategory', on_delete=models.CASCADE, default=None)
    discount = models.PositiveSmallIntegerField(help_text='скидка, %:', default=0)
    oplata = models.DecimalField(max_digits=7, decimal_places=2, help_text='Оплата, грн:', default=0)
    finresult = models.TimeField(help_text='Финишный результат:')

    def __str__(self):
        return f'{self.event}   {self.runner} {self.category}   {self.discount} %  {self.oplata} грн    {self.finresult}'

class ResultDetail(models.Model):
    protokol = models.ForeignKey('Protokols', on_delete=models.CASCADE)
    check_point = models.ForeignKey('CheckPoints', on_delete=models.CASCADE, help_text='КП ')
    result = models.TimeField(help_text='Результат на КП:')

    def __str__(self):
        return f'{self.protokol}     {self.check_point} км   {self.result}'
