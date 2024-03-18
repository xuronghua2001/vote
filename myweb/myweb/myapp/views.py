from django.shortcuts import render,redirect
from django.forms import model_to_dict

from django.http import HttpResponse,Http404,JsonResponse
import datetime
from .models import Stu,myapp_users
# Create your views here.

def index(request):
    return HttpResponse(str(datetime.datetime.now()))
def plus(request,num1,num2):
    return HttpResponse("{0}+{1}={2}".format(num1,num2,int(num1)+int(num2)))
def stu(request):
    lists = Stu.objects.all()
    print(Stu.objects.get(id=1))
    # print(lists)
    return HttpResponse("ok")

def plus_named(request,num1,num2):
    return HttpResponse("{0}+{1}={2}".format(num1,num2,int(num1)+int(num2)))

def info(request):
    response = HttpResponse('ok')
    response.set_cookie('key','value')
    if request.method == 'GET':
        id = request.GET['id']
        name = request.GET.get('name',None)
        age = request.GET.get('age', None)
        telephone = request.GET.get('phone',None)

    return response

def user(request):
    users = myapp_users.objects.all()
    context = {'data': users}
    # return JsonResponse(data, safe=False)
    return render(request,'userinfo.html',context)

    # return HttpResponse(str(myapp_users.objects.all()[0]))

def add_user(request):
    context = {'data': datetime.datetime.now()}
    # return JsonResponse(data, safe=False)
    return render(request, 'adduser.html', context)

def add(request):
    if request.method == 'GET':
        id = request.GET['id']
        name = request.GET.get('name',None)
        age = request.GET.get('age', None)
        phone = request.GET.get('phone',None)

    else:
        id = request.POST['id']
        name = request.POST.get('name', None)
        age = request.POST.get('age', None)
        phone = request.POST.get('phone', None)
    user = myapp_users()
    user.id = id
    user.name = name
    user.age = age
    user.phone = phone
    user.addtime = str(datetime.datetime.now())
    user.save()
    context = {'data': datetime.datetime.now()}
    return render(request, 'adduser.html', context)

def delete_user(request,id):
    user = myapp_users()
    user.id = id
    # user.save()
    user.delete()
    return redirect('/myapp/user')


def edit_user(request,id):
    users = myapp_users.objects.get(id=id)
    context = {'user': users}
    # return JsonResponse(data, safe=False)
    return render(request, 'edituser.html', context)