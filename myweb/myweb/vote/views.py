from datetime import datetime

from django.contrib import messages
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Vote, Vote_user


# Create your views here.
class Register(View):
    def post(self, request):
        if request.method == 'POST':
            user_name = request.POST.get('username', '')
            pwd = request.POST.get('password', '')
            if User.objects.filter(username=user_name).exists():
                return HttpResponse('用户已存在')
            else:
                user = User.objects.create_user(
                    username=user_name,
                    password=pwd,
                    email=str(user_name) + '@qq.com',
                    is_staff=1,
                    is_active=1,
                    is_superuser=0
                )
                user.save()
                return HttpResponse('用户注册成功')


class Login(View):
    def post(self, request):
        if request.method == 'POST':
            user_name = request.POST.get('username', '')
            pwd = request.POST.get('password', '')
            if User.objects.filter(username=user_name).exists():
                user = authenticate(username=user_name, password=pwd)
                if user:
                    if user.is_active:
                        login(request,user)
                        request.session['username'] = user_name
                        request.session['password'] = pwd
                        messages.error(request, user_name+'登陆成功')
                        return redirect('/vote')
                    else:
                        messages.error(request, '用户未激活')
                        return redirect('/vote')
                else:
                    messages.error(request, '用户认证失败')
                    return redirect('/vote')
            else:
                messages.info(request, '用户不存在')
                return redirect('/vote')
            # return render(request, 'votelogin.html')


def logout_view(request):
    # 执行注销操作，这将清除会话数据并注销用户
    logout(request)
    # 注销后重定向到指定页面，例如登录页面
    return redirect('/vote')

class Logout(View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            exists = User.objects.filter(username=username).exists()

            if not exists:
                return redirect('/vote')
            user = authenticate(username=username, password=password)
            if user:
                logout(request)
                request.session.flush()
                return redirect('/vote')
                # return HttpResponse('退出')


@csrf_exempt
def vote_info(request):
    vote = Vote.objects.all()
    list = vote.order_by("id")
    paginator = Paginator(list, 4)
    page = request.POST.get('page')
    print(page,3)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    context = {'data': vote, 'date': str(datetime.now()), 'contacts': contacts,
               'username': request.session.get('username', default='访客')}
    return render(request, 'vote.html', context)


def delete_vote(request, id):
    vote = Vote()
    vote.id = id
    vote.delete()
    return redirect('/vote')


def add_vote(request):
    if request.method == 'GET':
        user_name = request.GET.get('create_user')
        id = request.GET.get('id', None)
        subject = request.GET.get('subject', None)
        create_time = request.GET.get('create_time', None)
        end_time = request.GET.get('end_time', None)

    else:
        user_name = request.POST.get('create_user')
        id = request.POST.get('id', None)
        subject = request.POST.get('subject', None)
        create_time = request.POST.get('create_time', datetime.now())
        end_time = request.POST.get('end_time', datetime.now())
    vote = Vote()
    vote.id = id
    vote.subject = subject
    vote.create_date = create_time
    # vote.create_date = str(datetime.datetime.now())
    vote.end_date = end_time
    vote.create_user = user_name
    vote.save()
    return redirect('/vote')


def edit_vote(request, id):
    vote = Vote.objects.get(id=id)
    context = {'vote': vote}
    vote.create_date = vote.create_date.strftime('%Y-%m-%d')
    vote.end_date = vote.end_date.strftime('%Y-%m-%d')

    # return JsonResponse(data, safe=False)
    return render(request, 'editvote.html', context)
    # return render(request, 'vote.html', context)


def display_user_vote(request):
    user_name = request.POST.get('username')
    # vote_counts = Vote.objects.all().values('id')
    vote_subjects = Vote.objects.filter(create_user=user_name).values('subject').distinct().annotate(subject_count=Count('subject')).order_by('subject')
    subject = [item['subject'] for item in vote_subjects]
    counts = [item['subject_count'] for item in vote_subjects]
    context = {'subjects': subject,'subject_count':counts}
    # return HttpResponse(vote_subjects)
    return render(request, 'display_user_vote.html', context)