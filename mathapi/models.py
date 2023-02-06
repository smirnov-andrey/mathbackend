from django.db import models

from django.contrib.auth.models import User


class ContactModel(models.Model):
    '''Модель обратной связи'''
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact',
        verbose_name='Имя'
    )
    email = models.EmailField(max_length=255, verbose_name='Email')
    message = models.CharField(max_length=5000, verbose_name='Сообщение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class CategoryModel(models.Model):
    '''Модель категорий'''
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategoryModel(models.Model):
    '''Модель подкатегорий'''
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='subcategory',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class QuestionModel(models.Model):
    '''Модель работ'''
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название билета')
    description = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    question_text = models.TextField(null=True, blank=True, verbose_name='Тип - текст')
    question_file = models.FileField(upload_to='media/question_file', null=True, blank=True, verbose_name='Тип - скан')
    type = models.IntegerField(verbose_name='Тип данных')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    category = models.ForeignKey(
        SubCategoryModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='question',
        verbose_name='Категория'
    )

    def __str__(self):
        return f'{self.title} категория: {self.category}'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
