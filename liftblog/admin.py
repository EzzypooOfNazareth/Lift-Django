from django.contrib import admin
from . import models

admin.site.register(models.TextPost)
admin.site.register(models.VideoPost)
admin.site.register(models.HomeCarousel)
admin.site.register(models.HomeCarouselText)
