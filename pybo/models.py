from django.db import models # models는 Django에서 데이터베이스 테이블을 정의하고 관리하는 데 사용되는 모듈
from django.contrib.auth.models import User

# Question 클래스는 models.Model을 상속
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    voter = models.ManyToManyField(User, related_name='voter_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modified_date = models.DateTimeField(null=True, blank=True)

    # 모델 데이터 조회시 속성값 보여주기 위한 코드
    def __str__(self):
	    return self.subject #객체의 subject 속성 반환

# Answer 클래스는 models.Model을 상속
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    voter = models.ManyToManyField(User, related_name='voter_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField() 
    modified_date = models.DateTimeField(null=True, blank=True)


# Comment 클래스는 models.Model을 상속
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField() 
    modified_date = models.DateTimeField(null=True, blank=True)
    # 질문 또는 답변에 질문이 달릴거임, 그러므로 질문과 답변 필드 모두 null=True, blank=True로 설정 
        # 질문에 달린 댓글에 대해서는 답변 필드는 비어있고, 
        # 답변에 달린 댓글에 대해서는 질문 필드는 비어있고, 
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)