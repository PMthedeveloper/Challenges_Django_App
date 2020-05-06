from django.shortcuts import render,redirect
from .models import Challenges
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
        pic = request.POST['pic']
        title = request.POST['title']
        timeStamp = request.POST['timeStamp']
        active_Solvers = request.POST['active_Solvers']
        Tags = request.POST['Tags']
        price = request.POST['price']
        contents = request.POST['contents']
        slug = request.POST['slug']
        Challenge = Challenges(pic=pic,title=title,timeStamp=timeStamp,active_Solvers=active_Solvers,Tags=Tags,price=price,contents=contents,slug=slug)
        Challenge.save();
        messages.success(request,"Your Challenge has been add Successfully!");
        return redirect(show)
    else:
        return render(request,'index.html')

def show(request):
    allPosts = Challenges.objects.all();
    context = {'allPosts': allPosts}
    return render(request,'show.html',context)

def Asc(request):
    CH = Challenges.objects.all().order_by('title')
    return render(request,'Asc.html',{'CH':CH});
def Dsc(request):
    CHs = Challenges.objects.all().order_by('-title')
    return render(request,'Dsc.html',{'CHs':CHs});