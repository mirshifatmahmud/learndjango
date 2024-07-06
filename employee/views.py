
from django.http import HttpResponse



def employee(request):
    return HttpResponse('This is oure employee page')

def profile(reqest):
    return HttpResponse('My Profile Page')