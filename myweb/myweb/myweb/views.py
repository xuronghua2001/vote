from django.http import HttpResponse,Http404
from .models import User
from django.shortcuts import redirect
from django.urls import reverse



def hellowdjango(request):
    return HttpResponse('Hellodjango')
def helloworld(request):
    return HttpResponse('Helloworld')

def get_user(request,id):
    if User.objects.filter(id=id).exists():
        return HttpResponse(str(User.objects.get(id=id)))
    else:
        # return redirect(reverse('index'))
        raise Http404('id not found')
