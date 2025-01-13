from django.shortcuts import get_object_or_404,redirect #  render는 HTML 템플릿을 렌더링 모듈
from django.contrib import messages # 오류를 임의로 발생시키고자 하는 경우 사용(넌필드 오류에 해당당)
from django.contrib.auth.decorators import login_required

from ..models import Question, Answer


@login_required(login_url='common:login') #함수 실행 전, 로그인 여부 검사
def vote_question(request, question_id):
    '''
    pybo 질문 추천 등록 
    '''
    question = get_object_or_404(Question, pk=question_id)
    
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)



@login_required(login_url='common:login') #함수 실행 전, 로그인 여부 검사
def vote_answer(request, answer_id):
    '''
    pybo 답변 추천 등록 
    '''
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)