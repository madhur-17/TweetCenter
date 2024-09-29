from django.shortcuts import render,get_object_or_404,redirect
from .models import Tweet
from .forms import TweetForm,UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')


def tweets_list(request):
    AllTweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweets_list.html',{'AllTweets':AllTweets})

@login_required
def tweets_create(request):
    if request.method=='POST':
        form =TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweets_list')
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})
    
@login_required
def tweets_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
        form =TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweets_list')
        
    else:
        form =TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})
    
@login_required  
def tweets_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweets_list')
    
    return render(request,'tweet_delete.html',{'tweet':tweet})


def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect("tweets_list")
        
    else:
        form=UserRegisterForm()
    return render(request,'registration/register.html',{'form':form})