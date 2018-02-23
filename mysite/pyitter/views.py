from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm
# Create your views here.


@login_required
def tweet_index(request):
    tweets = Tweet.objects.all()
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user_id = request.user
            tweet.save()
            return redirect('/')
    else:
        form = TweetForm()
    return render(request,
                  'pyitter/tweet_index.html',
                  {'tweets': tweets, 'form': form})
