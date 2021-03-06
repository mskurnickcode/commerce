from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:post_id>", views.listing, name = "listing"),
    path("create", views.create, name = "create"),
    path("bid/<int:post_id>", views.bid, name = "bid"),
    path("watchlist/<int:post_id>", views.watchlist, name = "watchlist"),
    path("MyListings", views.myListings, name="myListings"),
    path("MyBids", views.myBiddings, name="myBiddings"),
    path("category/<str:category>", views.category, name="category")
]
