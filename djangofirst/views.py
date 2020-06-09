from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from djangofirst.models import Topic,Webpage,AccessRecord
from faker import Faker
from . import forms



def add_topic():
    t = Topic.objects.get_or_create(top_name="tyyyuyopppppppp")[0]
    t.save()
    return t

def populate(N=5):
    for i in range(N):
        fake = Faker()
        web_name=fake.company()
        web_url=fake.url()
        webpage=Webpage.objects.get_or_create(topic=add_topic(),name=web_name,url=web_url)[0]
        webpage.save()
        accessrecord = AccessRecord.objects.get_or_create(name=webpage, date=fake.date())[0]
        accessrecord.save()


def index(request):
    # return HttpResponse(__file__)
    # import pdb;pdb.set_trace()
    # populate(15)

    return render(request,"djangofirst/index.html",{"insert_me": AccessRecord.objects.all()})


def help(request):
    # return HttpResponse(__file__)
    return render(request,"djangofirst/help.html",{"insert_me": "HEYvYYYY"})

def form_function(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        # import pdb;pdb.set_trace()
        if form.is_valid():
            return render(request, "djangofirst/index.html", {"form": form})
    return render(request,"djangofirst/form_p.html",{"form":form})
