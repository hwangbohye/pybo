from django import forms
from pybo.models import Question, Answer, Comment

# ModelForm을 상속받은 QuestionForm 클래스
    # 모델폼이란 '모델과 연결된 폼'이란 의미
class QuestionForm(forms.ModelForm):
    # Question 클래스의 '내부 클래스' Meta
        # 장고에서 모델폼은 '반드시' Meta라는 내부 클래스를 가져야 함 
        # Meta 클래스에서는는 모델폼이 사용할 모델과 모델의 필드를 정의해야 함 
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변 내용'
        } 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용'
        }