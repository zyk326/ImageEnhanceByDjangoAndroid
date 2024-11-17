from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
import random
import string
from django.core.mail import send_mail
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, Login_form
from django.contrib.auth import get_user_model, login, logout

User = get_user_model()

# Create your views here.
@require_http_methods(['GET', 'POST'])
def zyklogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = Login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                return redirect('/')
            else:
                print('邮箱或者密码错误')
                # form.add_error('email', '邮箱或者密码错误')
                # return render(request, 'login.html', {'form': form})
                return redirect(reverse('zykauth:login'))

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create_user(email=email, password=password, username=username)
            return redirect(reverse('zykauth:login'))
        else:
            print(form.errors)
            return redirect(reverse('zykauth:register'))

def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code':"400", 'message':'必须传递邮箱'})
    # 生成验证码
    captcha = "".join(random.sample(string.digits, 4))
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail("博客注册验证码", message=f"您的注册验证码是：{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({"code":"200", "message":"邮箱发送成功！"})

def zyklogout(request):
    logout(request)
    return redirect('/')