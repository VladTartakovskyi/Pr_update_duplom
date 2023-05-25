from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
User = get_user_model()
vacancy_group, created = Group.objects.get_or_create(name='Вакансії')
class Vacancies(models.Model):
    posada = models.CharField(max_length=255, verbose_name="Посада")
    firma = models.CharField(max_length=255, verbose_name="Фірма")
    city = models.CharField(max_length=255, null=True, verbose_name="Місто")
    street = models.CharField(max_length=255, null=True, verbose_name="Вулиця")
    salary = models.IntegerField(verbose_name="Заробітна плата", null=True)
    vumogu = models.TextField(blank=True, verbose_name="Вимоги")
    responsibilities = models.TextField(blank=True, verbose_name="Умови праці")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата опублікування")
    pr = models.ForeignKey('Profession', on_delete=models.PROTECT,  verbose_name="Професії")
    kilkbez = models.IntegerField(null=True, verbose_name="Кількість претендентів на вакансію", blank = True)

    def __str__(self):
        return self.posada

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Вільні вакансії'
        verbose_name_plural = 'Вільні вакансії'
        ordering = ['-time_create']

class Profession(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Професія')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('profession', kwargs={'pr_id': self.pk})

    class Meta:
        verbose_name = 'Професія'
        verbose_name_plural ='Професія'
        ordering = ['id']

class Unemployed(models.Model):
    priz = models.CharField(max_length=100, verbose_name="Прізвище", null=True)
    name = models.CharField(max_length=50, verbose_name="Ім'я", null=True)
    pobat = models.CharField(max_length=100, verbose_name="По батькові", null=True)
    city = models.CharField(max_length=100, verbose_name="Місто", null=True)
    street = models.CharField(max_length=50, verbose_name="Вулиця", null=True)
    year = models.IntegerField(verbose_name="Вік", null=True)
    phone_regex = RegexValidator(
        regex=r'^0\d{9}$',
        message="Номер телефону повинен бути в форматі: '0XXXXXXXXX'. 10 цифр."
    )
    nomer_phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Номер телефону", blank=True, null=True)
    em = models.EmailField(verbose_name="Email", null=True)
    special = models.CharField(max_length=100, verbose_name="Спеціальність", null=True)
    vc = models.ForeignKey('Vacancies', on_delete=models.PROTECT, verbose_name="Вакансії", null=True)
    rez = models.FileField(upload_to= 'files/', null=True, verbose_name="Резюме")
    kor = models.CharField(max_length = 100, null=True, verbose_name = "Користувач")
    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.rez)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Безробітні'
        verbose_name_plural ='Безробітні'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Вид послуг')
    def __str__(self):
        return self.name

    def get_absol_url(self):
        return  reverse('category', kwargs={'pr_id': self.pk})

    class Meta:
        verbose_name = 'Вид послуг'
        verbose_name_plural ='Вид послуг'
        ordering = ['id']

class Cursu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва", null=True)
    pip_v = models.CharField(max_length=100, verbose_name = "Прізвище", null=True)
    truvalist = models.IntegerField(verbose_name = "Тривалість", null=True)
    city = models.CharField(max_length=100, verbose_name = "Місто", null=True)
    adress = models.CharField(max_length=100, verbose_name = "Адреса", null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата опублікування", null=True)
    pr = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Вид_послуг", null=True)
    vartist = models.IntegerField(verbose_name="Вартість", null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^0\d{9}$',
        message="Номер телефону повинен бути в форматі: '0XXXXXXXXX'. 10 цифр."
    )
    nomer_phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Номер телефону", blank=True,
                                   null=True)
    def __str__(self):
        return self.name

    def get_absol_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Курси'
        verbose_name_plural = 'Курси'
        ordering = ['-time_create']



