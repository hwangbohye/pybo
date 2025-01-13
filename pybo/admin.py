from django.contrib import admin
from .models import Question

# 장고 ADmin에서 데이터 검색 기능
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# admin에 Question모델 등록 
admin.site.register(Question, QuestionAdmin) 