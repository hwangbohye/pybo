from django.shortcuts import render, get_object_or_404,redirect, resolve_url #  render는 HTML 템플릿을 렌더링 모듈
from django.utils import timezone
from django.contrib import messages # 오류를 임의로 발생시키고자 하는 경우 사용(넌필드 오류에 해당당)
from django.contrib.auth.decorators import login_required

from ..models import Question, Answer
from ..forms import AnswerForm

 
@login_required(login_url='common:login') #함수 실행 전, 로그인 여부 검사
def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    # 질문 ID에 해당하는 Question 객체를 가져오거나 없으면 404 오류 반환
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST': # 사용자가 제출했을 경우
        form = AnswerForm(request.POST) #제출한 폼 내용 
        if form.is_valid():
            answer = form.save(commit=False) # commit=False는 임시 저장을 의미
            answer.author = request.user #현재 로그인한 계정의 User객체
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect( '{}#answer_{}'.format( resolve_url( 'pybo:detail', question_id=question.id ), answer.id ) )
    else: #get일 경우 # 사용자가 폼 요청했을 경우 
        form = AnswerForm()
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)



@login_required(login_url='common:login') # 로그인이 필요한 뷰
def answer_modify(request, answer_id):
    '''
    pybo 답변 수정
    '''
    answer = get_object_or_404(Answer, pk=answer_id)

    # 현재 user가 작성자 아닌 경우
    if(request.user != answer.author):
        messages.error(request, '수정권한이 없습니다.')
        redirect('pybo:detail', question_id=answer.question.id)

    # 현재 user가 작성자인 경우
    if request.method =='POST': #폼을 제출한 경우 
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False) #임시 저장
            answer.author = request.user
            answer.modified_date = timezone.now()
            answer = form.save()#DB에 반영
            return redirect( '{}#answer_{}'.format( resolve_url( 'pybo:detail', question_id=answer.question.id ), answer.id) )
    else: #GET#폼을 요청한 경우 
        form = AnswerForm(instance=answer)
    context = {'answer':answer, 'form': form }
    return render(request, 'pybo/answer_form.html', context)




@login_required(login_url='common:login') # 로그인이 필요한 뷰
def answer_delete(request, answer_id):
    '''
    pybo 답변 삭제 
    '''
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id) 
