from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
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
    return render(request, "auctions/listing.html", {
        "listing" : listing
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
