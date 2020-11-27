# Generated by Django 3.1.3 on 2020-11-25 20:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=64)),
                ('post_image', models.URLField(max_length=128)),
                ('post_text', models.CharField(max_length=250)),
                ('post_start_bid', models.PositiveIntegerField()),
                ('post_date', models.DateTimeField()),
                ('post_end_date', models.DateField()),
                ('post_category', models.CharField(max_length=25)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_current', models.BooleanField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.PositiveIntegerField()),
                ('bid_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]