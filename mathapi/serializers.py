from rest_framework import serializers

from .models import ContactModel, CategoryModel, SubCategoryModel, QuestionModel


class CaterorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ('id', 'title', 'description', 'subcategory')


class SubCategorySerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SubCategoryModel
        fields = ('id', 'title', 'description', 'category', 'category_id')


class QuestionSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = QuestionModel
        fields = ('title', 'description', 'question_text',
                  'question_file', 'type', 'create_date', 'category',
                  'category_id')

# class ContactSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = ContactModel
#         fields = '__all__'

