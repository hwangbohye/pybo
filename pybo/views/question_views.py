from django.shortcuts import render, get_object_or_404,redirect #  render는 HTML 템플릿을 렌더링 모듈
from django.contrib import messages # 오류를 임의로 발생시키고자 하는 경우 사용(넌필드 오류에 해당당)
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ..models import Question
from ..forms import QuestionForm



@login_required(login_url='common:login') #함수 실행 전, 로그인 여부 검사
def question_create(request):
    """
    pybo 질문 등록 
    """
    if request.method == 'POST': # 사용자가 폼을 제출한 경우
        form = QuestionForm(request.POST)
        if form.is_valid(): # 폼의 입력 데이터가 유효한지 검사
            question = form.save(commit=False) # commit=False는 임시 저장을 의미 
            question.author = request.user #현재 로그인한 계정의 User객체
            question.create_date = timezone.now()
            question.save() # 실제 저장
            return redirect('pybo:index') #질문 등록이 완료된 후, 질문 목록 페이지로 이동
    else:
        form = QuestionForm() # get인 경우 호출 # 즉, 폼을 요청할 경우 실행

    context = {'form':form}
    return render(request, 'pybo/question_form.html', context) # context를 전달하여, form 요소 생성에 사용할거임 
 





@login_required(login_url='common:login') # 로그인이 필요한 뷰
def question_modify(request, question_id):
    '''
    pybo 질문 수정 
    ''' 
    # question_id에 해당하는 Question 객체 가져오기, 없으면 404 오류 반환
    question = get_object_or_404(Question, pk=question_id)
    
    # 현재 user가 작성자가 아닌 경우
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)

    # 현재 user가 작성자인 경우
    if request.method == "POST": # 폼 제출한 경우 
        # instance=question 통해, 사용자가 제출한 데이터를 기존 question 객체에 채워넣기 
        form = QuestionForm(request.POST, instance=question)  
        if form.is_valid():
            question = form.save(commit=False) 
            question.author = request.user # 보안과 데이터 무결성을 유지하기 위해
            question.modified_date = timezone.now()
            question.save() # 저장 (DB 반영)
            return redirect('pybo:detail', question_id=question.id)
    else: # GET # 폼 요청한 경우'    
        # instance=question 통해, 사용자가 제출한 데이터를 기존 question 객체 상태에서 시작
        # 기존 질문 데이터를 채운 상태로 폼 생성
        form = QuestionForm(instance=question) # 폼 생성
        
    # 템플릿에 전달할 데이터 설정
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)




@login_required(login_url='common:login') # 로그인이 필요한 뷰
def question_delete(request, question_id):
    '''
    pybo 질문 삭제
    '''
    question = get_object_or_404(Question, pk=question_id) #Question 테이블에서 pk=question_id인 데이터 찾아오기 

    # 현재 user가 작성자 아닌 경우
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    # 현재 user가 작성자인 경우
    question.delete()
    return redirect('pybo:index')
