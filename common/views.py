from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from common.forms import UserForm


def logout_view(request):
    logout(request) # logout() 함수를 호출하여 세션을 종료
    return redirect('index')


def signup(request):
    '''
    회원가입
    '''
    if request.method == 'POST':  # POST 요청인 경우 (사용자가 회원가입 폼을 제출한 경우)
        form = UserForm(request.POST)  # UserForm 폼에 제출된 데이터를 담아옴
        if form.is_valid():  # 폼이 유효한지 검사 (유효성 검사)
            form.save()  # 유효하다면 폼을 저장 (회원가입을 완료)
            # 폼에서 사용자가 입력한 값 가져오기
            username = form.cleaned_data.get('username')  # username 필드 값
            raw_password = form.cleaned_data.get('password1')  # password1 필드 값 (비밀번호)
        
            ###회원가입 후 자동 로그인됨###
            # 사용자 인증 (입력한 username과 password로 로그인 시도)
            user = authenticate(username=username, password=raw_password)
            # 사용자 인증이 성공하면 로그인 처리
            login(request, user) 
            return redirect('index')# 로그인 후 index 페이지로 리다이렉트
    
    else: # GET 요청인 경우 (처음 회원가입 페이지를 열 때)
        form = UserForm()  # 빈 폼을 생성하여 사용자에게 전달
    
    # 회원가입 페이지 렌더링 (form 객체를 템플릿에 전달)
    return render(request, 'common/signup.html', {'form': form})