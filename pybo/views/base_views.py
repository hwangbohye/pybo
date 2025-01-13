from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect #  render는 HTML 템플릿을 렌더링 모듈
from django.db.models import Q, Count

from ..models import Question

def index(request): # request는 장고에 의해 자동으으로 전달되는  HTTP 요청 객체임  
    """
    pybo 목록 출력
    """
 
    # 입력 인자
    page = request.GET.get('page', '1')  # 페이지 # /pybo/?page=1
    kw = request.GET.get('kw', '')       # 검색어
    so = request.GET.get('so', 'recent') # 정렬 기준

    # 정렬
    if so == 'recommend':
        # Question 객체에서 'voter' 필드의 개수를 세고, 'num_voter'로 임시 필드를 추가하여, 정렬에 활용
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date') # (-)역순 리스트
    elif so == 'popular':
        # Question 객체에서 'answer' 필드의 개수를 세고, 'num_answer'로 임시 필드를 추가하여, 정렬에 활용
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # so == 'recent'
        question_list = Question.objects.order_by('-create_date') #(-)역순 리스트

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)|                   # 제목 검색
            Q(content__icontains=kw)|                   # 내용 검색
            Q(author__username__icontains=kw)|           # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)    # 답변 글쓴이 검색
        ).distinct()

    # 페이징 처리 
    paginator = Paginator(question_list, 10) #question_list를 페이징 객체 Paginator로 변환 # 페이지당 10개씩 보여 주기 
    page_obj = paginator.get_page(page)
    
    context = {'question_list': page_obj, 'page':page, 'kw':kw , 'so':so} #조회한 데이터 context변수에 저장 # key:value
    return render(request, 'pybo/question_list.html', context) # 템플릿(pybo/question_list.html)을 렌더링하여 HTTP 응답을 생성





def detail(request, question_id): # question_id는 URL에 있던 question_id임
    """
    pybo 내용 출력
    """
    # pk(primary key == id)에 해당하는 데이터가 없으면 오류 대신, 404페이지
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)
