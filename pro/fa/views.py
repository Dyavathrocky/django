from django.shortcuts import render
from django.http import HttpResponse
from fa.models import AccessRecord,Topic,Webpage
from . import forms
from forms import Form

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request , 'fa/index.html',context = date_dict)

def form_name_view(request):
    form = forms.Form()
    return  render(request,'form_name.html',{'form':form})
