from django.urls import path

from rest_framework import routers

from .views import (CategoryListAPIView, CategoryDetailAPIView,
                    SubCategotyListAPIView, SubCategoryDetailAPIView,
                    QuestionListAPIView, DetailWorkAPIView)

# from .views import ContactModelViewSet


router = routers.DefaultRouter()
# router.register(r'contact', ContactModelViewSet, basename='contact')

urlpatterns = [
    # List categories
    path('categories/', CategoryListAPIView.as_view()),
    # Detail category
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    # List subcateries category_id=pk
    path('categories/<int:pk>/subcategories/',
         SubCategotyListAPIView.as_view()),
    # List call subcategories
    path('subcategories/', SubCategotyListAPIView.as_view()),
    # Detail subcategory
    path('subcategories/<int:pk>/', SubCategoryDetailAPIView.as_view()),
    # List works category_id=pk_cat
    path('categories/<int:pk_cat>/works/', QuestionListAPIView.as_view()),
    # List works subcategory_id=pk_subcat
    path('subcategories/<int:pk_subcat>/works/',
         QuestionListAPIView.as_view()),
    # List all works
    path('works/', QuestionListAPIView.as_view()),
    # Detail subcategory
    path('works/<int:pk>/', DetailWorkAPIView.as_view()),

]

# urlpatterns += router.urls