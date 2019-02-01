from django.shortcuts import render
from django.http import HttpResponse
from fa.models import AccessRecord,Topic,Webpage

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request , 'fa/index.html',context = date_dict)
