from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *


from .models import *


def index(request):
    listings = Post.objects.all()
    return render(request, "auctions/index.html", {
        'listings':listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing(request, post_id):
    listing = Post.objects.get(id = post_id)
    high_bid = bids.objects.filter(post_id=post_id).aggregate(Max('bid'))
    on_watchlist = Watchlist.objects.filter(post_id=post_id, user_id=request.user)
    return render(request, "auctions/listing.html", {
        "listing" : listing,
        "BidForm": BidForm(),
        "bid" : high_bid,
        "post_id": post_id,
        "watchlist": on_watchlist
        })

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user_id = request.user
            post_name = form.cleaned_data['post_name']
            post_image = form.cleaned_data['post_image']
            post_text = form.cleaned_data['post_text']
            post_start_bid = form.cleaned_data['post_start_bid']
            post_end_date = form.cleaned_data['post_end_date']
            post_category = form.cleaned_data['post_category']


            post = Post(user_id= user_id, post_name= post_name, post_image= post_image, post_text=post_text, post_start_bid=post_start_bid, post_end_date=post_end_date, post_category=post_category, post_date=datetime.datetime.now())
        print(post_name, post_category, post_end_date)
        post.save()
        listings = Post.objects.all()
        return render(request, "auctions/index.html", {
        'listings':listings
    })

    
    else:
        return render(request, "auctions/create.html", {
            'form': PostForm()
            })

def bid(request, post_id):
    if request.method == "POST":
        form = BidForm(request.POST or None)
        if form.is_valid():
            bid = form.cleaned_data['bid']
        
        user_id = request.user
        post_instance = Post.objects.get(id = post_id)
        bid_time = datetime.now()
        bid = bids(user_id=user_id, post_id=post_instance, bid=bid, bid_time=bid_time)
        bid.save()
        return listing(request, post_id)
    else:
        return index(request)

def watchlist(request, post_id):
    user_id = request.user
    post_instance = Post.objects.get(id = post_id)
    post_watched = Watchlist.objects.filter(user_id=user_id, post_id=post_instance)
    if post_watched:
        post_watched.delete()
        new_get = Watchlist.objects.all()


    else:
        add = Watchlist(user_id=user_id, post_id=post_instance, watch_current=True)
        add.save()
        new_get = Watchlist.objects.all()

    listing = Post.objects.get(id = post_id)
    high_bid = bids.objects.filter(post_id=post_id).aggregate(Max('bid'))
    on_watchlist = Watchlist.objects.filter(post_id=post_id, user_id=request.user)
    return render(request, "auctions/listing.html", {
        "listing" : listing,
        "BidForm": BidForm(),
        "bid" : high_bid,
        "post_id": post_id,
        "watchlist": on_watchlist
        })