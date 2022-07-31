from django.shortcuts import render
from .models import posts
# Create your views here.
def home(request):
    Posts = posts.objects.all()
    return render(request,'home.html', {'Posts':Posts})

def upload(request):
    if request.method=='POST':
        title=request.POST['title']
        post=request.POST['post']
        port=posts(title=title,body=post)
        port.save()
    return render(request,'upload.html' )

