from django.contrib import admin

from .models import CategoryModel, ContactModel, SubCategoryModel, QuestionModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'create_date')


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(SubCategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'type', 'create_date')

