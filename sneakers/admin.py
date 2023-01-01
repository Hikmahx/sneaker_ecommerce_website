from .models import Sneaker, SneakerImgs, Sizes, Color
from django.contrib import admin

# Register your models here.
admin.site.register(Sneaker)
admin.site.register(SneakerImgs)
admin.site.register(Color)
admin.site.register(Sizes)
