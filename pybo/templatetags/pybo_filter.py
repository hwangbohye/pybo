import markdown
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter # 이 함수를 템플릿 필터로 등록
def sub(value, arg):
    return value - arg


@register.filter # 이 함수를 템플릿 필터로 등록
def mark(value): # value는 필터가 처리할 텍스트
    
    #확장 도구 설정
    extentions = ["nl2br","fenced_code"] #"nl2br 줄바꿈 # "fenced_code" 마크다운의 소스코드 표현을 위한 도구

    # marksafe 안전한 HTML로 인식하도록 html코드로 변환
    return mark_safe(markdown.markdown(value, extensions=extentions))# extensions로로 마크다운 규칙 확장 반영