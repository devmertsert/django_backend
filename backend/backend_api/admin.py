from django.contrib import admin

# Register your models here.
from .models import User, Movie, WatchList

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(WatchList)
