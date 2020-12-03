from django import forms
from .models import Post, bids
from datetime import datetime

item_categories = (
    ('0','Electronics' ), ('1', 'Home Goods'), ('2','Clothing'), ('3', 'Automotive'), ('4', 'Real Estate')
)

class PostForm (forms.Form):
    post_name = forms.CharField(label='Post Name', max_length=64)
    post_image = forms.URLField(label='URL of Item Image',max_length=128)
    post_text = forms.CharField(label='Item Description', widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))
    post_start_bid = forms.IntegerField(label= 'Starting Bid',min_value=0)
    post_end_date = forms.DateField(label='Set Auction End Date', widget=forms.SelectDateWidget())
    post_category = forms.ChoiceField(choices=item_categories)

class BidForm (forms.Form):
    bid = forms.IntegerField()
