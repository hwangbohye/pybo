from django.shortcuts import render, get_object_or_404,redirect, resolve_url #  render는 HTML 템플릿을 렌더링 모듈
from django.utils import timezone
from django.contrib import messages # 오류를 임의로 발생시키고자 하는 경우 사용(넌필드 오류에 해당당)
from django.contrib.auth.decorators import login_required

from ..models import Question, Answer, Comment
from ..forms import CommentForm


@login_required(login_url='common:login') # 로그인이 필요한 뷰
def comment_create_question(request, question_id):
    '''
    pybo 질문 댓글 등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST": #질문 등록 폼 제출 
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', question_id=question.id), comment.id))
    else: #GET #질문 등록 폼 요청
        form = CommentForm()
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)





@login_required(login_url='common:login') # 로그인이 필요한 뷰
def comment_modify_question(request, comment_id):
    '''
    pybo 질문 댓글 수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.question.id)
    
    if request.method == "POST": # 폼 제출한 경우 
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modified_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
    else: #GET # 폼 요청한 경우 
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'pybo/comment_form.html',context)





@login_required(login_url='common:login') # 로그인이 필요한 뷰
def comment_delete_question(request, comment_id):
    '''
    pybo 질문 댓글 삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.question.id)
    else:
        comment.delete()
    return redirect('pybo:detail', question_id=comment.question.id)




@login_required(login_url='common:login') # 로그인이 필요한 뷰
def comment_create_answer(request, answer_id):
    '''
    pybo 답변 댓글 등록
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST": #질문 등록 폼 제출 
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', question_id=comment.answer.question.id), comment.id))
    else: #GET #질문 등록 폼 요청
        form = CommentForm()
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)





@login_required(login_url='common:login') # 로그인이 필요한 뷰
def comment_modify_answer(request, comment_id):
    '''
    pybo 답변 댓글 수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.answer.question.id)
    
    if request.method == "POST": # 폼 제출한 경우 
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modified_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('pybo:detail', question_id=comment.answer.question.id),comment.id))
    else: #GET # 폼 요청한 경우 
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'pybo/comment_form.html',context)





@login_required(login_url='common:login') # 로그인이 필요한 뷰
def comment_delete_answer(request, comment_id):
    '''
    pybo 답변 댓글 삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다.')
        return redirect('pybo:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('pybo:detail', question_id=comment.answer.question.id)