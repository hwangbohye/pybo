from django.urls import path
from .views import answer_views, base_views, question_views, comment_views, vote_views

app_name = 'pybo' # 네임 스페이스 지정 

urlpatterns = [
    # base_views
    path("", base_views.index, name='index'), # "pybo/" URL은 views.index함수와 연결
    path("<int:question_id>/",  base_views.detail, name='detail'),  # "pybo/{question_id}/" URL은 views.detail함수와 연결
    #answer_views
    path("answer/create/<int:question_id>/", answer_views.answer_create , name="answer_create"),
    path("answer/modify/<int:answer_id>/", answer_views.answer_modify, name="answer_modify"), # answer_id를 answer_modify에 넘겨줌 
    path("answer/delete/<int:answer_id>/", answer_views.answer_delete, name="answer_delete"), # answer_id를 answer_delete에 넘겨줌 
    #question_views
    path("question/create/", question_views.question_create , name="question_create"),
    path("question/modify/<int:question_id>/", question_views.question_modify, name='question_modify'), # question_id를 question_modify에 넘겨줌 
    path("question/delete/<int:question_id>/", question_views.question_delete, name="question_delete"), # question_id를 question_delete에 넘겨줌 
    # comment_views
    path("comment/create/question/<int:question_id>/", comment_views.comment_create_question, name="comment_create_question"),
    path("comment/modify/question/<int:comment_id>/", comment_views.comment_modify_question, name="comment_modify_question"),
    path("comment/delete/question/<int:comment_id>/", comment_views.comment_delete_question, name="comment_delete_question"),
    path("comment/create/answer/<int:answer_id>/", comment_views.comment_create_answer, name="comment_create_answer"),
    path("comment/modify/answer/<int:comment_id>/", comment_views.comment_modify_answer, name="comment_modify_answer"),
    path("comment/delete/answer/<int:comment_id>/", comment_views.comment_delete_answer, name="comment_delete_answer"),
    # vote_views
    path("vote/question/<int:question_id>/", vote_views.vote_question , name="vote_question"), 
    path("vote/answer/<int:answer_id>/", vote_views.vote_answer , name="vote_answer"),
]  