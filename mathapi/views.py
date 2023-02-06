from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import ContactModel, CategoryModel, SubCategoryModel, QuestionModel
from .serializers import CaterorySerializer, SubCategorySerializer, QuestionSerializer


class CategoryListAPIView(ListAPIView):
    '''List categories'''
    queryset = CategoryModel.objects.all()
    serializer_class = CaterorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
    '''Detail categories'''
    queryset = CategoryModel.objects.all()
    serializer_class = CaterorySerializer


class SubCategotyListAPIView(ListAPIView):
    '''List subcategories all/category_id=pk'''
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return SubCategoryModel.objects.all().select_related('category')
        return SubCategoryModel.objects.filter(category_id=pk).select_related('category')


class SubCategoryDetailAPIView(RetrieveAPIView):
    '''Detail subcategory'''
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategorySerializer


class QuestionListAPIView(ListAPIView):
    '''List question all/pk_subcat/pk_cat'''
    serializer_class = QuestionSerializer

    def get_queryset(self):
        # pk_subcat = self.kwargs.get('pk_subcat')
        # pk_cat = self.get('pk_cat')
        if self.kwargs.get('pk_subcat'):
            pk_subcat = self.kwargs.get('pk_subcat')
            return QuestionModel.objects.filter(category_id=pk_subcat).select_related('category')
        if self.kwargs.get('pk_cat'):
            pk_cat = self.kwargs.get('pk_cat')
            return QuestionModel.objects.filter(category__category_id=pk_cat).select_related('category')
        else:
            return QuestionModel.objects.all().select_related('category')


class DetailWorkAPIView(RetrieveAPIView):
    '''Detail question'''
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

# class ContactModelViewSet(ModelViewSet):
#     queryset = ContactModel.objects.all()
#     serializer_class = ContactSerializers



