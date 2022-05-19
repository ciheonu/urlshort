from django.http import HttpResponse
from django.shortcuts import render, redirect
import uuid
from .models import URL
# Create your views here.


def home(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = URL(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def final(request, pk):
    url_details = URL.objects.get(uuid=pk)
    return redirect(url_details.link)
